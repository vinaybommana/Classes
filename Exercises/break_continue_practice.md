# Break & Continue Practice Problems

---

## Problem 1: Skip the Odds

Loop through the numbers 1 to 15. Use `continue` to **skip odd numbers** and only print the even ones.

**Expected output:**

```
2
4
6
8
10
12
14
```

**Hint:** Use `if number % 2 != 0` to detect odd numbers, then `continue` to skip them.

---

## Problem 2: Stop at the First Negative

Given this list:

```python
numbers = [5, 12, 8, 3, -1, 7, 10, -6, 2]
```

Use a `for` loop to print each number, but **break out of the loop** as soon as you encounter a negative number. Do **not** print the negative number.

**Expected output:**

```
5
12
8
3
```

---

## Problem 3: Skip Banned Users

Given this list of usernames:

```python
users = ["alice", "bob", "admin", "charlie", "root", "diana"]
banned = ["admin", "root"]
```

Loop through `users` and print a welcome message for each one, but use `continue` to **skip any user in the banned list**.

**Expected output:**

```
Welcome, alice!
Welcome, bob!
Welcome, charlie!
Welcome, diana!
```

---

## Problem 4: Find the First Passing Score

Given this list of test scores:

```python
scores = [42, 55, 38, 61, 73, 90, 85]
```

Use a `for` loop to find the **first score that is 60 or above**. Print it and then `break` out of the loop.

**Expected output:**

```
First passing score: 61
```

---

## Problem 5: Clean Data — Skip Blanks

Given this list of user inputs:

```python
inputs = ["hello", "", "world", "", "", "python", ""]
```

Loop through the list. Use `continue` to skip any **empty strings**. Print only the non-empty values.

**Expected output:**

```
hello
world
python
```

---

## Problem 6: Search and Stop

Given this list of words:

```python
words = ["apple", "banana", "cherry", "dragonfruit", "elderberry"]
```

Use a `for` loop to search for a word that starts with the letter `"d"`. When you find it, print the word and `break`. If no word is found, print `"Not found"`.

**Hint:** Use the `for...else` pattern — the `else` block after a `for` loop only runs if the loop was **not** exited by a `break`.

```python
for word in words:
    if ...:
        ...
        break
else:
    print("Not found")
```

**Expected output:**

```
Found: dragonfruit
```

---

## Problem 7: Sum Until Limit

Given this list:

```python
values = [10, 20, 15, 30, 25, 5, 40]
```

Use a loop to add up the values one by one. **Break** as soon as the running total **exceeds 50**. Print the total just before it exceeded the limit, and how many numbers were added.

**Expected output:**

```
Added 3 numbers
Total before exceeding limit: 45
```

**Explanation:** 10 + 20 + 15 = 45. Adding the next value (30) would make it 75, which exceeds 50, so we stop.

---

## Problem 8: Skip Multiples of 3, Stop at 25

Loop through numbers 1 to 40.

- Use `continue` to **skip** any number that is a multiple of 3
- Use `break` to **stop** the loop entirely when the number reaches 25

Print each number that is not skipped.

**Expected output:**

```
1
2
4
5
7
8
10
11
13
14
16
17
19
20
22
23
25
```

---

## Problem 9: Password Retry (while + break)

Simulate a login system. The correct password is `"python123"`. The user gets a maximum of 3 attempts. Use a `while` loop.

```python
correct_password = "python123"
attempts = ["letmein", "python123", "hello"]
```

Loop through the attempts using a `while` loop. If the password matches, print `"Access granted!"` and `break`. If all attempts are used without a correct guess, print `"Account locked."`.

**Expected output:**

```
Attempt 1: Wrong password.
Attempt 2: Access granted!
```

---

## Problem 10: Nested Loop with Break — Find a Pair

Given these two lists:

```python
list_a = [1, 3, 5, 7]
list_b = [2, 5, 8, 3]
```

Use a **nested loop** to find the **first** pair `(a, b)` where `a + b == 10`. Print the pair and break out of **both** loops.

**Hint:** Use a `found` flag variable to break out of the outer loop too.

```python
found = False
for a in list_a:
    for b in list_b:
        if ...:
            ...
            found = True
            break
    if found:
        break
```

**Expected output:**

```
Pair found: 5 + 5 = 10
```
