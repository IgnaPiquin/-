import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from abc import ABC, abstractmethod


# Abstract class defining the chart comparator interface
class ChartComparator(ABC):
    @abstractmethod
    def compare(self, query):
        pass

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

class CategoriesChartMaker(ChartComparator):
    def __init__(self, data_provider):
        self.data_provider = data_provider
    
    def compare(self, query, date1, date2):
        # Prepare the query parameters
        parameters = (date1, date2)
        
        # Set Seaborn style
        plt.style.use('seaborn')
        
        # Fetch data from the database and create a DataFrame with specific columns
        expenses = pd.DataFrame(self.data_provider.execute_query(query, parameters),
                                columns=["Category", "Spent", "Date"])

        # Convert 'Date' column to datetime format
        expenses['Date'] = pd.to_datetime(expenses['Date'])
        
        # Generate a date range between date1 and date2
        date_range = pd.date_range(start=date1, end=date2, freq='D')
        
        # Create a new DataFrame with all combinations of dates and categories
        categories = expenses['Category'].unique()
        complete_data = []
        for category in categories:
            # Filter data for the current category
            category_data = expenses[expenses['Category'] == category].copy()
            # Set 'Date' as the index for easier manipulation
            category_data.set_index('Date', inplace=True)
            # Reindex the data to include the complete date range
            category_data = category_data.reindex(date_range, fill_value=0)
            # Add a 'Category' column to store the category name
            category_data['Category'] = category
            # Append the processed data to the list
            complete_data.append(category_data)

        # Combine all processed data into a single DataFrame (complete_data is a list so we want to convert it to a DataFrame)
        complete_df = pd.concat(complete_data)
        # Assingning a name to the index, to use it in the sns.lineplot
        complete_df = complete_df.rename_axis(index='Date')

        # Create a line plot using Seaborn
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=complete_df, x='Date', y='Spent', hue='Category')
        plt.title('Money Spent Over Time by Category')
        plt.xlabel('Date')
        plt.ylabel('Amount Spent')
        plt.show()

class MonthsChartMaker(ChartComparator):
    def __init__(self, data_provider):
        self.data_provider = data_provider
    
    def compare(self, query1, query2, month1, month2):
        # Set Seaborn style
        plt.style.use('seaborn')
        
        # Define date ranges for the two months
        month1_range1 = str(month1) + '-01'
        month1_range2 = str(month1) + '-31'
        month2_range1 = str(month2) + '-01'
        month2_range2 = str(month2) + '-31'
        date_range1 = pd.date_range(start=month1_range1, end=month1_range2, freq='D')
        date_range2 = pd.date_range(start=month2_range1, end=month2_range2, freq='D')
        
        # Fetch data from the database and create a DataFrame for month1
        month1_df = pd.DataFrame(self.data_provider.execute_query(query1, (month1, )), columns=["Date", "Spent"])
        
        # Fetch data from the database and create a DataFrame for month2
        month2_df = pd.DataFrame(self.data_provider.execute_query(query2, (month2, )), columns=["Date", "Spent"])

        # Convert 'Date' column to datetime format
        month1_df['Date'] = pd.to_datetime(month1_df['Date'])
        
        # Convert 'Date' column to datetime format
        month2_df['Date'] = pd.to_datetime(month2_df['Date'])
        
        # Set 'Date' column as the index for both DataFrames
        month1_df.set_index('Date', inplace=True)
        month2_df.set_index('Date', inplace=True)
       
        # Left join the full_date_range with expenses, filling NaN with 0
        month1_df = month1_df.reindex(date_range1, fill_value=0)
        month2_df = month2_df.reindex(date_range2, fill_value=0)
        
        # Rename the index to 'Date' for both DataFrames
        month1_df = month1_df.rename_axis(index='Date')
        month2_df = month2_df.rename_axis(index='Date')
        
        # Add 'Month' column to both DataFrames
        month1_df['Month'] = month1
        month2_df['Month'] = month2
        
        # Concatenate both DataFrames to create a single DataFrame for comparison
        comparation = pd.concat([month1_df, month2_df])
        
        # Extract the day part from the index and create a new 'Day' column
        comparation['Day'] = comparation.index.strftime('%d')
        
        # Create a line plot using Seaborn
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=comparation, x='Day', y='Spent', hue='Month')
        plt.title('Money Spent Over Time by Day for Two Months')
        plt.xlabel('Day')
        plt.ylabel('Amount Spent')
        plt.show()

class PersonalizedChartMaker(ChartComparator):
    def __init__(self, data_provider):
        self.data_provider = data_provider
    
    def compare(self, query1, query2, date1_sp, date1_ep, date2_sp, date2_ep):
        parameters1 = (date1_sp, date1_ep)
        parameters2 = (date2_sp, date2_ep)
        # Fetch data from the database and create a DataFrame for query1
        date1_df = pd.DataFrame(self.data_provider.execute_query(query1, parameters1), columns=["Date", "Spent"])
        
        # Fetch data from the database and create a DataFrame for query2
        date2_df = pd.DataFrame(self.data_provider.execute_query(query2, parameters2), columns=["Date", "Spent"])
        
        # Convert 'Date' column to datetime format
        date1_df['Date'] = pd.to_datetime(date1_df['Date'])
        
        # Convert 'Date' column to datetime format
        date2_df['Date'] = pd.to_datetime(date2_df['Date'])
        
        # Set 'Date' column as the index for both DataFrames
        date1_df.set_index('Date', inplace=True)
        date2_df.set_index('Date', inplace=True)
        
        date_range1 = pd.date_range(start=date1_sp, end=date1_ep, freq='D')
        date_range2 = pd.date_range(start=date2_sp, end=date2_ep, freq='D')
        
        # Left join the full_date_range with expenses, filling NaN with 0
        date1_df = date1_df.reindex(date_range1, fill_value=0)
        date2_df = date2_df.reindex(date_range2, fill_value=0)
        
        # Add 'Range' column to both DataFrames
        date1_df['Range'] = 1
        date2_df['Range'] = 2
        
        # Reset index, add auto-incremented column, and set index back to date on both DataFrames
        date1_df.reset_index(inplace=True)
        date1_df['Day'] = date1_df.index + 1
        date1_df.set_index('index', inplace=True)
        
        date2_df.reset_index(inplace=True)
        date2_df['Day'] = date1_df.index + 1
        date2_df.set_index('index', inplace=True)
        
        # Rename the index to 'Date' for both DataFrames
        month1_df = month1_df.rename_axis(index='Date')
        month2_df = month2_df.rename_axis(index='Date')
        
        
        # Concatenate both DataFrames to create a single DataFrame for comparison
        comparation = pd.concat([date1_df, date2_df])
        
        # Assingning a name to the index, to use it in the sns.lineplot
        comparation = comparation.rename_axis(index='Date')
        
        # Create a line plot using Seaborn
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=comparation, x='Day', y='Spent', hue='Range')
        plt.title('Money Spent Over Time by day with Personilized Ranges')
        plt.xlabel('Day')
        plt.ylabel('Amount Spent')
        plt.show()