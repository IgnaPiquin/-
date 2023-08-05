def decorator(function):
    def modified_function():
        print('before calling the fuction')
        function()
        print('before calling the fuction')
    return modified_function
#This is a non standard way of using decorators
# def greeting():
#     print('hi igna')

# modified_greeting = decorator(greeting)
# modified_greeting()
@decorator
def greeting():
    print('hi igna')

greeting()