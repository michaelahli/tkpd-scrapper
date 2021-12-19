import os
from dotenv import load_dotenv
from src.dictionary.dictionary import command, xpath
from src.utils.utils import GetListValues
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()

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