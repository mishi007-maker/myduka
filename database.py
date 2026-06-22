import psycopg2

# establishing a connection to a postgres database
conn=psycopg2.connect(host="localhost",port="5432",user="postgres",password="warigia",dbname="myduka")
cur=conn.cursor()
# cur object

def get_products():
    cur.execute("select * from products")
    products_data= cur.fetchall()
    return products_data

def get_sales():
    cur.execute("select * from sales")
    sales_data= cur.fetchall()
    return sales_data


# method 1:
def insert_products(values):
    cur.execute(f"insert into products(name,buying_price,selling_price)values{values}")
    conn.commit()

product1=('Lenovo laptop',45000,55000)
product2=('Infinix',25000,32000)

# insert_products(product1)
# insert_products(product2)

# method 2:
# def insert_products2(values):
#     cur.execute("insert into products(name,buying_price,selling_price)values(%s,%s,%s)" ,values)
#     conn.commit()

# product3=('Tecno',23000,30000)
# insert_products2(product3)

# products_data=get_products()
# print(products_data)

def get_stock():
    cur.execute("select * from stock")
    stock_data=cur.fetchall()
    return stock_data

def insert_sales(values):
    cur.execute("insert into sales(pid,quantity)values(%s,%s)" ,values)
    conn.commit()

sale3=(3,10)
sale4=(4,26)
sale5=(5,32)

# insert_sales(sale3)
# insert_sales(sale4)
# insert_sales(sale5)


sales_data = get_sales()
print(sales_data)


def insert_stock(values):
    cur.execute("insert into stock(pid,stock_quantity)values(%s,%s)" ,values)
    conn.commit()

stock1=(1,12)
stock2=(2,17)
stock3=(3,18)

# insert_stock(stock1)
# insert_stock(stock2)
# insert_stock(stock3)

stock_data = get_stock()
print(stock_data)

def sales_per_day():
    cur.execute("""
    select date(sales.created_at) as date, sum(sales.quantity * products.selling_price)
     as total_sales from sales join products on products.id = sales.pid group by date;
    """)
    daily_sales=cur.fetchall()
    return daily_sales

def profit_per_day():
    cur.execute("""
   select date(sales.created_at) as date, sum(sales.quantity *( products.selling_price - products.buying_price)) 
    as total_sales from sales join products on products.id = sales.pid group by date;
    """)
    daily_profit=cur.fetchall()
    return daily_profit

def sales_per_product():
    cur.execute("""
    select products.name as p_name , sum(sales.quantity * products.selling_price) as total_sales 
    from products join sales on sales.pid = products.id group by p_name;
    """)
    product_sales=cur.fetchall()
    return product_sales

def  profit_per_product():
    cur.execute("""
    select products.name as p_name , sum(sales.quantity *( products.selling_price - products.buying_price)) 
    as total_sales from products join sales on sales.pid = products.id group by p_name;
    """)
    product_profit=cur.fetchall()
    return product_profit

def check_available_stock(pid):
    cur.execute("select sum(stock.stock_quantity) from stock where pid = %s",(pid,))
    total_stock=cur.fetchone()[0] or 0

    cur.execute("select sum(sales.quantity) from sales where pid=%s",(pid,))
    total_sold=cur.fetchone()[0] or 0

    return total_stock - total_sold

def check_user_exists(email):
    cur.execute("select * from users where email = %s", (email,))
    user=cur.fetchone()
    return user

# existing_user=check_user_exists('mitch@gmail.com')
# print(existing_user)




def create_user(user_details):
    cur.execute("insert into users(full_name,email,phone_number,password) values (%s,%s,%s,%s)", user_details)
    conn.commit()

