class Person():
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    
    @name.deleter
    def name(self):
        del self.__name
        

person1 = Person('Ignacio', 18)

print(person1.name)

person1.name = 'Santiago'

print(person1.name)

del person1.name

print(person1.name)
            
            