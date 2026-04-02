# Loop + Conditional Practice Problems

---

## Problem 1: FizzBuzz

Loop through the numbers 1 to 30.

- If a number is divisible by both 3 **and** 5, print `"FizzBuzz"`
- Else if divisible by 3, print `"Fizz"`
- Else if divisible by 5, print `"Buzz"`
- Otherwise, print the number itself

**Hint:** use the modulo operator `%` to check divisibility. `15 % 3 == 0` means 15 is divisible by 3.

---

## Problem 2: Sum of Even Numbers

Given this list:

```python
numbers = [1, 2, 7, 8, 13, 14, 19, 20]
```

Use a loop to calculate the sum of only the **even** numbers. Print the final sum.

**Expected output:** `44` (2 + 8 + 14 + 20)

---

## Problem 3: Password Validator

Given this list of passwords:

```python
passwords = ["hello", "p@ssw0rd!", "abc", "securePass123", "hi"]
```

Loop through each one and print whether it is `"valid"` or `"too short"`. A password is valid if it has **8 or more** characters.

**Expected output:**

```
hello -> too short
p@ssw0rd! -> valid
abc -> too short
securePass123 -> valid
hi -> too short
```

---

## Problem 4: Find the First Negative Number

Given this list:

```python
numbers = [10, 25, 7, -4, 15, -2, 8]
```

Use a **while loop** to iterate through the list. Stop as soon as you find a negative number and print:

```
First negative number is -4 at index 3
```

If there are no negative numbers, print `"No negative numbers found"`.

---

## Problem 5: Counting Vowels

Given this string:

```python
sentence = "The quick brown fox jumps over the lazy dog"
```

Use a loop to count how many **vowels** (a, e, i, o, u) are in the sentence. Ignore case (uppercase and lowercase both count).

**Expected output:** `11`

**Hint:** you can use the `in` keyword to check if a character is in a string of vowels, e.g. `if char in "aeiou"`

---

## Problem 6: Multiplication Table Filter

Print a multiplication table for the numbers 1 through 5, but **only** print products that are greater than 10.

Use a **nested for loop** (a loop inside a loop).

**Expected output:**

```
3 x 4 = 12
3 x 5 = 15
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
```

---

## Problem 7: Number Guessing Countdown

A user gets 5 attempts to guess a secret number. Use a **while loop** that counts down the remaining attempts. For each guess in the list, print whether it is `"too low"`, `"too high"`, or `"correct!"`. If the guess is correct, stop the loop early.

```python
secret = 42
guesses = [20, 55, 38, 42, 60]
```

**Expected output:**

```
Attempt 1: 20 is too low (4 attempts left)
Attempt 2: 55 is too high (3 attempts left)
Attempt 3: 38 is too low (2 attempts left)
Attempt 4: 42 is correct!
```

---

## Problem 8: Grade Classifier

Given this dictionary of student scores:

```python
scores = {"Alice": 92, "Bob": 67, "Charlie": 85, "Diana": 45, "Eve": 73}
```

Loop through each student and print their name along with a letter grade:

- 90 and above: `A`
- 80–89: `B`
- 70–79: `C`
- 60–69: `D`
- Below 60: `F`

**Expected output:**

```
Alice: A
Bob: D
Charlie: B
Diana: F
Eve: C
```
