l = [1,2,3,4,5,6]

i = len(l) - 1
# print(l[i])
new_list = []
while i >= 0:
    print(i, new_list)
    new_list.append(l[i])
    i = i - 1

print(new_list)