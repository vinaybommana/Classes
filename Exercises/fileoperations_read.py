# sample.txt

# f = open("sample.txt")
# print(f.readline())
# f.close()

# f = open("sample.txt")
# for line in f:
#     print(line)

# f.close()

with open("sample.txt") as f: # with
    for line in f:
        print(line)

with open("sample.txt", "a") as f:
    f.write("\nthis is another test")
