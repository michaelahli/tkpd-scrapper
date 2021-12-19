import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()

# csv header
print('name, desc, detail, price, image, store, rating')

# selenium available command dictionary
command = {
    "scroll": "window.scrollTo(0, document.body.scrollHeight);"
}

# target XPATH dictionary
xpath = {
    "listProducts": '//*[@id="zeus-root"]/div/div[2]/div/div[2]/div/div[2]/div[3]/div[2]/div[3]/div',
    "detailPage": './/a',
    "productName": './/a/div[2]/div[2]/span',
    "productPrice": './/a/div[2]/div[2]/div[1]/div/span',
    "productRating": '//*[@id="pdp_comp-product_content"]/div/div[1]/div/div[2]/span[1]/span[2]',
    "productDescription":'//*[@id="pdp_comp-product_detail"]/div[2]/div[2]/div/span/span/div',
    "productStore": '//*[@id="pdp_comp-shop_credibility"]/div[2]/div[1]/div/a/h2',
    "productImage": '//*[@id="pdp_comp-product_media"]/div/div[1]/div/div[2]/img'
}

# Product entity
class Product():
    def _init_(self, detail, name, desc, price, image, store, rating):
        self.detail = detail
        self.name = name
        self.desc = desc
        self.price = price
        self.image = image
        self.store = store
        self.rating = rating
    
    def _str_(self):
        return "%s,%s,%s,%s,%s,%s,%s" % (
            repr(self.name), 
            repr(self.desc), 
            repr(self.detail),
            repr(self.price), 
            repr(self.image), 
            repr(self.store),
            repr(self.rating)
        )

# method to get value from elements
def GetListValues(list):
    for a in list:
        return a.text.replace(",", "")

# Bot entity
class Bot():
    def _init_(self):
        self.driver = webdriver.Chrome(executable_path=os.environ.get('DRIVER_LOC'))
        self.list_products = []

    def open_dashboard(self, uri):
        self.driver.get(uri)
        
        sleep(1)
        
        self.driver.execute_script(command["scroll"])
        
        list_products = self.driver.find_elements(By.XPATH,xpath["listProducts"])
        
        for product in list_products:
            detail_page = product.find_element(By.XPATH, xpath["detailPage"])
            product_name = product.find_elements(By.XPATH, xpath["productName"])
            product_price = product.find_elements(By.XPATH, xpath["productPrice"])
            
            product_name_str = GetListValues(product_name)
            product_price_str = GetListValues(product_price)
            
            self.list_products.append(Product(detail_page.get_attribute("href"), product_name_str,"",product_price_str,"","",""))

    def open_detail(self, detail_uri):
        self.driver.get(detail_uri)

        global product_rate
        global product_desc
        global product_store
        global product_image

        sleep(1)

        rating = self.driver.find_elements(By.XPATH, xpath["productRating"])
        desc = self.driver.find_elements(By.XPATH, xpath["productDescription"])
        store = self.driver.find_elements(By.XPATH, xpath["productStore"])
        
        product_rate = GetListValues(rating)
        product_desc = GetListValues(desc)
        product_store = GetListValues(store)

        image = self.driver.find_elements(By.XPATH, xpath["productImage"])

        for a in image:
            product_image = a.get_attribute("src")

        return [product_desc,product_rate,product_store,product_image]

scrapper = Bot()

page_num = 0
while len(scrapper.list_products) < 100:
    page_num = page_num + 1

    # get initial data (list products)
    scrapper.open_dashboard(os.environ.get('TARGET_URI')+str(page_num))
    
    # get data from detailed uri
    for i, product in enumerate(scrapper.list_products):
        # some url is protected in tokopedia, cannot fetch data from it
        if os.environ.get('PROTECTED_URI') not in product.detail: 
            res = scrapper.open_detail(product.detail)

            scrapper.list_products[i].desc = res[0]
            scrapper.list_products[i].rating = res[1]
            scrapper.list_products[i].store = res[2]
            scrapper.list_products[i].image = res[3]

for i, product in enumerate(scrapper.list_products):
    # validate data
    if product.desc != "":
        print(product)