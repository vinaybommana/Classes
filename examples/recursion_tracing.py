# ============================================================
# Tracing Recursive and Non-Recursive Programs
# ============================================================
#
# Tracing = following the execution step by step
# We use indentation to show how deep the recursion goes
#

# --------------------------------------------------
# Example 1: Tracing Factorial
# --------------------------------------------------
def factorial_traced(n, depth=0):
    indent = "  " * depth
    print(f"{indent}factorial({n}) called")

    if n == 0 or n == 1:
        print(f"{indent}factorial({n}) returns 1  [BASE CASE]")
        return 1

    result = n * factorial_traced(n - 1, depth + 1)
    print(f"{indent}factorial({n}) returns {result}")
    return result

print("=== Tracing factorial(5) ===")
print(f"Final result: {factorial_traced(5)}")
# Expected trace:
# factorial(5) called
#   factorial(4) called
#     factorial(3) called
#       factorial(2) called
#         factorial(1) called
#         factorial(1) returns 1  [BASE CASE]
#       factorial(2) returns 2
#     factorial(3) returns 6
#   factorial(4) returns 24
# factorial(5) returns 120


# --------------------------------------------------
# Example 2: Tracing Sum of list
# --------------------------------------------------
def sum_list_traced(lst, depth=0):
    indent = "  " * depth
    print(f"{indent}sum_list({lst}) called")

    if len(lst) == 0:
        print(f"{indent}sum_list([]) returns 0  [BASE CASE]")
        return 0

    result = lst[0] + sum_list_traced(lst[1:], depth + 1)
    print(f"{indent}sum_list({lst}) returns {result}")
    return result

print("\n=== Tracing sum_list([3, 7, 1]) ===")
print(f"Final result: {sum_list_traced([3, 7, 1])}")
# Expected trace:
# sum_list([3, 7, 1]) called
#   sum_list([7, 1]) called
#     sum_list([1]) called
#       sum_list([]) called
#       sum_list([]) returns 0  [BASE CASE]
#     sum_list([1]) returns 1
#   sum_list([7, 1]) returns 8
# sum_list([3, 7, 1]) returns 11


# --------------------------------------------------
# Example 3: Tracing a non-recursive (iterative) version
# --------------------------------------------------
def factorial_loop_traced(n):
    print(f"factorial_loop({n}) called")
    result = 1
    for i in range(1, n + 1):
        result = result * i
        print(f"  step {i}: result = {result}")
    print(f"factorial_loop({n}) returns {result}")
    return result

print("\n=== Tracing factorial_loop(5) ===")
print(f"Final result: {factorial_loop_traced(5)}")
# Expected trace:
# factorial_loop(5) called
#   step 1: result = 1
#   step 2: result = 2
#   step 3: result = 6
#   step 4: result = 24
#   step 5: result = 120
# factorial_loop(5) returns 120


# --------------------------------------------------
# Example 4: Fibonacci — see the branching!
# --------------------------------------------------
# fib(0) = 0, fib(1) = 1
# fib(n) = fib(n-1) + fib(n-2)
#
# This is a TREE recursion — each call makes TWO recursive calls

call_count = 0

def fibonacci_traced(n, depth=0):
    global call_count
    call_count += 1
    indent = "  " * depth
    print(f"{indent}fib({n}) called")

    if n <= 1:
        print(f"{indent}fib({n}) returns {n}  [BASE CASE]")
        return n

    left = fibonacci_traced(n - 1, depth + 1)
    right = fibonacci_traced(n - 2, depth + 1)
    result = left + right
    print(f"{indent}fib({n}) returns {result}")
    return result

print("\n=== Tracing fibonacci(4) ===")
call_count = 0
print(f"Final result: {fibonacci_traced(4)}")
print(f"Total function calls: {call_count}")
# Notice how many calls it takes — fib(2) is computed multiple times!


# --------------------------------------------------
# Example 5: Side-by-side comparison table
# --------------------------------------------------
print("\n" + "=" * 55)
print("COMPARISON: Recursive vs Non-recursive (Iterative)")
print("=" * 55)
print(f"{'Feature':<25} {'Recursive':<15} {'Iterative':<15}")
print("-" * 55)
print(f"{'Uses a loop?':<25} {'No':<15} {'Yes':<15}")
print(f"{'Calls itself?':<25} {'Yes':<15} {'No':<15}")
print(f"{'Needs a base case?':<25} {'Yes':<15} {'No':<15}")
print(f"{'Uses more memory?':<25} {'Yes (stack)':<15} {'No':<15}")
print(f"{'Easier to read?':<25} {'Sometimes':<15} {'Sometimes':<15}")
print(f"{'Risk of stack overflow?':<25} {'Yes':<15} {'No':<15}")
