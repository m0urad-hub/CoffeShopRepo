import sells
import inject_json_bd as inj
import sqlite3
import menu
import json
import coffe
conn=sqlite3.connect("coffee_shop1.db")
cursor=conn.cursor()
#menu.insert(conn,cursor)
#menu.affich(conn,cursor)
#inj.inject(conn,cursor)
#sells.insert()
while True :
    command=input("enter comand show_menu/insert_menu/add_sells/exit " )
    match command:
        case "show_menu":
            menu.affich(conn,cursor)
        case "insert_menu":
            menu.insert(conn,cursor)
        case "add_sells":
            sells.insert(conn,cursor)
            inj.inject(conn,cursor)
        case "exit":
            break
 
conn.close()   