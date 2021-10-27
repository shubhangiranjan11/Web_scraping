import json
from pprint import pprint

file=open("task2.json","r")
movies=json.load(file)



def group_by_decade():
    decade_year=[]
    moviedec={}
    for index in movies:
        ye=index
        mod=int(ye)%10       
        dic=int(ye)-mod  
        if dic not in decade_year:      
            decade_year.append(dic)
    decade_year.sort()
    # print(decade_year)

    movie_dict={}
    index=0
    while index<len(decade_year): 
        min=decade_year[index]+10
        print(min)
        l=[]
        for x in movies:
            if int(x)>=decade_year[index] and int(x)<=min:
                l.append(movies[x])
                movie_dict[decade_year[index]]=l
        index+=1
    with open("task3.json","w")as json_data:
        json.dump(movie_dict,json_data,indent=4)
        
        return moviedec
group_by_decade()





