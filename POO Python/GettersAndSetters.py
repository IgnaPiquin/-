class Person:
    def __init__(self, name, age):
        self._name=name
        self._age=age
    
    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        self._name=new_name
        

person1 = Person('Ignacio', 18)

name = person1.get_name()
print (name)

name = person1.set_name('Santiago')
print (name)

'''Using getters and setters enhances the principle of encapsulation, which is a fundamental concept of object-oriented programming. It allows you to hide the internal implementation details of the class, reducing coupling and making your code more maintainable and robust.(More on how to make them esear to use in Properties)'''
