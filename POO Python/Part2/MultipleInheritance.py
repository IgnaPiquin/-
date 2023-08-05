class Person:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality
        
    
    def talk(self):
        print('hello, Im talking')
        
    def play(self):
        print('Playing...')

class Artist:
    def __init__(self, ability):
        self.ability=ability
    
    def show_ability(self):
        return f'My ability is:{self.ability}'


class ArtistEmployee(Person, Artist):
    def __init__(self,name, age, nationality, ability, salary, enterprise):
        Person.__init__(self, name, age, nationality)
        Artist.__init__(self, ability)
        self.salary = salary
        self.enterprise = enterprise
        
    #overwriting the method show_ability IN THIS CLASS
    def show_ability(self):
        return f'I dont have one, haha'
    
    #calling the method from the father(super) class
    def introduction(self):
        return f'{super().show_ability()}'

class Employee(Person):
    def __init__(self, name, age, nationality, work, Salary):
        super().__init__(name, age, nationality)
        self.work=work
        self.Salary=Salary
    
    #overwriting the method play
    def play(self):
        print('Im working, I cant play...')

    
    
    

Roberto = ArtistEmployee('Roberto', 43, 'argentino', 'sing', 10000, 'windows')

subclass=issubclass(ArtistEmployee, Employee)
instance=isinstance(Roberto, Employee)


print(Roberto.introduction())