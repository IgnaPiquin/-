'''Class decorators are typically implemented as functions that take a class as an argument and return a modified version of that class. You can use the @decorator_name syntax to apply the decorator to a class definition.'''
def my_decorator(cls):
    def new_method(self):
        return "This is a new method!"
    
    cls.new_method = new_method
    cls.new_attribute = "Hello from the decorator!"
    return cls

@my_decorator
class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(42)
print(obj.value)            # Output: 42
print(obj.new_attribute)    # Output: Hello from the decorator!
print(obj.new_method())     # Output: This is a new method!

# Using Class Inheritance
'''
class MyClass:
    def __init__(self, value):
        self.value = value

class MySubclass(MyClass):
    def new_method(self):
        return "This is a new method!"

obj = MySubclass(42)
print(obj.value)           # Output: 42
print(obj.new_method())    # Output: This is a new method!
'''