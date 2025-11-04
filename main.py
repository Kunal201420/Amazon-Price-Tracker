import requests
from bs4 import BeautifulSoup
import os
import smtplib

AMAZON_ENDPOINT = os.getenv("AMAZON_ENDPOINT")
EMAIL_ID = os.getenv("EMAIL_ID")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}


response = requests.get(AMAZON_ENDPOINT, headers=header)
response_data = response.text

soup = BeautifulSoup(response_data, 'html.parser')
product_name = soup.find(name='span', class_="a-size-large product-title-word-break")
product_price = soup.find(name='span', class_="a-price-whole")

right_price = product_price.text.split('.')[0]
right_name = product_name.text.split(',',1)[0]

round_price = float(right_price.replace(',', ''))
target_price = round((float(round_price) /1.2),2)


if round_price < target_price:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=EMAIL_ID, password=EMAIL_PASSWORD)
    connection.sendmail(from_addr=EMAIL_ID,
                        to_addrs=EMAIL_ID,
                        msg=f'Subject: Price Decreased Alert \n\n The price you are looking for is live now!\n'
                            f'{right_name} is only for {right_price}')




