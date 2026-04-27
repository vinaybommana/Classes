number_list = [99, 102, 105, 107, 1000] # 1000, 107, 105, 102, 99

list_length = len(number_list)
# print(list_length)

output_list = []
while list_length > 0:
    print(list_length)
    output_list.append(number_list[list_length - 1])
    list_length = list_length - 1

print(output_list)