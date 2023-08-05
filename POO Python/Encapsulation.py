class MyClass:
    def __init__(self):
        #Private Attributes ()
        self._private_var = 42
        #Very Private Attributes
        self.__very_private_var = 100

'''In general, the use of private and very private attributes in Python is a matter of convention and is meant to indicate the intended usage of the attribute rather than enforcing strict access control.'''

obj = MyClass()
print(obj._private_var)
print(obj.__very_private_var)  # This will raise an AttributeError
print(obj._MyClass__very_private_var)  # This will access the attribute successfully but is not the correct way(more on getters and setters)