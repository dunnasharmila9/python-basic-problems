## 79.Create an authentication decorator that checks username and password before allowing access to a function.
def authentication(func):
    def wrapper():

        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if username == "admin" and password == "1234":
            print("Login Successful")
            func()
        else:
            print("Access Denied")

    return wrapper
@authentication
def dashboard():
    print("Welcome to Dashboard")
dashboard()