# readlines() method --> dumping everything from the file
# read() --> using iterator
# readline() --> reading only first line of the method


# f = open("sample.txt", "r")
# # file_content = f.readlines()
# # for l in f:
# #     print(l)
# # print(file_content)
# single_line = f.readline()
# print(single_line) # this is a sample file\n

# f.close()

with open("sample.txt", "r") as f:
    print(f.readlines())
