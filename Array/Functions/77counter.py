## 77.Create a closure function that acts as a counter and remembers previous count values.
def outer():

    count = 0

    def inner():
        nonlocal count

        count += 1

        print("Count =", count)

    return inner
counter = outer()
counter()
counter()
counter()
counter()
counter()