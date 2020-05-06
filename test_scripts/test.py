import requests
import time
import sha3
import binascii
from bs4 import BeautifulSoup
from ecdsa import SigningKey, SECP256k1
url = ("https://etherscan.io/address/84A0d77c693aDAbE0ebc48F88b3fFFF010577051")
html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
soup = BeautifulSoup(html, "html.parser")
table = soup.find("div", {"class": "col-md-8"})
value = table.text.split(' ')[0].strip()
amount =float(value)
print (str(amount))