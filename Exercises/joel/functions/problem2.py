# Write a function called add that takes two numbers as parameters and returns their sum. Print the result of calling the function.


def add(number1, number2): # number1 and number2 are int
    if type(number1) == int and type(number2) == int:
        sum = number1 + number2
        return sum


print(add(1, 2))
total = add(4, 5)
print(total)