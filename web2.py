from web1 import return_value
from pprint import pprint
import json

def group_by_year(movies):
    years=[]
    dict1={}
    for i in movies:
        year=[]
        for j in movies:
            if i["year"] == j["year"]:
                year.append(i)
                # pprint(year)
                dict1[i["year"]]=year
                # pprint(dict1)
    # b=year.sort()
    # pprint(b)
    with open("task2.json","w+") as file:
        json.dump(dict1,file,indent=4)
        return dict1

Year_=group_by_year(movies=return_value)
