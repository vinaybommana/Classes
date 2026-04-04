numbers = [1, 2, 7, 8, 13, 14, 19, 20]

sum = 0
for number in numbers:
    if number % 2 == 0:
        sum = sum + number

print(f"The Sum of the Even Numbers is: {sum}")