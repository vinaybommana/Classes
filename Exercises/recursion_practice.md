# Recursion Practice Problems

---

## Problem 1: Reverse a String

Write a **recursive** function called `reverse_string` that takes a string and returns it reversed.

**Think about it:**
- What is the base case? (What is the simplest string to reverse?)
- How can you break the problem into a smaller piece?

```python
print(reverse_string("hello"))
print(reverse_string("abc"))
print(reverse_string("a"))
print(reverse_string(""))
```

**Expected output:**

```
olleh
cba
a

```

**Hint:** The reverse of `"hello"` is `reverse_string("ello") + "h"`. The base case is an empty string.

---

## Problem 2: Count Digits

Write a **recursive** function called `count_digits` that takes a positive integer and returns the number of digits in it.

```python
print(count_digits(42))
print(count_digits(7))
print(count_digits(100000))
```

**Expected output:**

```
2
1
6
```

**Hint:** Dividing by 10 with `n // 10` removes the last digit. When `n < 10`, you have exactly 1 digit — that's your base case.

---

## Problem 3: Sum of Digits

Write a **recursive** function called `sum_digits` that takes a positive integer and returns the sum of its digits.

```python
print(sum_digits(123))
print(sum_digits(9))
print(sum_digits(4567))
```

**Expected output:**

```
6
9
22
```

**Hint:** `n % 10` gives the last digit. `n // 10` gives the rest. Base case: a single digit number (`n < 10`).

---

## Problem 4: Trace It! (Paper exercise)

**Without running the code**, trace through the following function call and write down the output at each step.

```python
def mystery(n):
    if n <= 0:
        return 0
    print(n)
    return n + mystery(n - 2)

result = mystery(7)
print(f"Result: {result}")
```

**Your task:** Write down:
1. What gets printed at each step
2. What value each call returns
3. The final result

**After tracing on paper, run the code to check your answer.**

---

## Problem 5: Recursive vs Iterative — Power

Write **two versions** of a function that computes `base ** exp`:

1. `power_loop(base, exp)` — using a **loop**
2. `power_recursive(base, exp)` — using **recursion**

```python
print(power_loop(3, 4))
print(power_recursive(3, 4))
print(power_loop(2, 0))
print(power_recursive(2, 0))
```

**Expected output:**

```
81
81
1
1
```

---

## Problem 6: Trace It! (Paper exercise)

Trace the following recursive function call step by step. Show the call stack.

```python
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

result = power(2, 4)
```

**Your task:** Draw out each call like this:

```
power(2, 4) called
  power(2, 3) called
    ...
```

Write the return value at each level. Verify the final result is 16.

---

## Problem 7: Fibonacci (with tracing)

Write a recursive function `fib(n)` that returns the nth Fibonacci number.

```
fib(0) = 0
fib(1) = 1
fib(n) = fib(n-1) + fib(n-2)
```

```python
print(fib(0))
print(fib(1))
print(fib(6))
print(fib(10))
```

**Expected output:**

```
0
1
8
55
```

**Bonus:** Add a counter to see how many times `fib` is called for `fib(10)`. Why is this number so high? Could you solve this with a loop instead? Try writing `fib_loop(n)` and compare.

---

## Problem 8: Recursive List Search

Write a **recursive** function called `search(lst, target)` that returns `True` if the target is in the list, `False` otherwise. Do **not** use the `in` operator.

```python
print(search([4, 2, 7, 1, 9], 7))
print(search([4, 2, 7, 1, 9], 5))
print(search([], 3))
```

**Expected output:**

```
True
False
False
```

**Hint:** Check the first element. If it matches, return `True`. Otherwise, search the rest of the list `lst[1:]`. Base case: empty list returns `False`.

---

## Problem 9: Trace It! (Paper exercise)

Trace the following code. List what gets printed and the return value.

```python
def sum_list(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sum_list(lst[1:])

result = sum_list([5, 3, 8])
print(result)
```

**Your trace should look like:**

```
sum_list([5, 3, 8]) called
  sum_list([3, 8]) called
    sum_list([8]) called
      sum_list([]) called → returns 0
    returns 8 + 0 = 8
  returns 3 + 8 = 11
returns 5 + 11 = 16
```

**Final output:** `16`

---

## Problem 10: Palindrome Checker

Write a **recursive** function called `is_palindrome` that takes a string and returns `True` if it reads the same forwards and backwards.

```python
print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("madam"))
print(is_palindrome("a"))
print(is_palindrome(""))
```

**Expected output:**

```
True
False
True
True
True
```

**Hint:** Compare the first and last characters. If they match, recursively check the substring without those two characters. Base case: a string of length 0 or 1 is always a palindrome.
