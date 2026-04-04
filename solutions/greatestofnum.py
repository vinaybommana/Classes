numbers = [1, 99, 0, 209, 1000, 998, 12]

biggest = -1

# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
# print(sorted_numbers[len(sorted_numbers)-1])

for num in numbers:
    print(num, biggest)
    if num > biggest:
        biggest = num

print(biggest)
