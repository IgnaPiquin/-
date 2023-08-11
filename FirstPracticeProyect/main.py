import sqlite3
import pandas as pd
from Categories import *
from Purchases import *
import re
# ---------- Functions -----------

# Function to add categories to the database
def add_category(name, description):
    with sqlite3.connect('FirstPracticeProyect.db') as connection:
        repository = CategoryRepository(connection)

        add_category = AddCategory('Categories', repository, 'CategoryName', 'CategoryDescription', name=name, description=description)
        add_category.Add_Category()

#Function to add purchases to the database
def add_purchase(purchase, values):
    with sqlite3.connect('FirstPracticeProyect.db') as connection:
        repository = PurchasesRepository(connection)

        add_purchase = AddPurchase(purchase, values, repository)
        add_purchase.Add_Purchase()


# -----------------Validations for the user--------------------
def category_name_input():
    name_input = input('Input the name you want to use with the new category: ')
    

def purchase_date_input():
    date = input('Input the date in which you bought the product(YYYY-MM-DD): ')
    x = re.search(r'\d{4}/\d{2}/\d{2}', date)
    while x:
        print('Remember to use the correct format for the date')
        date = input('Input the date in which you bought the product(YYYY-MM-DD): ')
        x = re.search(r'\d{4}/\d{2}/\d{2}', date)
    return date

def purchase_category_input():
    category_input = input('Input the category')

query1 ='select CategoryName as Category from Categories'
with sqlite3.connect('FirstPracticeProyect.db') as conn:
    # Obteniendo los 10 productos con mas Revenue
        
    top_product = pd.read_sql_query(query1, conn)
    print(top_product)
# ---------- User Interaction -----------
consult = input(f'''
                1 - Add Category
                2 - Add Purchase 
                
                ''')
if consult == '1':
    name = input('Input the name you want to use with the new category: ')
    description = input('Input the description you want to add to the new category: ')
    add_category(name, description)
elif consult == '2':
    values = PurchaseTF('Purchases', 'PurchaseDate', 'CategoryID', 'ProductName', 'ProductPrice', 'ProductQuantity')
    purchase = PurchaseValues
    purchase.name = input('Input the name of the product you bought: ')
    purchase.date = purchase_date_input()
    purchase.categoryID = input('Input the category of the product you bought: ')
    purchase.price = input('Input the price of the product you bought: ')
    purchase.quantity = input('Input the quantity of the product you bought: ')
    add_purchase(purchase, values)
