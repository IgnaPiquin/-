import sqlite3
import pandas as pd
from Categories import *


def add_category(name, description):
    with sqlite3.connect('FirstPracticeProyect.db') as connection:
        repository = CategoryRepository(connection)

        add_category = AddCategory('Categories', 'CategoryName', 'CategoryDescription', name, description, repository)
        add_category.Add_Category()





consult = input('1 - Add Category')
if consult == '1':
    name = input('Input the name you want to use with the new category: ')
    description = input('Input the description you want to add to the new category: ')
    add_category(name, description)
