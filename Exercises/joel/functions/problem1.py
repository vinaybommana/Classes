# Problem 1: Greeting Machine
# Write a function called greet that takes a name as a parameter and prints a greeting message.

def greet(name): # name is an str
    if type(name) == str:
        print(f"Hi, {name}")
    
    return ""

greet("joel")
greet("vinay")
greet("hannah")
greet("ash")
greet("joe")