
import requests
import json
from bs4 import BeautifulSoup
from pprint import pprint


var2=requests.get("https://www.flipkart.com/redmi-note-10-pro-glacial-blue-128-gb/p/itm04ba1f0aed358?pid=MOBGFDFYE7TFYZKV&lid=LSTMOBGFDFYE7TFYZKVFRRVV9&marketplace=FLIPKART&q=redmi+note+10+pro&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_2_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_3_na_na_na&fm=SEARCH&iid=12360908-c2a3-41d5-b559-fb350dda2840.MOBGFDFYE7TFYZKV.SEARCH&ppt=hp&ppn=homepage&ssid=ng4okjejdc0000001623152160795&qH=20ef7d326dcad8f3")
soup=BeautifulSoup(var2.text,"html.parser")
pprint(soup)

def scrape_data():
    dict1={}
    cavr=soup.find("span",class_="B_NuCI").get_text()[:-34]
    rati=soup.find("div",class_="_3LWZlK").get_text()
    pri=soup.find("div",class_="_30jeq3 _16Jk6d").get_text()[1:]
    colo=soup.find("span",class_="B_NuCI").get_text()[18:][:-15]
    rom=soup.find("span",class_="B_NuCI").get_text()[42:]
    gene=soup.find("li",class_="_21lJbe").get_text()
    snap=soup.find("span",class_="_3j4Zjq").get_text()
    stor=soup.find("span",class_="B_NuCI").get_text()[33:][:-13]
    high=soup.find("div",class_="_2cM9lP").get_text()[25:][:-40]
    came=soup.find("div",class_="_2cM9lP").get_text()[52:][:-16]
    batt=soup.find("div",class_="_2cM9lP").get_text()[75:]
    dict1["company_name"]=cavr
    dict1["ratings"]=rati
    dict1["price"]=pri
    dict1["color"]=colo
    dict1["ram"]=rom
    dict1["general"]=gene
    dict1["bank_offers"]=snap
    dict1["storage"]=stor
    dict1["size"]=high
    dict1["camera"]=came
    dict1["battrey"]=batt
    with open("scrapping_data.json","w") as file2:
        json.dump(dict1,file2,indent=4)
scrape_data()

