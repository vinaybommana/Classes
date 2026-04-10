list_a = [1, 3, 5, 7]
list_b = [2, 5, 8, 3]  # couple of lists

# Use a nested loop to find the first pair (a, b) where a + b == 10. Print the pair and break out of both loops.

outer_loop_break = False # boolean
for i in list_a:
    for j in list_b: # nested loops
        print(i, j)
        if i + j == 10:
            outer_loop_break = True
            break
    
    if outer_loop_break is True:
        # print(i, j)
        break