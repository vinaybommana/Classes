# Functions: Modularising Problems into Chunks of Code

The key idea: instead of writing one long block of code, **break the problem into smaller functions**, each doing one job. Then combine them to solve the bigger problem.

---

## Problem 1: Student Report Card

You have a list of students and their marks in three subjects. Build a **report card generator** by writing these functions:

1. `calculate_average(marks)` — takes a list of marks and returns the average.
2. `get_grade(average)` — takes an average and returns a letter grade:
   - 90 and above → `"A"`
   - 80–89 → `"B"`
   - 70–79 → `"C"`
   - 60–69 → `"D"`
   - Below 60 → `"F"`
3. `print_report(name, marks)` — takes a student name and their marks, then **uses the two functions above** to print a formatted report line.

```python
students = {
    "Alice": [88, 92, 79],
    "Bob": [55, 63, 70],
    "Charlie": [95, 98, 100],
    "Diana": [72, 68, 65]
}

print("--- Student Report Card ---")
for name, marks in students.items():
    print_report(name, marks)
```

**Expected output:**

```
--- Student Report Card ---
Alice  | Average: 86.3 | Grade: B
Bob    | Average: 62.7 | Grade: D
Charlie | Average: 97.7 | Grade: A
Diana  | Average: 68.3 | Grade: D
```

**Why modularise?**
- `calculate_average` can be reused anywhere you need an average — not just for grades.
- `get_grade` contains the grading logic in one place — if the scale changes, you fix it in one spot.
- `print_report` orchestrates the other two — it doesn't need to know *how* the average is calculated or *how* grades are assigned.

---

## Problem 2: Shopping Cart

Build a simple shopping cart checkout system using these functions:

1. `calculate_subtotal(cart)` — takes a list of `(item_name, price, quantity)` tuples and returns the subtotal (sum of price * quantity for each item).
2. `apply_discount(subtotal, discount_percent)` — returns the price after applying the discount. If `discount_percent` is 0, return the subtotal unchanged.
3. `calculate_tax(amount, tax_rate)` — returns the tax amount (not the total).
4. `print_receipt(cart, discount_percent, tax_rate)` — uses all three functions above to print a full receipt.

```python
cart = [
    ("Notebook", 5.99, 3),
    ("Pen", 1.50, 10),
    ("Backpack", 29.99, 1)
]

print_receipt(cart, discount_percent=10, tax_rate=8.5)
```

**Expected output:**

```
--- Receipt ---
Notebook   x3   $17.97
Pen        x10  $15.00
Backpack   x1   $29.99
---------------------
Subtotal:        $62.96
Discount (10%):  -$6.30
After Discount:  $56.66
Tax (8.5%):      $4.82
---------------------
Total:           $61.48
```

(Round all money values to 2 decimal places.)

**Why modularise?**
- Each function handles **one responsibility**. The discount logic doesn't know about tax. The tax logic doesn't know about items.
- You could swap `apply_discount` for a coupon-based system without touching the rest.
- `print_receipt` reads like a recipe: get subtotal, apply discount, calculate tax, print — easy to follow.

---

## Problem 3: Password Validator

Build a password strength checker by writing these functions:

1. `has_minimum_length(password, min_length=8)` — returns `True` if the password is at least `min_length` characters long.
2. `has_uppercase(password)` — returns `True` if the password contains at least one uppercase letter.
3. `has_digit(password)` — returns `True` if the password contains at least one digit.
4. `has_special_char(password)` — returns `True` if the password contains at least one special character from `!@#$%^&*`.
5. `validate_password(password)` — uses **all four functions above** to check the password. Returns a tuple: `(is_valid, list_of_failures)` where `is_valid` is `True` only if all checks pass, and `list_of_failures` contains messages for each failed check.

```python
passwords = ["hello", "Hello123", "H3llo!", "Ab1!xyzw"]

for pw in passwords:
    is_valid, failures = validate_password(pw)
    if is_valid:
        print(f"'{pw}' -> STRONG")
    else:
        print(f"'{pw}' -> WEAK: {', '.join(failures)}")
```

**Expected output:**

```
'hello' -> WEAK: Too short, No uppercase, No digit, No special character
'Hello123' -> WEAK: No special character
'H3llo!' -> WEAK: Too short
'Ab1!xyzw' -> STRONG
```

**Why modularise?**
- Each check is its own function — easy to test individually. You can verify `has_digit` works without running the whole validator.
- Adding a new rule (e.g., "no spaces allowed") means writing **one new function** and adding one line to `validate_password` — nothing else changes.
- The main `validate_password` function reads like a checklist, making the logic clear at a glance.

---

## Key Takeaway

In all three problems, notice the pattern:
1. **Small functions** that each do one thing.
2. **A main function** that calls the smaller ones to solve the bigger problem.
3. Each function can be **tested, reused, and changed independently**.

This is what modularisation means — splitting a problem into manageable chunks so your code is easier to read, debug, and extend.
