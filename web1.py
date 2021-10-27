import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

rest=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
soup=BeautifulSoup(rest.text,"html.parser")
print(soup)

def scrap_top_list():
    div = soup.find("div",class_="lister")
    table = div.find("tbody",class_="lister-list")
    tr = table.find_all("tr")

    movie_name = []
    movie_year = []
    movie_rank = []
    movie_url = []
    movie_rating = []
    for i in tr:
        details=i.find("td",class_="titleColumn").get_text()
        rank = " "
        index = 0
        while index < len(details):
            if "." not in details[index] :
                rank = rank+details[index]

            else:
                break
            index+=1
        movie_rank.append(rank)


        name = i.find("td",class_="titleColumn").a.get_text()
        movie_name.append(name)

        year = i.find("td",class_="titleColumn").span.get_text()
        movie_year.append(year)
        
        
        rating = i.find("td",class_="ratingColumn imdbRating").strong.get_text()
        movie_rating.append(rating)

        url = i.find("td",class_="titleColumn").a["href"]
        url_add = "https://www.imdb.com"+url
        movie_url.append(url_add)

    movie_list = []
    movie_dict = {"rank":" ","name":" ","year":" ","rating":" ","url":" "}
    counter = 0
    while counter<len(movie_rank):
        movie_dict["name"] = movie_name[counter]

        movie_dict["rank"] = int(movie_rank[counter])

        movie_dict["year"] = int(movie_year[counter][1:5])

        movie_dict["url"] = movie_url[counter]

        movie_dict["rating"] = float(movie_rating[counter])

        movie_list.append(movie_dict.copy())
        
        counter = counter+1

    with open("task1.json","w") as movie_data:
        json.dump(movie_list,movie_data,indent=4)
    return (movie_list)
# var=scrap_top_list()
# pprint(var)

return_value=scrap_top_list()
pprint(return_value)