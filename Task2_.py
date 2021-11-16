import json

def scrape_top_list() :

    task1_file=open("web_task1.json","r") 
    task1_data=json.load(task1_file)
    # print(task1_data)

    list1=[]
    dic={}
    for a in task1_data:
        if int(a["year"]) not in dic:
            list1.append(int(a["year"]))
    # print(list1)

    list1.sort()
    # print(list1)

    for b in list1: 
        store_data=[]
        for c in task1_data:
            if b==int(c["year"]) :
                store_data.append(c)
        dic[b]=store_data
    return dic
    # print(store_data)
data=scrape_top_list() 

file2=open("web_task2.json","w")
file_data=json.dump(data,file2,indent=5)

