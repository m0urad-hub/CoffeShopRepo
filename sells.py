import json
import sqlite3
import os

conn = sqlite3.connect("coffee_shop1.db")
cursor = conn.cursor()
import datetime 
def insert(): # Added ()
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            try:
                data = json.load(f)
            except:
                data = []
    else:
        data = []

    while True:
        name = input("Enter product name (or 'quit' to save): ")
        if name.lower() == 'quit':
            break
        date=datetime.datetime.now().strftime("%Y-%m-%d")    
        cursor.execute("SELECT price, category FROM products WHERE name = ?", (name,))
        product = cursor.fetchone() 
        
        if product:
            price = product[0]
            category = product[1]
            
            
            data.append({
                "name": name,
                "price": price,
                "unit": "TND",
                "category": category,
                "time":date 
            })
            print(f"Added {name} to the list.")
        else:
            print("Product not found in database!")

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Data saved successfully!")
