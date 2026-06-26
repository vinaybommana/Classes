# Write a function called power that takes a base and an exponent. The exponent should have a default value of 2 (so it squares the number if no exponent is given).


def power(base, exponent=2): # exponent is a default argument
    return base ** exponent

print(power(3))
print(power(3, 4))