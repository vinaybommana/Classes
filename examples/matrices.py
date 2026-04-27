matrix_a = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]] # 4x4

flag = False  #boolean True flag
for i in range(len(matrix_a)): # outer list
    for j in range(len(matrix_a[0])): # inner list
        # matrix_a[i][j] = matrix_a[i][j] + 1
        print(matrix_a[i][j])
        if matrix_a[i][j] == 11:
            flag = True
            break
    print(f"value is {flag}")
    if flag is True:
        break

# for i in range(len(matrix_a)): # outer list
#     for j in range(len(matrix_a[0])): # inner list
#         print(matrix_a[i][j])
#         if matrix_a[i][j] == 11:
#             break


# list_a = [1, 2, 3, 4, 5]
# for i in range(len(list_a)):
#     print(list_a[i])
#     if list_a[i] == 3:
#         break