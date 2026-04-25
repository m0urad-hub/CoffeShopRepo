import json
import sqlite3

def inject(conn,cursor):
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
        
        for item in data:

            try:
                cursor.execute("""
                    INSERT INTO sells (name_product, price, unit, time, category) 
                    VALUES (?, ?, ?, ?, ?)
                """, (item["name"], item["price"], "TND", item["time"], item["category"]))
            except sqlite3.Error as e:
                print(f"Error inserting {item.get('name')}: {e}")

        conn.commit()
        print("Data injected successfully!")

    except FileNotFoundError:
        print("Error: The file 'data.json' was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. Check your file format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
