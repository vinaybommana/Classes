values = [10, 20, 15, 30, 25, 5, 40]

total = 0

for val in values:
    print(total, val)
    if total > 50:
        break
    total = total + val
