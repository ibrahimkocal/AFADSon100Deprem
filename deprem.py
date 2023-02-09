import requests
import json
from bs4 import BeautifulSoup

url = "https://deprem.afad.gov.tr/last-earthquakes.html"
html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

print(" AFAD Son Depremler(Son 100 Deprem) ".center(50, "*"))
print(" ")

list = soup.find("tbody").find_all("tr")
title = soup.find("thead").find_all("tr")

def kaydet(bilgi):
    with open ("son100deprem_bilgi.json","a", encoding= "utf-8") as file:
        json.dump(bilgi, file)
    with open ("son100deprem_bilgi.txt","a", encoding= "utf-8") as file:
        json.dump(bilgi, file)    

for th in title:
    tarih = th.find_all("th")[0].text.rjust(5)
    derinlik = th.find_all("th")[3].text.rjust(3)
    büyüklük = th.find_all("th")[5].text
    depremID = th.find_all("th")[7].text
    yer = th.find_all("th")[6].text
    print(tarih, derinlik, yer, büyüklük, depremID)

x = 1
for td in list:
    tarih = td.find_all("td")[0].text
    derinlik = td.find_all("td")[3].text
    büyüklük = td.find_all("td")[5].text
    depremID = td.find_all("td")[7].text
    yer = td.find_all("td")[6].text
    print(f"{x}- {tarih}, {derinlik}, {yer}, {büyüklük}, {depremID}")
    x += 1

    bilgi = {
    "tarih" : tarih,
    "derinlik": derinlik,
    "büyüklük": büyüklük,
    "depremID": depremID,
    "yer": yer
    }

    kaydet(bilgi)


