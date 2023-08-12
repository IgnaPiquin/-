import sqlite3
import pandas as pd
from AddRows import Repository, Add  # Import Category-related classes
from PurchasesChartMaker import ChartDataProvider, ExpensesChartMaker
from PurchasesAmountComparator import DataProvider, AmountComparator
import re  # Regular expression module for input validation


# ---------------------- Functions ---------------------------

# ---- Adding functions ----

# Function to add categories to the database
def add_category(name, description):
    # Establish a connection to the database
    with sqlite3.connect('FirstPracticeProyect.db') as connection:
        # Create a CategoryRepository instance with the connection
        repository = Repository(connection)

        # Create an AddCategory instance to add the new category
        add_category = Add('Categories', repository, 
                                   'CategoryName', 'CategoryDescription',
                                   name=name, description=description)
        # Call the method to add the category
        add_category.execute()

# Function to add purchases to the database
def add_purchase(name, date, categoryID, price, quantity):
    # Establish a connection to the database
    with sqlite3.connect('FirstPracticeProyect.db') as connection:
        # Create an AddPurchasesRepository instance with the connection
        repository = Repository(connection)

        # Create an AddPurchase instance to add the new purchase
        add_purchase = Add('Purchases', repository,
                                   'PurchaseDate', 'CategoryID', 'ProductName', 'ProductPrice', 'ProductQuantity',
                                   date=date, categoryID=categoryID, name=name, price=price, quantity=quantity)
        # Call the method to add the purchase
        add_purchase.execute()
        
        
# ---- Chart functions ----


# Function to show expenses in a chart within a specified date range
def show_expenses(date1, date2, show_no_purchase_days):
    with sqlite3.connect('FirstPracticeProyect.db') as connection:
        data_provider = ChartDataProvider(connection)
        expenses_chart_maker = ExpensesChartMaker(data_provider)

        query = '''
                SELECT PurchaseDate as Date, SUM(ProductPrice * ProductQuantity) as Spent
                FROM Purchases 
                WHERE PurchaseDate BETWEEN ? AND ?
                GROUP BY PurchaseDate
                ORDER BY PurchaseDate
                '''

        expenses_chart_maker.create_chart(query, date1, date2, show_no_purchase_days)


# ---- Amount functions ----

# Function to compare prices between all the categories
def compare_categories_amount(date1, date2):
    with sqlite3.connect('FirstPracticeProyect.db') as connection:
        data_provider = DataProvider(connection)
        categories_coparator = AmountComparator(data_provider)

        query = '''
                SELECT CategoryName as Category, SUM(ProductPrice * ProductQuantity) as Spent
                FROM Purchases p
                JOIN Categories c ON c.CategoryID = p.CategoryID                
                WHERE PurchaseDate BETWEEN ? AND ?
                GROUP BY Category
                ORDER BY Spent
                '''
        type = 'Categories'
        print(categories_coparator.compare(query, date1, date2, type))

def compare_months_amount(month1, month2):
    with sqlite3.connect('FirstPracticeProyect.db') as connection:
        data_provider = DataProvider(connection)
        categories_comparator = AmountComparator(data_provider)

        query = '''
                SELECT SUBSTR( PurchaseDate, 1, 7) as Months, SUM(ProductPrice * ProductQuantity) as Spent
                FROM Purchases              
                WHERE Months BETWEEN ? AND ?
                GROUP BY Months
                ORDER BY Months
                '''
        type = 'Months'
        print(categories_comparator.compare(query, month1, month2, type))

def compare_years_amount(year1, year2):
    with sqlite3.connect('FirstPracticeProyect.db') as connection:
        data_provider = DataProvider(connection)
        categories_comparator = AmountComparator(data_provider)

        query = '''
                SELECT SUBSTR( PurchaseDate, 1, 4) as Years, SUM(ProductPrice * ProductQuantity) as Spent
                FROM Purchases              
                WHERE Years BETWEEN ? AND ?
                GROUP BY Years
                ORDER BY Years
                '''
        type = 'Years'
        print(categories_comparator.compare(query, year1, year2, type))

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

def compare_expenses_amount():
    consult2 = input('''
                     1 - All Categories
                     2 - Months
                     3 - Years
                     4 - Peronalized
                     ''')
    if consult2 == '1':
        date1 = input('Input the date from which you want to show the expenses: ')
        date2 = input('Input the date to which you want to show the expenses: ')
        compare_categories_amount(date1, date2)
    if consult2 == '2':
        month1 = input('Input  the month from which you want to show the expenses: ')
        month2 = input('Input the month to which you want to show the expenses: ')
        compare_months_amount(month1, month2)
    if consult2 == '3':
        year1 = input('Input  the month from which you want to show the expenses: ')
        year2 = input('Input the month to which you want to show the expenses: ')
        compare_years_amount(year1, year2)

consult = input(f'''
                1 - Add Category
                2 - Add Purchase 
                3 - Show Expenses
                4 - Compare Expenses by amount
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
    date1 = input('Input the date from which you want to show the expenses: ')
    date2 = input('Input the date to which you want to show the expenses: ')
    show_no_purchase_days = input("Do you want to show the days in which you didn't purchase anything?(yes/no): ")
    show_expenses(date1, date2, show_no_purchase_days)
elif consult == '4':
    compare_expenses_amount()


