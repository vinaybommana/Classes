# conditionals
import math

print(math.pi)

# boolean value: true or false
# True and False

var = 2
# if var < 1: # true or false (2 < 1)
# if <conditional-check>:
# ....
if (var < 1) or (var == 1): # (2 < 1) or (2 == 1) # false or false # false
    # do something
    print(f"{var} is less than 1")
elif var < 2: # (2 < 2) # false
    print(f"{var} is less than 2")
else:
    # do something
    print(f"{var} is greater than 1")


fruit = "apple"
