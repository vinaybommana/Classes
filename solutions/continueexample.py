for i in range(1, 40):
    print(i)
    if i % 4 == 0:
        continue
    if i % 2 == 0:
        print(f"{i} is even")


print("loop is done")