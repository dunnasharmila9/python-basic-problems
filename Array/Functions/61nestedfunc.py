## Create a nested function where one function is defined inside another function.
def user_authentication(name,email):
    def clean_up(text):
         return text.strip().lower()
    clean_name=clean_up(name)
    clean_email=clean_up(email)
    print("saved:",clean_name,"-",clean_email)
user_authentication("sharmila","dunnasharmila9@gmail.com")        

    
      