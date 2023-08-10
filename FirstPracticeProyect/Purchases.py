from abc import ABC, abstractmethod
import sqlite3
class IDataAccess(ABC):
    @abstractmethod
    def add(self, table, field1, field2, name, description):
        pass

class PurchasesRepository(IDataAccess):
    def __init__(self, connection):
        self.connection = connection
    #Using the objects purchase, which has the name and fields of the table, and values, which has the values that are going to be stored in the database
    def add(self, purchase, values):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(f'''
                            INSERT INTO {purchase.table} 
                            ({purchase.field1}, {purchase.field2}, {purchase.field3}, {purchase.field4}, {purchase.field5}) 
                            VALUES ('{values.date}', '{values.categoryID}', '{values.name}', '{values.price}', '{values.quantity}')
                            ''')

class AddPurchase:
    def __init__(self, purchase, values, repository):
        self.purchase = purchase
        self.values = values
        self.repository = repository
    
    def Add_Purchase(self):
        self.repository.add(self.purchase, self.values)



# Purchase Table and Fields
class PurchaseTF:
    def __init__(self, table, field1, field2, field3,field4,field5):
        self.table = table
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3
        self.field4 = field4
        self.field5 = field5

# Values of the product which the client bought
class PurchaseValues:
    def __init__(self, name, date, categoryID, price, quantity):
        self.name = name
        self.date = date
        self.categoryID = categoryID
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        return '- Name: {self.name}, \n-Date: {self.date}, \n-Category: {self.category}, \n-Price: {self.price}, n\-Quantity:{self.quantity}'

# values = PurchaseValues('Water', '08-10-2023', 10, 20, 5)
# purchase = PurchaseTF('Purchases', 'PurchaseDate', 'CategoryID', 'ProductName', 'ProductPrice', 'ProductQuantity')
# with sqlite3.connect('FirstPracticeProyect.db') as connection:
#     repository = PurchasesRepository(connection)

#     add_purchase = AddPurchase(purchase, values, repository)
#     add_purchase.Add_Purchase()