import requests
from bs4 import BeautifulSoup



for i in range(1,3):
    url = "https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)

    r = requests.get(url)
                    # print(r)
    soup = BeautifulSoup(r.text, "lxml")
        # box = soup.find("div",class_ = "DOjaWF gdgoEp")
    
    products_tag = soup.findAll("div" , class_="tUxRFH")
    
    productdic = {}
    
    for product in  products_tag:
        

        names = product.find("div",class_ = "KzDlHZ")


        prices = product.find("div",class_ = "Nx9bqj _4b5DiR")

        productdic["name"] = names.text.strip()
        productdic["price"] = prices.text.strip()
        
        print(productdic)
    



    
    
    
