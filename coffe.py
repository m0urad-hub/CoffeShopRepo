import sqlite3
def initialize_database():
    # Connect to the database (creates file 'coffee_shop.db' if it doesn't exist)
    conn = sqlite3.connect('coffee_shop1.db')
    cursor = conn.cursor()

    # 1. Create Products Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products(
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            category TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sells (
            id_sells INTEGER PRIMARY KEY AUTOINCREMENT,
            name_product TEXT NOT NULL,
            price REAL NOT NULL,
            unit TEXT,
            time TEXT,
            category TEXT
        )
    ''')


    print("Database and tables created successfully!")
    
    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()