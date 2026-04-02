var = input("What is your age: ") # str

# error handling
try:
    var = int(var) # type conversion
except ValueError:
    print("you can't enter strings, please enter a number")

print(type(var))