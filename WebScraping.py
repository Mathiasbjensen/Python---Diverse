from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"

# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class":"item-container"})

filename = "products.csv"
# w for 'write'.
f = open(filename, "w")

# Headers for csv file
headers = "brand; product_name; shipping; price\n"

f.write(headers)
# grabs each product

for container in containers:
# Some objects do n ot have such attributes, therefor attribute exception is needed.
    try:
        brand = container.div.div.a.img["title"]
    except: AttributeError


    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    try:

        price_container = container.findAll("li", {"class":"price-current"})
        price = price_container[0].text.strip()
        price_stripped = re.findall(r"[$]\S*",price)[0]

    except: TypeError


    print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)
    print("price: " + price_stripped)

    f.write(brand + ";" + product_name.replace(",", "|") + ";" + shipping + ";" + price_stripped + "\n")

f.close()






