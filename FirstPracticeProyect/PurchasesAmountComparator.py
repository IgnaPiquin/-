import matplotlib.pyplot as plt
import pandas as pd

class DataProvider:
    def __init__(self, connection):
        self.connection = connection
    
    def execute_query(self, query, parameters=None):
        with self.connection:
            cursor = self.connection.cursor()
            if parameters is None:
                cursor.execute(query)
            else:
                cursor.execute(query, parameters)
            return cursor.fetchall()

class AmountComparator():
    def __init__(self, data_provider):
        self.data_provider = data_provider
    
    def compare(self, query, date1, date2, type):
        parameters = (date1, date2)
        expenses = pd.DataFrame(self.data_provider.execute_query(query, parameters), columns=[type, "Spent"])
        expenses = expenses.to_string(index=False)
        return (expenses)
    