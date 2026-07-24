
def function_with_loops(number):
    product = 1
    while number > 1:
        product = product * number
        number = number - 1

    return product

# print(recursion_with_loops(6))

def factorial_with_recursion(number):
    # base condition
    if number <= 1:
        return 1
    # calling function
    else:
        print(number , f"factorial({number})")
        return number * factorial_with_recursion(number - 1)
    
print(factorial_with_recursion(5))