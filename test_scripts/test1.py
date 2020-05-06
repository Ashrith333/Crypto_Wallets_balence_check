# python -m pip install --upgrade pip
# C:\Users\ashri\AppData\Local\Programs\Python\Python38-32\Scripts
#pip install ecdsa/pysha3/bs4/requests
import requests
import time
import sha3
import binascii
from bs4 import BeautifulSoup
from ecdsa import SigningKey, SECP256k1
start = time.time()
i = 1
while (i>0):

    t_time=time.time() - start
    keccak = sha3.keccak_256()
    priv = SigningKey.generate(curve=SECP256k1)
    pub =  priv.get_verifying_key().to_string()
    keccak.update(pub)
    address = keccak.hexdigest()[24:]
    z = str( binascii.hexlify(priv.to_string()), 'utf-8')
    print (str(i) + " " + "private key "+ z + " " + "address = 0x"+address+ " ")
    url = ("https://etherscan.io/address/%s"%address)
    html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("div", {"class": "col-md-8"})
    value = table.text.split(' ')[0].strip()
    
    table1 = soup.find("span", {"class": "badge badge-primary mx-1"})
    if table1 != None:
        value1 =10
    else:
        value1= 0 
    amount =float(value)+value1
    print(amount)
    file1 = open("ETH-PRV-ADD-VAL.txt", "a")
    file1.write(str(i)+" "+"Priv_Adr = "+z+" "+"Add = 0x"+address+ " "+str(amount)+ "\n")
    if amount > 0 :
        print ("_______________________________")
        print ("          FOUND                ")
        print ("private key        = "+z)
        print ("address            =0x"+address)
        print ("eth amount         = "+str(amount))
        file2 = open("FOUND.txt", "a")
        file2.write(str(i)+" "+"Priv_Adr = "+z+" "+"Add = 0x"+address+ " "+str(amount)+ "\n")
        file2.close()
    i=i+1
    time.sleep(0.0)

file1.close()
print (t_time)