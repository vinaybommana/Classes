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
