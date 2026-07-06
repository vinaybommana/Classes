cart = [
    ("Notebook", 5.99, 3),
    ("Pen", 1.50, 10),
    ("Backpack", 29.99, 1)
]




def calculate_subtotal(c):

    total_cost = 0
    for i in c:
        item_name, cost, n = i
        total_cost = total_cost + (cost * n)
    
    return total_cost

calculate_subtotal(cart)

print(calculate_subtotal(cart))
    