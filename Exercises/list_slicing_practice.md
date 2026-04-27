# List Slicing Practice Problems

---

## Problem 1: First and Last Three

Given this list:

```python
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
```

Using list slicing, print:

1. The first 3 elements
2. The last 3 elements
3. Everything except the first and last element

**Expected output:**

```
['red', 'orange', 'yellow']
['blue', 'indigo', 'violet']
['orange', 'yellow', 'green', 'blue', 'indigo']
```

**Hint:** negative indices count from the end of the list. `my_list[-3:]` gives the last 3 elements.

---

## Problem 2: Every Other Element

Given this list:

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```

Using list slicing with a **step**, print:

1. Every other element starting from the first (`10, 30, 50, ...`)
2. Every other element starting from the second (`20, 40, 60, ...`)
3. The list in reverse order

**Expected output:**

```
[10, 30, 50, 70, 90]
[20, 40, 60, 80, 100]
[100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
```

**Hint:** the full slice syntax is `list[start:stop:step]`. A step of `2` skips every other element, and a step of `-1` reverses the list.

---

## Problem 3: Palindrome Checker

Given these strings:

```python
words = ["racecar", "hello", "madam", "python", "level"]
```

For each word, use list slicing to check if the word is a **palindrome** (reads the same forwards and backwards). Print each word along with whether it is a palindrome or not.

**Expected output:**

```
racecar -> palindrome
hello -> not a palindrome
madam -> palindrome
python -> not a palindrome
level -> palindrome
```

**Hint:** strings support the same slicing syntax as lists. `word[::-1]` gives the reversed string.

---

## Problem 4: Swap Halves

Given this list:

```python
data = [1, 2, 3, 4, 5, 6, 7, 8]
```

Use list slicing to create a **new list** where the first half and second half are swapped.

**Expected output:**

```
[5, 6, 7, 8, 1, 2, 3, 4]
```

**Hint:** find the midpoint with `len(data) // 2`, then slice the list into two halves and combine them with `+`.
