class Cat():
    def Sound(self):
        return 'miau'
    
class Dog():
    def Sound(self):
        return 'Guau'


def make_sound(animal):
    print(animal.Sound())

cat = Cat()
dog = Dog()

print(dog.Sound())
print(cat.Sound())


make_sound(dog)
make_sound(cat)