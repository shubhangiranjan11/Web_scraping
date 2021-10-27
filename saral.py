from web1 import return_value
import requests
from bs4 import BeautifulSoup
import json

def scrape_movie_details(Url):
    dict = {}

    data1 = requests.get(Url)
    url_details = BeautifulSoup(data1.text,"html.parser")

    rank = url_details.find("span",class_= "AggregateRatingButton__RatingScore-sc-1il8omz-1 fhMjqK").get_text()
    dict["Rank"] = rank

    name = url_details.find("h1",class_= "TitleHeader__TitleText-sc-1wu6n3d-0 dxSWFG").get_text()
    dict["Name"] = name

    director = url_details.find("li",role_="presentation", class_= "ipc-metadata-list_item",testid_="title-pc-principal-credit").get_text()
    dict["Director"] = director

    run_time = url_details.find("div",class_="TitleBlock__TitleMetaDataContainer-sc-1nlhx7j-4 cgfrOx").get_text()[10:]
    dict["Time"] = run_time

    poster_img_url = url_details.find("a",class_="ipc-lockup-overlay ipc-focusable")["href"]
    dict["Poster_img_url"] = poster_img_url

    genre = url_details.find("div",class_="ipc-chip-list ipc-chip-list--wrap GenresAndPlot__GenresChipList-cum89p-6 fLrtBh").get_text()
    dict["Genre"] = genre

    maindiv = url_details.select("div[data-testid='title-details-section']")
    for key in maindiv:
        find_all_li = key.select("li[data-testid='title-details-languages']")
        for li_lan in find_all_li:
            lan = li_lan.find_all("li",class_="ipc-inline-list__item")
            lanuage = [d.get_text() for d in lan]
            dict["Language"] = lanuage
    
    subdiv = url_details.select("li[data-testid='title-details-origin']")
    for c in subdiv:
        find1_all_li = c.find_all("li",class_="ipc-inline-list__item")
        country = [d.get_text() for d in find1_all_li]
        dict["Country"] = country

    bio = url_details.find("div",class_="ipc-html-content ipc-html-content--base").get_text()
    dict["Bio"] = bio

    with open("saral_task4.json","w+") as file:
        json.dump(dict,file,indent=4)
        
    return dict

one_movie_details = scrape_movie_details("https://www.imdb.com/title/tt0048473/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=690bec67-3bd7-45a1-9ab4-4f274a72e602&pf_rd_r=GG2HC88ZEPEX4S4SN68T&pf_rd_s=center-4&pf_rd_t=60601&pf_rd_i=india.top-rated-indian-movies&ref_=fea_india_ss_toprated_tt_1")
print(one_movie_details)

# here we call the function if you want to see output then print otherwise not need to print