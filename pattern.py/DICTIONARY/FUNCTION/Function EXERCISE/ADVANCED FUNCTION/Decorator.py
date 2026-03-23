def decorator(func):
    def wrapper():
        print("Before Execution")
        func()
        print("After Execution")
    return wrapper
def greet():
    print("Hello!")
greet = decorator(greet)
greet()
