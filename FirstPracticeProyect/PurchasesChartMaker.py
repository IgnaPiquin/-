import matplotlib.pyplot as plt
import pandas as pd

class ChartDataProvider:
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

class ExpensesChartMaker:
    def __init__(self, data_provider):
        self.data_provider = data_provider
    
    def create_chart(self, query, date1, date2, show_no_purchase_days):
        parameters = (date1, date2)
        plt.style.use('seaborn')
        expenses = pd.DataFrame(self.data_provider.execute_query(query, parameters), columns=["Date", "Spent"])
        
        if show_no_purchase_days:
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

