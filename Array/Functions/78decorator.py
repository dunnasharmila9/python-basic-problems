## Create a decorator that prints a message before and after executing any function.
def message(func):

    def wrapper():
        print("Before Executing Function")

        func()

        print("After Executing Function")

    return wrapper

@message
def addition():
    a = 10
    b = 20
    print("Sum =", a + b)
addition()