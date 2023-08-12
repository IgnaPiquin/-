from abc import ABC, abstractmethod
import sqlite3
import pandas as pd
# Abstract class defining the data access interface
class IDataAccess(ABC):
    @abstractmethod
    def add(self, table, fields, values, values_amount):
        pass

# Concrete class implementing the IDataAccess interface
class CategoryRepository(IDataAccess):
    def __init__(self, connection):
        self.connection = connection

    def add(self, query):
        # Use connection as a context manager to ensure proper resource handling
        with self.connection:
            cursor = self.connection.cursor()
            # Execute SQL query to insert data into the specified table
            cursor.execute(query)
    def return_value(self, query):
        with self.connection:
            cursor = self.connection.cursor()
            # Execute SQL query to insert data into the specified table
            cursor.execute(query)
            categories = cursor.fetchall()
            return categories
            




query = '''SELECT * 
        FROM ?''', 'Categories'


# Establish a connection to the database
with sqlite3.connect('FirstPracticeProyect.db') as connection:
    # Create a CategoryRepository instance with the connection
    repository = CategoryRepository(connection)
    data=repository.return_value(query)
    print(data)
    data = pd.DataFrame(data)
    print (data)
    