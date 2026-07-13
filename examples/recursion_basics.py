# ============================================================
# Understanding Recursion
# ============================================================
#
# Recursion = a function that calls ITSELF
#
# Every recursive function needs TWO things:
#   1. BASE CASE    - when to STOP (prevents infinite loop)
#   2. RECURSIVE CASE - the function calls itself with a SMALLER problem
#

# --------------------------------------------------
# Example 1: Countdown (simplest recursion)
# --------------------------------------------------
# Non-recursive version (loop)
def countdown_loop(n):
    while n > 0:
        print(n)
        n -= 1
    print("Go!")

# Recursive version
def countdown(n):
    if n <= 0:         # BASE CASE: stop when n reaches 0
        print("Go!")
        return
    print(n)
    countdown(n - 1)   # RECURSIVE CASE: call itself with n-1

print("=== Countdown (recursive) ===")
countdown(5)


# --------------------------------------------------
# Example 2: Factorial   n! = n * (n-1) * ... * 1
# --------------------------------------------------
# Non-recursive version (loop)
def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

# Recursive version
def factorial(n):
    if n == 0 or n == 1:      # BASE CASE
        return 1
    return n * factorial(n - 1)  # RECURSIVE CASE

print("\n=== Factorial ===")
print(f"factorial(5) = {factorial(5)}")       # 120
print(f"factorial_loop(5) = {factorial_loop(5)}")  # 120


# --------------------------------------------------
# Example 3: Sum of a list
# --------------------------------------------------
# Non-recursive version (loop)
def sum_list_loop(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Recursive version
def sum_list(lst):
    if len(lst) == 0:       # BASE CASE: empty list
        return 0
    return lst[0] + sum_list(lst[1:])  # first element + sum of the rest

print("\n=== Sum of list ===")
numbers = [3, 7, 1, 9, 2]
print(f"sum_list({numbers}) = {sum_list(numbers)}")           # 22
print(f"sum_list_loop({numbers}) = {sum_list_loop(numbers)}") # 22


# --------------------------------------------------
# Example 4: Power / Exponentiation  (base^exp)
# --------------------------------------------------
# Non-recursive version (loop)
def power_loop(base, exp):
    result = 1
    for i in range(exp):
        result = result * base
    return result

# Recursive version
def power(base, exp):
    if exp == 0:             # BASE CASE: anything^0 = 1
        return 1
    return base * power(base, exp - 1)  # RECURSIVE CASE

print("\n=== Power ===")
print(f"power(2, 8) = {power(2, 8)}")           # 256
print(f"power_loop(2, 8) = {power_loop(2, 8)}") # 256
