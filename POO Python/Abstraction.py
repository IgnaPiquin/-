# the term "abstraction" refers to the process of simplifying complex systems
class Car():
    def __init__(self):
        self.state = 'off'
    
    def turn_on(self):
        self.state = 'on'
        print ('The car is on')
    
    def drive(self):
        if self.state == 'off':
            self.turn_on()
        print ('Riding the car')


my_car = Car()
my_car.drive()