# Special Methods are implemented to change the behavior of the class, in this case with the + operator.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'Person(name={self.name}, age={self.age})'
    
    def __add__(self, other):
        new_value = self.age + other.age
        return Person(self.name+other.name, new_value)

ignacio = Person('ignacio', 18)
dalto = Person('Lucas', 21)

newPerson = ignacio+dalto
print (newPerson)