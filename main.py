import requests
from bs4 import BeautifulSoup
import os
import smtplib

AMAZON_ENDPOINT = os.getenv("AMAZON_ENDPOINT")
EMAIL_ID = os.getenv("EMAIL_ID")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")



response = requests.get(AMAZON_ENDPOINT)
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




