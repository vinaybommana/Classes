# Python Functions Practice Problems

---

## Problem 1: Greeting Machine

Write a function called `greet` that takes a **name** as a parameter and **prints** a greeting message.

```python
greet("Alice")
greet("Bob")
```

**Expected output:**

```
Hello, Alice! Welcome!
Hello, Bob! Welcome!
```

**Hint:** Define the function with `def greet(name):` and use an f-string inside it.

---

## Problem 2: Add Two Numbers

Write a function called `add` that takes **two numbers** as parameters and **returns** their sum. Print the result of calling the function.

```python
result = add(10, 25)
print(result)
print(add(3, 7))
```

**Expected output:**

```
35
10
```

**Hint:** Use the `return` keyword to send the result back. Remember, `return` is different from `print` — `return` gives the value back to the caller.

---

## Problem 3: Even or Odd

Write a function called `even_or_odd` that takes a number and **returns** the string `"Even"` if the number is even, or `"Odd"` if it is odd.

```python
print(even_or_odd(4))
print(even_or_odd(7))
print(even_or_odd(0))
```

**Expected output:**

```
Even
Odd
Even
```

**Hint:** Use `number % 2 == 0` to check if a number is even.

---

## Problem 4: Default Parameters

Write a function called `power` that takes a **base** and an **exponent**. The exponent should have a **default value of 2** (so it squares the number if no exponent is given).

```python
print(power(5))
print(power(3, 3))
print(power(2, 10))
```

**Expected output:**

```
25
27
1024
```

**Hint:** Define it as `def power(base, exponent=2):` and use the `**` operator.

---

## Problem 5: Return Multiple Values

Write a function called `min_max` that takes a **list of numbers** and **returns both** the minimum and maximum values as a tuple.

```python
low, high = min_max([4, 1, 8, 3, 9, 2])
print(f"Min: {low}, Max: {high}")

low, high = min_max([100])
print(f"Min: {low}, Max: {high}")
```

**Expected output:**

```
Min: 1, Max: 9
Min: 100, Max: 100
```

**Hint:** You can return multiple values with `return min_val, max_val`. Python packs them into a tuple automatically.

---

## Problem 6: Keyword Arguments

Write a function called `build_profile` that takes a **name** (required), and **keyword arguments** `age`, `city`, and `job` (all with default value `"Not provided"`). It should return a formatted string with the profile info.

```python
print(build_profile("Alice", age=30, city="New York"))
print(build_profile("Bob", job="Engineer"))
print(build_profile("Charlie", age=25, city="Austin", job="Designer"))
```

**Expected output:**

```
Name: Alice, Age: 30, City: New York, Job: Not provided
Name: Bob, Age: Not provided, City: Not provided, Job: Engineer
Name: Charlie, Age: 25, City: Austin, Job: Designer
```

**Hint:** Define it as `def build_profile(name, age="Not provided", city="Not provided", job="Not provided"):`.

---

## Problem 7: *args — Flexible Addition

Write a function called `add_all` that takes **any number of arguments** using `*args` and returns their sum.

```python
print(add_all(1, 2, 3))
print(add_all(10, 20, 30, 40, 50))
print(add_all(5))
print(add_all())
```

**Expected output:**

```
6
150
5
0
```

**Hint:** Use `*args` in the function definition. Inside the function, `args` is a tuple — you can loop through it or use `sum()`.

---

## Problem 8: **kwargs — Build a Dictionary

Write a function called `make_dict` that takes `**kwargs` and returns a dictionary of only the key-value pairs where the value is **not None**.

```python
result = make_dict(name="Alice", age=30, email=None, city="NYC")
print(result)

result = make_dict(a=1, b=None, c=None, d=4)
print(result)
```

**Expected output:**

```
{'name': 'Alice', 'age': 30, 'city': 'NYC'}
{'a': 1, 'd': 4}
```

**Hint:** Use `**kwargs` in the definition. Inside, `kwargs` is a dictionary — use a dictionary comprehension or loop to filter out `None` values.

---

## Problem 9: Function Calling Another Function

Write **two functions**:

1. `is_prime(n)` — returns `True` if `n` is a prime number, `False` otherwise.
2. `primes_in_range(start, end)` — returns a **list** of all prime numbers between `start` and `end` (inclusive). It should **call** `is_prime` to check each number.

```python
print(is_prime(7))
print(is_prime(10))
print(primes_in_range(1, 20))
print(primes_in_range(50, 60))
```

**Expected output:**

```
True
False
[2, 3, 5, 7, 11, 13, 17, 19]
[53, 59]
```

**Hint:** A number is prime if it is greater than 1 and not divisible by any number from 2 to its square root. Use `range(2, int(n**0.5) + 1)` for efficiency.

---

## Problem 10: Lambda Functions and Sorting

Given a list of tuples representing students and their grades, use a **lambda function** to:

1. Sort the list by **grade** (second element) in descending order.
2. Filter out students who scored **below 70** using `filter()` and a lambda.

```python
students = [("Alice", 85), ("Bob", 62), ("Charlie", 91), ("Diana", 70), ("Eve", 55)]

sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print("Sorted:", sorted_students)

passing = list(filter(lambda x: x[1] >= 70, students))
print("Passing:", passing)
```

**Expected output:**

```
Sorted: [('Charlie', 91), ('Alice', 85), ('Diana', 70), ('Bob', 62), ('Eve', 55)]
Passing: [('Alice', 85), ('Charlie', 91), ('Diana', 70)]
```

**Hint:** `lambda x: x[1]` accesses the second element of each tuple. `sorted()` with `reverse=True` sorts in descending order. `filter(func, iterable)` keeps items where `func` returns `True`.

---

## Bonus Problem: Recursive Function

Write a **recursive** function called `flatten` that takes a nested list and returns a single flat list with all elements.

```python
print(flatten([1, [2, 3], [4, [5, 6]], 7]))
print(flatten([[1, 2], [[3]], [4, [5, [6]]]]))
print(flatten([1, 2, 3]))
```

**Expected output:**

```
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6]
[1, 2, 3]
```

**Hint:** Check if each element `isinstance(item, list)`. If it is, recursively call `flatten` on it. Otherwise, add it to your result. A function calling itself is called **recursion** — just make sure you have a base case (when the item is not a list).
