import sqlite3
from Categories import CategoryRepository, AddCategory

with sqlite3.connect('FirstPracticeProyect.db') as connection:
    repository = CategoryRepository(connection)

    name = "test"
    description = "testAll kinds of beverages, like coke, water, juice, etc."

    add_category = AddCategory('Categories', 'CategoryName', 'CategoryDescription', name, description, repository)
    add_category.Add_Category()