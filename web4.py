
import requests
import json
from bs4 import BeautifulSoup
from pprint import pprint

var=requests.get("https://www.flipkart.com/apple-iphone-11-red-64-gb/p/itmc3935326f2feb?pid=MOBFWQ6BYYV3FCU7&lid=LSTMOBFWQ6BYYV3FCU7JCCDZJ&marketplace=FLIPKART&q=iphone+11&store=tyy%2F4io&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&fm=SEARCH&iid=650b9660-6749-4250-85eb-b450a2efa3c8.MOBFWQ6BYYV3FCU7.SEARCH&ppt=sp&ppn=sp&ssid=2jch47tjog0000001622171948056&qH=f6cdfdaa9f3c23f3")
soup=BeautifulSoup(var.text,"html.parser")
# pprint(soup)


def scrap_link():
    dicti={}
    snap=soup.find("span",class_="B_NuCI").get_text()[:15]
    div=soup.find("div",class_="_3LWZlK").get_text()
    var=soup.find("div",class_="_30jeq3 _16Jk6d").get_text()[1:]
    rom=soup.find("li",class_="_21Ahn-").get_text()
    bank_off=soup.find("span",class_="_3j4Zjq row").get_text()
    colo=soup.find("span",class_="B_NuCI").get_text()[16:]
    dicti["company_name"]=snap
    dicti["star"]=div
    dicti["price"]=var
    dicti["ram"]=rom
    dicti["bank_offers"]=bank_off
    dicti["colour"]=colo
    with open("scrapping_link.json","w") as file:
        json.dump(dicti,file,indent=4)
scrap_link()

