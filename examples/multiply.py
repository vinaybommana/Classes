# number1 = int(input("give the first number:"))
# number2 = int(input("give the second number"))

# product = number1 * number2
# print(f"the product is {product}")
import sys

# print(sys.argv)
# print(int(sys.argv[1]) * int(sys.argv[2])) # command line argument
print(sys.argv[1:]) # slicing
product = 1
for i in sys.argv[1:]:
    if i:
        product = product * int(i)

print(f"product is {product}")
