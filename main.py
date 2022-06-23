import requests
from bs4 import *
import smtplib

User_Agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36'
Accept_Language = 'en-US,en;q=0.9'
URL = 'url of product you would like to track'
header = {"User-Agent": User_Agent,
          "Accept-Language": Accept_Language
          }

response = requests.get(URL, headers=header)

soup = BeautifulSoup(response.content, 'lxml')
price = soup.find(id='sns-tiered-price').get_text()
price_num = float(price.split('$')[1])

title = soup.find(id="productTitle").get_text().strip()

BUY_PRICE = 10
Email = 'your email'
Psw = 'your password'
if price_num < BUY_PRICE:
    message = f"{title} is now {price_num}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(Email, Psw)
        connection.sendmail(
            from_addr=Email,
            to_addrs='',
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )
