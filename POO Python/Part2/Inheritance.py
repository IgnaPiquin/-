class Person:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality
        
    
    def talk(self):
        print('hello, Im talking')
        
    def play(self):
        print('Playing...')



class Employee(Person):
    def __init__(self, name, age, nationality, work, Salary):
        super().__init__(name, age, nationality)
        self.work=work
        self.Salary=Salary
    
    #overwriting th method play
    def play(self):
        print('Im working, I cant play...')


class Student(Person):
    def __init__(self, name, age, nationality, university, year):
        super().__init__(name, age, nationality)
        self.university=university
        self.year=year
    
    #overwriting th method play
    def play(self):
        print('Im Studying, I cant play...')
    
    
    

Roberto = Employee('Roberto', 43, 'argentino', 'programador', 10000)