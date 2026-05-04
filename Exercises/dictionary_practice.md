# Dictionary Practice Problems

---

### Useful dictionary methods:

| Method | Description |
|---|---|
| `d.keys()` | Returns all keys |
| `d.values()` | Returns all values |
| `d.items()` | Returns all key-value pairs as tuples |
| `d.get(key, default)` | Returns value for key, or default if key doesn't exist |
| `d.pop(key)` | Removes key and returns its value |
| `d.update(other_dict)` | Merges another dictionary into this one |
| `key in d` | Checks if a key exists in the dictionary |

---

## Problem 1: Phone Book Lookup

Create a dictionary called `phone_book` with the following contacts:

| Name | Phone Number |
|---|---|
| Alice | 555-1234 |
| Bob | 555-5678 |
| Charlie | 555-9012 |

Then:

1. Print Bob's phone number
2. Add a new contact: Diana with number 555-3456
3. Update Alice's number to 555-0000
4. Print the entire phone book

**Expected output:**

```
555-5678
{'Alice': '555-0000', 'Bob': '555-5678', 'Charlie': '555-9012', 'Diana': '555-3456'}
```

**Hint:** access values with `phone_book["Bob"]` and add/update with `phone_book["Diana"] = "555-3456"`.

---

## Problem 2: Counting Characters

Given this string:

```python
text = "hello world"
```

Write code that creates a dictionary where each **character** is a key and the **count** of how many times it appears is the value. Skip spaces.

**Expected output:**

```
{'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
```

**Hint:** loop through each character. Use `d.get(char, 0)` to get the current count (defaulting to 0 if the character hasn't been seen yet), then add 1.

---

## Problem 3: Student Grades

Given this dictionary:

```python
grades = {
    "Alice": [85, 92, 78],
    "Bob": [90, 88, 95],
    "Charlie": [70, 75, 80],
    "Diana": [100, 98, 97]
}
```

1. Calculate and print each student's **average** grade
2. Find and print the student with the **highest** average

**Expected output:**

```
Alice: 85.0
Bob: 91.0
Charlie: 75.0
Diana: 98.33
Top student: Diana with average 98.33
```

**Hint:** use `sum(grades_list) / len(grades_list)` to compute the average. Use `round(value, 2)` to round to 2 decimal places.

---

## Problem 4: Merging Dictionaries

Given these two dictionaries:

```python
prices_store_a = {"apples": 1.50, "bananas": 0.75, "oranges": 2.00}
prices_store_b = {"bananas": 0.60, "grapes": 3.00, "oranges": 1.80}
```

Write code that creates a new dictionary `best_prices` containing the **lowest price** for each item across both stores.

**Expected output:**

```
{'apples': 1.5, 'bananas': 0.6, 'oranges': 1.8, 'grapes': 3.0}
```

**Hint:** combine all keys from both dictionaries, then for each key check which store has the lower price. Use `d.get(key, float('inf'))` so that missing items don't win the comparison.

---

## Problem 5: Inverting a Dictionary

Given this dictionary:

```python
capitals = {
    "USA": "Washington D.C.",
    "France": "Paris",
    "Japan": "Tokyo",
    "India": "New Delhi"
}
```

Create a **new dictionary** where the keys and values are swapped — the capitals become keys and the countries become values.

**Expected output:**

```
{'Washington D.C.': 'USA', 'Paris': 'France', 'Tokyo': 'Japan', 'New Delhi': 'India'}
```

**Hint:** loop through `capitals.items()` to get both the key and value at the same time, then build the new dictionary with them reversed.

---

## Problem 6: Nested Dictionaries

Given this nested dictionary representing a school:

```python
school = {
    "math": {
        "teacher": "Mr. Smith",
        "students": ["Alice", "Bob", "Charlie"]
    },
    "science": {
        "teacher": "Ms. Johnson",
        "students": ["Diana", "Alice", "Eve"]
    },
    "english": {
        "teacher": "Mrs. Davis",
        "students": ["Bob", "Charlie", "Eve", "Frank"]
    }
}
```

1. Print the teacher for the science class
2. Print the number of students in the english class
3. Find and print all students who are in **more than one** class

**Expected output:**

```
Ms. Johnson
4
Students in more than one class: Alice, Bob, Charlie, Eve
```

**Hint:** for part 3, collect all student names and count how many times each appears. You can use a dictionary to count, or you can use a list and check with `.count()`.

---

## Problem 7: Dictionary Comprehension

Dictionary comprehensions let you build dictionaries in a single line, similar to list comprehensions:

```python
# Syntax: {key_expr: value_expr for item in iterable}
squares = {x: x ** 2 for x in range(1, 6)}
# Result: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

Given this list:

```python
words = ["apple", "banana", "cherry", "date", "elderberry"]
```

Use a **dictionary comprehension** to create a dictionary where each word is a key and its **length** is the value.

**Expected output:**

```
{'apple': 5, 'banana': 6, 'cherry': 6, 'date': 4, 'elderberry': 10}
```
