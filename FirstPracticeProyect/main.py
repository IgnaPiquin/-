import sqlite3
from Categories import *

with sqlite3.connect('FirstPracticeProyect.db') as connection:
    repository = CategoryRepository(connection)

    name = ""
    description = ""

    add_category = AddCategory('Categories', 'CategoryName', 'CategoryDescription', name, description, repository)
    add_category.Add_Category()