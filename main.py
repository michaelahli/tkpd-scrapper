import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()

print('name, desc, detail, price, image, store, rating')

class Product():
    def __init__(self, detail, name, desc, price, image, store, rating):
        self.detail = detail
        self.name = name
        self.desc = desc
        self.price = price
        self.image = image
        self.store = store
        self.rating = rating
    
    def __str__(self):
        return "%s,%s,%s,%s,%s,%s,%s" % (
            repr(self.name), 
            repr(self.desc), 
            repr(self.detail),
            repr(self.price), 
            repr(self.image), 
            repr(self.store),
            repr(self.rating)
        )

class Bot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=os.environ.get('DRIVER_LOC'))
        self.list_products = []

    def open_dashboard(self, uri):
        self.driver.get(uri)
        sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        list_products = self.driver.find_elements(By.XPATH,'//*[@id="zeus-root"]/div/div[2]/div/div[2]/div/div[2]/div[3]/div[2]/div[3]/div')
        for i, product in enumerate(list_products):
            product_name = product.find_elements(By.XPATH, './/a/div[2]/div[2]/span')
            for a in product_name:
                product_name_str = a.text.replace(",", "")
            product_price = product.find_elements(By.XPATH, './/a/div[2]/div[2]/div[1]/div/span')
            for a in product_price:
                product_price_str = a.text.replace(",", "")
            store_name = product.find_elements(By.XPATH, './/a/div[2]/div[2]/div[2]/div/span')
            for a in store_name:
                store_name_str = a.text.replace(",", "")
            detail_page = product.find_element(By.XPATH, './/a')
            self.list_products.append(Product(detail_page.get_attribute("href"), product_name_str,"",product_price_str,"",store_name_str,""))

    def open_detail(self, detail_uri):
        self.driver.get(detail_uri)
        global product_rate
        global product_desc
        global product_store
        global product_image
        sleep(1)
        rating = self.driver.find_elements(By.XPATH, '//*[@id="pdp_comp-product_content"]/div/div[1]/div/div[2]/span[1]/span[2]')
        for a in rating:
            product_rate = a.text.replace(",", "")
        desc = self.driver.find_elements(By.XPATH, '//*[@id="pdp_comp-product_detail"]/div[2]/div[2]/div/span/span/div')
        for a in desc:
            product_desc = a.text.replace(",", "")
        store = self.driver.find_elements(By.XPATH, '//*[@id="pdp_comp-shop_credibility"]/div[2]/div[1]/div/a/h2')
        for a in store:
            product_store = a.text.replace(",", "")
        image = self.driver.find_elements(By.XPATH, '//*[@id="pdp_comp-product_media"]/div/div[1]/div/div[2]/img')
        for a in image:
            product_image = a.get_attribute("src")
        return [product_desc,product_rate,product_store,product_image]

scrapper = Bot()

page_num = 0
while len(scrapper.list_products) < 100:
    page_num = page_num + 1
    scrapper.open_dashboard(os.environ.get('TARGET_URI')+str(page_num))
    for i, product in enumerate(scrapper.list_products):
        if "ta.tokopedia.com/promo/v1/" not in product.detail: 
            res = scrapper.open_detail(product.detail)
            scrapper.list_products[i].desc = res[0]
            scrapper.list_products[i].rating = res[1]
            scrapper.list_products[i].store = res[2]
            scrapper.list_products[i].image = res[3]

for i, product in enumerate(scrapper.list_products):
    if product.desc != "":
        print(product)
    
