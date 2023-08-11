from abc import ABC, abstractmethod


# Abstract class defining the data access interface
class IDataAccess(ABC):
    @abstractmethod
    def add(self, table, fields, values, values_amount):
        pass

# Concrete class implementing the IDataAccess interface
class CategoryRepository(IDataAccess):
    def __init__(self, connection):
        self.connection = connection

    def add(self, table, fields, values, values_amount):
        # Use connection as a context manager to ensure proper resource handling
        with self.connection:
            cursor = self.connection.cursor()
            # Execute SQL query to insert data into the specified table
            cursor.execute(f'''
                            INSERT INTO {table} ({fields}) 
                            VALUES ({values_amount})
                            ''', values)


class AddCategory:
    def __init__(self, table, repository, *args, **kwargs):
        self.table = table
        # The repository is the object that contains the conection to the database which was created using the CategoryRepository class.
        self.repository = repository
        #args are the fields of the table and kwargs are the values that the user wants to use to create the new category.
        self.field_names = args
        self.field_values = kwargs
    
    def Add_Category(self):
        # Unpack *args into field names and **kwargs into field values
        fields = ', '.join(self.field_names)
        values = tuple(self.field_values.values())
        values_amount= ', '.join(['?' for _ in self.field_values])
        
        # fields is a string with the fields to use in the query, values is a tuple with the values that the user wants to use to create the new category, and values_amount is a string with the amount of placeholder we need to match the amount of values
        self.repository.add(self.table, fields, values, values_amount)