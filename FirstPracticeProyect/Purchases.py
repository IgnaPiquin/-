from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

class AdDataAccess(ABC):
    @abstractmethod
    def add(self, table, fields, values, values_amount):
        pass

class FilterDataAccess(ABC):
    @abstractmethod
    def Filter(self, table, fields, date1, date2):
        pass
    
    
class AddPurchasesRepository(AdDataAccess):
    def __init__(self, connection):
        self.connection = connection
    #Using the objects purchase, which has the name and fields of the table, and values, which has the values that are going to be stored in the database
    def add(self, table, fields, values, values_amount):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(f'''
                            INSERT INTO {table} ({fields}) 
                            VALUES ({values_amount})
                            ''', values)

class AddPurchase:
    def __init__(self, table, repository, *args, **kwargs):
        self.table = table
        # The repository is the object that contains the conection to the database which was created using the CategoryRepository class.
        self.repository = repository
        #args are the fields of the table and kwargs are the values that the user wants to use to create the new category.
        self.field_names = args
        self.field_values = kwargs
    
    def Add_Purchase(self):
        # Unpack *args into field names and **kwargs into field values
        fields = ', '.join(self.field_names)
        values = tuple(self.field_values.values())
        values_amount= ', '.join(['?' for _ in self.field_values])
        
        # fields is a string with the fields to use in the query, values is a tuple with the values that the user wants to use to create the new category, and values_amount is a string with the amount of placeholder we need to match the amount of values
        self.repository.add(self.table, fields, values, values_amount)

class ShowExpenses():
    def __init__(self, connection):
        self.connection = connection
    #Using the objects purchase, which has the name and fields of the table, and values, which has the values that are going to be stored in the database
    def date_filter(self, date1, date2):
            query = f'''
            SELECT PurchaseDate as Date, SUM(ProductPrice * ProductQuantity) as Spent
            FROM Purchases 
            WHERE PurchaseDate BETWEEN "{date1}" AND "{date2}"
            GROUP BY PurchaseDate
            ORDER BY PurchaseDate
            '''
            with sqlite3.connect('FirstPracticeProyect.db') as conn:
                plt.style.use('seaborn')
                expenses = pd.read_sql_query(query, conn)
                s = input("Do you want to show the days in which you didnt purchase anything?(yes/no)")
                if s == "yes":
                    # Convert 'Date' column to datetime and set it as the index
                    expenses['Date'] = pd.to_datetime(expenses['Date'])
                    expenses.set_index('Date', inplace=True)

                    # Generate a date range between date1 and date2
                    full_date_range = pd.date_range(start=date1, end=date2, freq='D')

                    # Left join the full_date_range with expenses, filling NaN with 0
                    expenses = expenses.reindex(full_date_range, fill_value=0)
                else:
                    expenses.set_index('Date', inplace=True)
                expenses.plot(figsize=(10,8), fontsize=12)
                plt.xlabel('Date')
                plt.ylabel('Amount Spent')
                plt.legend(fontsize=12)
                plt.subplots_adjust(bottom=0.3, top=1)
                plt.show()