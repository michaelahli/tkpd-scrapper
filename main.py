import os
from dotenv import load_dotenv
from src.entity.entity import Bot

load_dotenv()

# csv header
print('name, desc, detail, price, image, store, rating')

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