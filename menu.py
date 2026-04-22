
def insert(conn,cursor):
    run=1
    while run :
        
        name=input("enter the name of the product : ")
        price=float(input("enter the pric e of the product : "))
        categ=input("type of product drink/food ? : ")
        cursor.execute("insert into products (name,price,category) values(?,?,?)",(name,price,categ))
        loop = input ("wanna add another product yes/no ?")
        if loop == "no":
            run=False 
    conn.commit()
def affich(conn,cursor):
    cursor.execute("select* from products")
    data=cursor.fetchall()
    for item in data :
        print (f"|| name :{item[1]} || price :{item[2]} || category :{item[3]} ||\n")