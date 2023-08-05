class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def Identity(self):
        print (f'Name: {self.name} \nAge: {self.age}')


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    
    def Grade(self):
        print(f'Grade: {self.grade}')


Student1=Student('Ignacio', '18', '7')
print(Student1.name, Student1.age, Student1.grade)

Student1.Identity()
Student1.Grade()
        