import requests
from bs4 import BeautifulSoup
import time


#Input for skroutz link
def initializer():
    print('Please provide a skroutz product link:')
    url = input()   
    return url
    
#compares starting price with price it gets in every search and prints the result
def check_Currentprice(price,URL):
    curr = price
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find_all('span', attrs={'itemprop':'lowPrice'})
    for span in price:
        semiconverted_price = span.string
    converted_Currentprice = float(semiconverted_price[0:2])
    if(converted_Currentprice==curr):
        print('Price is still the same')
    elif(converted_Currentprice<curr):
        print('Price went down.')
    elif(converted_Currentprice>curr):
        print('Price went up')
    
#The first time the script runs it saves the product price to compare it with every search
def get_startingPrice(URL):
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find_all('span', attrs={'itemprop':'lowPrice'})
    for span in price:
        semiconverted_price = span.string
    converted_Currentprice = float(semiconverted_price[0:2])
    return converted_Currentprice

url = initializer()
price = get_startingPrice(url)
while(True):
    check_Currentprice(price,url)
    time.sleep(60*60*24)
