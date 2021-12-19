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