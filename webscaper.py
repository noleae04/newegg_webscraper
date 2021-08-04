# Imports
import requests
from requests import get
from bs4 import BeautifulSoup as soup
import numpy as np
import csv

# Parses website
headers = {"Accept-Language": "en-US, en;q=0.5"}
url = "https://www.newegg.com/p/pl?d=graphics+card&page=1"
results = requests.get(url, headers=headers)
soupy = soup(results.text, "html.parser")

csv_file = open('newegg_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_file.write("Brand Product Price Shipping Ratings URL\n")

# Fetches each product
containers = soupy.find_all('div', class_='item-container')

for container in containers:
    title = container.a.img['title']
    url = container.a['href'].strip()
    try:
        brand = container.div.img['title']
        price = container.find('li', class_ = 'price-current').text
        shipping = container.find('li', class_= 'price-ship').text
        ratingNum = container.find('span', class_= 'item-rating-num').text

    except:
        brand = 'Undefined'
        price = 'Unavailable'
        shipping = 'Direct'
        ratingNum = 'No ratings'

    csv_file.write(brand.replace(" " , "|") + " " + title.replace(" " , "|") + " " + price.replace(" " , "|") + " " + shipping.replace(" " , "|") + " " + ratingNum.replace(" " , "|") + " " + url.replace(" " , "") + "\n")

newegg = {
    'Brand' : brand,
    'Name' : title,
    'Price' : price,
    'Shipping Cost' : shipping,
    'Rating' : ratingNum,
    'URL' : url
}
    
csv_file.close()