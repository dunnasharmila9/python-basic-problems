## Create a function using **kwargs to display student details.
def Student(name,roll_number,**kwargs):
    print("Name:",name)
    print("Rollnumber:",roll_number)
    for k,v in kwargs.items():
        print(k+":",v)
print("Student one Details:")        
Student(name="sharmila",roll_number="24B11DS053",Branch="DS",Section=2)
print("Student two details:")
Student(name="Ramya",roll_number="24B11IT024",Branch="IT")        
       