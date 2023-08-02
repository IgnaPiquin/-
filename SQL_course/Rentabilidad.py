import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Obteniendo los 10 productos mas rentables
query1 = '''
    SELECT ProductName, SUM(Price * Quantity) as Revenue
    FROM OrderDetails od
    JOIN Products p ON p.ProductID = od.ProductID
    GROUP BY od.ProductID
    ORDER BY Revenue DESC
    LIMIT 10
'''

# Obteniendo los 10 empleados con mas ventas
query2 = '''
    SELECT FirstName || ' ' || LastName as Employee, COUNT(*) as Total
    FROM Orders o
    JOIN Employees e ON e.EmployeeID = o.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY Total DESC
    LIMIT 10
'''
# Obteniendo los 10 empleados con mayor ganancia
query3= '''
    SELECT FirstName || ' ' || LastName as Employee,
    SUM(Price * Quantity) as Total
    
    FROM OrderDetails od
    JOIN Products p ON p.ProductID = od.ProductID
    JOIN Orders o ON o.OrderID = od.OrderID
    JOIN Employees e ON e.EmployeeID = o.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY Total DESC
    LIMIT 10
'''


with sqlite3.connect('Northwind.db') as conn:
    # Obteniendo los 10 productos con mas Revenue
        
    top_product = pd.read_sql_query(query1, conn)
    top_product.plot(x='ProductName', y='Revenue', kind='bar', figsize=(10, 5), legend=False)

    plt.title('10 productos mas rentables')
    plt.xlabel('Productos')
    plt.ylabel('Revenue')
    plt.xticks(rotation=90)
    plt.subplots_adjust(bottom=0.3)
    plt.show()

    # Obteniendo los 10 empleados mas efectivos
    top_employee = pd.read_sql_query(query2, conn)
    top_employee.plot(x='Employee', y='Total', kind='bar', figsize=(10, 5), legend=False)

    plt.title('10 empleados con mas ventas')
    plt.xlabel('Empleados')
    plt.ylabel('Cantidad total Vendida')
    plt.xticks(rotation=45)
    plt.subplots_adjust(bottom=0.3)
    plt.show()
    
    # Obteniendo los 10 empleados con mayor Revenue
    top_employee = pd.read_sql_query(query3, conn)
    top_employee.plot(x='Employee', y='Total', kind='bar', figsize=(10, 5), legend=False)

    plt.title('10 empleados con mayor Revenue')
    plt.xlabel('Empleados')
    plt.ylabel('Revenue')
    plt.xticks(rotation=45)
    plt.subplots_adjust(bottom=0.3)
    plt.show()