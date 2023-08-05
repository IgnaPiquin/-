from abc import ABC, abstractclassmethod
#Abrstract Classes are a useful way to foment polymorphism and to implement your own documentation for your classes.
class Person(ABC):
    @abstractclassmethod
    def __init__(self, name, age, sex, activity):
        self.name = name
        self.age = age
        self.sex = sex
        self.activity = activity
    
    @abstractclassmethod
    def do_activity(self):
        pass
    
    def introduce_oneself(self):
        print (f'Hi my name is: {self.name} and I am {self.age} years old')

class Student(Person):
    def __init__(self, name, age, sex, activity):
        super().__init__(name, age, sex, activity)
        
    def do_activity(self):
        print (f'I am currently studying: {self.activity}')

class Worker(Person):
    def __init__(self, name, age, sex, activity):
        super().__init__(name, age, sex, activity)
    
    def do_activity(self):
        print (f'My current work is: {self.activity}')
        

Ignacio= Student('Ignacio', 18, 'Masculine', 'Data Science')
Santiago = Worker('Santiago', 18, 'Masculine', 'Coding')

Ignacio.introduce_oneself()
Ignacio.do_activity() 
Santiago.introduce_oneself()
Santiago.do_activity()
