import sys

user_inputs = sys.argv[1:]

sum = 0
for i in user_inputs:
    sum += int(i)

print(f"the sum is {sum}")