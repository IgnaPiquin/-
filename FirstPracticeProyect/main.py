import sqlite3
import pandas as pd
from Categories import *  # Import Category-related classes
from Purchases import *    # Import Purchase-related classes
import re  # Regular expression module for input validation


# ---------- Functions -----------

# Function to add categories to the database
def add_category(name, description):
    # Establish a connection to the database
    with sqlite3.connect('FirstPracticeProyect.db') as connection:
        # Create a CategoryRepository instance with the connection
        repository = CategoryRepository(connection)

        # Create an AddCategory instance to add the new category
        add_category = AddCategory('Categories', repository,
                                   'CategoryName', 'CategoryDescription',
                                   name=name, description=description)
        # Call the method to add the category
        add_category.Add_Category()

# Function to add purchases to the database
def add_purchase(name, date, categoryID, price, quantity):
    # Establish a connection to the database
    with sqlite3.connect('FirstPracticeProyect.db') as connection:
        # Create an AddPurchasesRepository instance with the connection
        repository = AddPurchasesRepository(connection)

        # Create an AddPurchase instance to add the new purchase
        add_purchase = AddPurchase('Purchases', repository,
                                   'PurchaseDate', 'CategoryID', 'ProductName', 'ProductPrice', 'ProductQuantity',
                                   date=date, categoryID=categoryID, name=name, price=price, quantity=quantity)
        # Call the method to add the purchase
        add_purchase.Add_Purchase()

# Function to show expenses within a specified date range
def show_expenses(date1, date2):
    # Establish a connection to the database
    with sqlite3.connect('FirstPracticeProyect.db') as connection:
        # Create a ShowExpenses instance with the connection
        repository = ShowExpenses(connection)
        # Call the method to filter and display expenses
        repository.date_filter(date1, date2)


# -----------------Validations for the user--------------------
# Function to input the name for a new category, ensuring uniqueness
def category_name_input():
    # Prompt user for category name
    name_input = input('Input the name you want to use with the new category: ')
    query1 ='select CategoryName as Category from Categories'
    with sqlite3.connect('FirstPracticeProyect.db') as conn:
        categories = pd.read_sql_query(query1, conn)
        # Loop until a unique name is provided
        while name_input in categories['Category'].values:
            name_input = input('That category already exists, input the name you want to use with the new category: ')
        return name_input

# Function to input the purchase date, validating the format
def purchase_date_input():
    # Prompt user for purchase date
    date = input('Input the date in which you bought the product(YYYY-MM-DD): ')
    x = re.search(r'\d{4}/\d{2}/\d{2}', date)
    # Loop until a valid date format is provided
    while x:
        print('Remember to use the correct format for the date')
        date = input('Input the date in which you bought the product(YYYY-MM-DD): ')
        x = re.search(r'\d{4}/\d{2}/\d{2}', date)
    return date

# Function to input the purchase category, validating existence
def purchase_category_input():
    # Prompt user for purchase category
    category_input = input('Input the category of the product you bought:')
    with sqlite3.connect('FirstPracticeProyect.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT CategoryID 
                       FROM Categories 
                       WHERE CategoryName = ?''', (category_input,))
        categories = cursor.fetchone()
        categories = categories[0]
        return categories

# ---------- User Interaction -----------
# Prompt user for action
consult = input(f'''
                1 - Add Category
                2 - Add Purchase 
                3 - Show Expenses
                ''')
# Process user's choice
if consult == '1':
    name = category_name_input()
    description = input('Input the description you want to add to the new category: ')
    add_category(name, description)
elif consult == '2':
    name = input('Input the name of the product you bought: ')
    date = purchase_date_input()
    categoryID = purchase_category_input()
    price = input('Input the price of the product you bought: ')
    quantity = input('Input the quantity of the product you bought: ')
    add_purchase(name, date, categoryID, price, quantity)
elif consult == '3':
    date1 = input('Input the date from which you want to show the expenses')
    date2 = input('Input the date to which you want to show the expenses')
    show_expenses(date1, date2)
