from abc import ABC, abstractmethod

class IDataAccess(ABC):
    @abstractmethod
    def add(self, table, field1, field2, name, description):
        pass

class CategoryRepository(IDataAccess):
    def __init__(self, connection):
        self.connection = connection

    def add(self, table, field1, field2, name, description):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(f'''
                            INSERT INTO {table} ({field1}, {field2}) 
                            VALUES ('{name}', '{description}')
                            ''')

class AddCategory:
    def __init__(self, table, field1, field2, name, description, repository):
        self.table = table
        self.field1 = field1
        self.field2 = field2
        self.name = name
        self.description = description
        self.repository = repository
    
    def Add_Category(self):
        self.repository.add(self.table, self.field1, self.field2, self.name, self.description)

