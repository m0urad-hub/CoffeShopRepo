import json
import sqlite3
conn=sqlite3.connect("coffee_shop1.db")
cursor=conn.cursor()
def inject(cursor):
    with open("data.json","r") as file :
        data=json.load(file)
        print(data)
    for item in data :
        
        print(item[0])