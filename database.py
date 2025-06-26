import psycopg2


conn = psycopg2.connect(
    dbname ="DFCCIL",
    username ="postgres",
    password = "Tejpal@123",
    host = 'localhost',
    port = 5432
)

cur = conn.cursor()

create_query = '''create table po_data(
    VendorName varchar(100),
    ProductName varchar(256), orderQuantity varchar(100),
    unitPrice varchar(100),date datetime 
    )'''
cur.execute(create_query)
conn.commit()






