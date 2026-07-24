# Comprehensive Practice Problems

These problems combine **multiple concepts** you've learned: data structures, loops, functions, file I/O, and modularisation. Each problem requires you to use several skills together.

---

## Problem 1: Word Frequency Counter

Write a program that takes a string of text and returns a **dictionary** where each key is a word and each value is how many times it appears. Then print the top 3 most frequent words.

**Functions to write:**

1. `count_words(text)` — returns a dictionary of `{word: count}`.
2. `top_n(word_counts, n)` — returns a list of the `n` most frequent `(word, count)` tuples, sorted by count descending.

```python
text = "the cat sat on the mat the cat ate the rat on the mat"

counts = count_words(text)
print(counts)
print()

print("Top 3 words:")
for word, count in top_n(counts, 3):
    print(f"  '{word}' appeared {count} times")
```

**Expected output:**

```
{'the': 4, 'cat': 2, 'sat': 1, 'on': 2, 'mat': 2, 'ate': 1, 'rat': 1}

Top 3 words:
  'the' appeared 4 times
  'cat' appeared 2 times
  'on' appeared 2 times
```

**Concepts used:** strings, dictionaries, loops, functions, sorting with lambda, tuples.

**Hint:** Use `.split()` to break text into words. Use `sorted()` with a `key=lambda` to sort by count.

---

## Problem 2: Student Gradebook from File

Create a file called `grades.csv` with this content:

```
Alice,88,92,79
Bob,55,63,70
Charlie,95,98,100
Diana,72,68,65
Eve,85,90,88
```

Write a program that reads this file and produces a full report.

**Functions to write:**

1. `read_grades(filename)` — reads the CSV file and returns a **list of dictionaries** like:
   `[{"name": "Alice", "marks": [88, 92, 79]}, ...]`
2. `calculate_average(marks)` — returns the average of a list of marks.
3. `get_grade(average)` — returns a letter grade (A/B/C/D/F using the scale from earlier problems).
4. `class_statistics(students)` — returns a dictionary with `{"highest": name, "lowest": name, "class_average": avg}`.
5. `print_report(students)` — uses all the above to print a formatted report.

```python
students = read_grades("grades.csv")
print_report(students)
```

**Expected output:**

```
========== CLASS REPORT ==========
Name       Avg     Grade
----------------------------------
Alice      86.3    B
Bob        62.7    D
Charlie    97.7    A
Diana      68.3    D
Eve        87.7    B
----------------------------------
Class Average: 80.5
Highest: Charlie (97.7)
Lowest:  Bob (62.7)
==================================
```

**Concepts used:** file I/O, string methods (`.split()`, `.strip()`), lists, dictionaries, functions, loops, formatted output.

---

## Problem 3: Contact Book

Build an in-memory contact book using a **list of dictionaries**. Write functions that let you add, search, update, and delete contacts.

**Functions to write:**

1. `add_contact(contacts, name, phone, email)` — adds a new contact dict to the list. Return `False` if the name already exists.
2. `find_contact(contacts, name)` — returns the contact dict if found, or `None`.
3. `update_contact(contacts, name, **kwargs)` — updates any fields passed as keyword arguments. Return `False` if contact not found.
4. `delete_contact(contacts, name)` — removes the contact. Return `False` if not found.
5. `search_contacts(contacts, query)` — returns a list of contacts where the query appears in the name, phone, or email (case-insensitive).

```python
contacts = []

add_contact(contacts, "Alice", "555-1234", "alice@email.com")
add_contact(contacts, "Bob", "555-5678", "bob@email.com")
add_contact(contacts, "Alice Smith", "555-9999", "asmith@email.com")

print("--- All contacts ---")
for c in contacts:
    print(f"  {c['name']} | {c['phone']} | {c['email']}")

print()
print("--- Search 'alice' ---")
results = search_contacts(contacts, "alice")
for c in results:
    print(f"  {c['name']}")

print()
update_contact(contacts, "Bob", phone="555-0000", email="bob_new@email.com")
bob = find_contact(contacts, "Bob")
print(f"Updated Bob: {bob}")

print()
delete_contact(contacts, "Alice Smith")
print(f"After deletion: {len(contacts)} contacts remaining")
```

**Expected output:**

```
--- All contacts ---
  Alice | 555-1234 | alice@email.com
  Bob | 555-5678 | bob@email.com
  Alice Smith | 555-9999 | asmith@email.com

--- Search 'alice' ---
  Alice
  Alice Smith

Updated Bob: {'name': 'Bob', 'phone': '555-0000', 'email': 'bob_new@email.com'}

After deletion: 2 contacts remaining
```

**Concepts used:** lists, dictionaries, functions, `**kwargs`, loops, string methods (`.lower()`), conditionals.

---

## Problem 4: File-Based Todo List

Build a todo list manager that **persists data to a file** so tasks survive between program runs. The file `todos.txt` should have one task per line in the format: `status|task` (e.g., `done|Buy groceries`).

**Functions to write:**

1. `load_todos(filename)` — reads the file and returns a list of dicts like `[{"task": "Buy groceries", "done": True}, ...]`. If the file doesn't exist, return an empty list.
2. `save_todos(filename, todos)` — writes all todos back to the file.
3. `add_todo(todos, task)` — adds a new todo (not done yet) to the list.
4. `complete_todo(todos, task_text)` — marks a todo as done. Return `False` if not found.
5. `list_todos(todos)` — prints all todos with their status.
6. `pending_count(todos)` — returns how many todos are not yet done.

```python
todos = load_todos("todos.txt")

add_todo(todos, "Learn Python basics")
add_todo(todos, "Practice loops")
add_todo(todos, "Build a Flask app")

complete_todo(todos, "Learn Python basics")

print("--- My Todo List ---")
list_todos(todos)
print(f"\n{pending_count(todos)} tasks remaining")

save_todos("todos.txt", todos)

# Simulate restarting the program
print("\n--- Reloaded from file ---")
reloaded = load_todos("todos.txt")
list_todos(reloaded)
```

**Expected output:**

```
--- My Todo List ---
[x] Learn Python basics
[ ] Practice loops
[ ] Build a Flask app

2 tasks remaining

--- Reloaded from file ---
[x] Learn Python basics
[ ] Practice loops
[ ] Build a Flask app
```

**Concepts used:** file I/O (read, write), lists, dictionaries, functions, string methods, conditionals, loops.

---

## Problem 5: Matrix Operations

Write functions that work with matrices (2D lists — lists of lists).

**Functions to write:**

1. `create_matrix(rows, cols, fill=0)` — returns a matrix (list of lists) filled with `fill`.
2. `print_matrix(matrix)` — prints the matrix in a readable grid format.
3. `add_matrices(a, b)` — returns a new matrix that is the sum of `a` and `b`. Return `None` if dimensions don't match.
4. `transpose(matrix)` — returns a new matrix where rows become columns and columns become rows.
5. `multiply_matrices(a, b)` — returns the product of two matrices. Return `None` if dimensions are incompatible.

```python
a = [[1, 2, 3],
     [4, 5, 6]]

b = [[7, 8, 9],
     [1, 2, 3]]

print("Matrix A:")
print_matrix(a)

print("\nMatrix B:")
print_matrix(b)

print("\nA + B:")
print_matrix(add_matrices(a, b))

print("\nTranspose of A:")
print_matrix(transpose(a))

c = [[1, 2],
     [3, 4],
     [5, 6]]

print("\nA (2x3) * C (3x2):")
print_matrix(multiply_matrices(a, c))
```

**Expected output:**

```
Matrix A:
  1  2  3
  4  5  6

Matrix B:
  7  8  9
  1  2  3

A + B:
  8 10 12
  5  7  9

Transpose of A:
  1  4
  2  5
  3  6

A (2x3) * C (3x2):
  22  28
  49  64
```

**Concepts used:** nested lists, nested loops, functions, default parameters, list comprehensions, conditionals.

**Hint for multiply:** For matrix multiplication, the element at row `i`, column `j` of the result is the sum of `a[i][k] * b[k][j]` for all `k`.

---

## Problem 6: Data Pipeline

Build a data processing pipeline that reads raw sales data, cleans it, processes it, and writes a summary report.

Create a file called `sales.csv` with this content (note: some lines have bad data):

```
date,product,quantity,price
2024-01-15,Widget,10,4.99
2024-01-15,Gadget,5,9.99
2024-01-16,Widget,bad_data,4.99
2024-01-16,Doohickey,8,2.50
2024-01-17,Gadget,3,9.99
2024-01-17,Widget,7,4.99
2024-01-17,,5,3.00
2024-01-18,Doohickey,12,2.50
```

**Functions to write:**

1. `read_csv(filename)` — reads the CSV and returns a list of dictionaries (one per row), using the header row as keys.
2. `clean_data(records)` — filters out records with missing product names or non-numeric quantity/price. Returns a tuple: `(clean_records, skipped_count)`.
3. `sales_by_product(records)` — returns a dict of `{product: total_revenue}` where revenue = quantity * price.
4. `sales_by_date(records)` — returns a dict of `{date: total_revenue}`.
5. `write_report(filename, by_product, by_date, skipped)` — writes a formatted summary to a file.

```python
raw = read_csv("sales.csv")
clean, skipped = clean_data(raw)

by_product = sales_by_product(clean)
by_date = sales_by_date(clean)

write_report("sales_report.txt", by_product, by_date, skipped)

# Print the report to confirm
with open("sales_report.txt", "r") as f:
    print(f.read())
```

**Expected output (written to `sales_report.txt`):**

```
===== SALES REPORT =====

Sales by Product:
  Widget:     $84.83
  Gadget:     $79.92
  Doohickey:  $50.00

Sales by Date:
  2024-01-15: $99.85
  2024-01-16: $20.00
  2024-01-17: $64.90
  2024-01-18: $30.00

Skipped 2 invalid record(s).
Total Revenue: $214.75
========================
```

**Concepts used:** file I/O (read and write), dictionaries, lists, string methods, functions, loops, error handling, tuples, formatted output.

---

## Problem 7: Log File Analyzer

Write a program that analyzes a server log file. Create `server.log` with this content:

```
2024-01-15 10:23:15 INFO  User alice logged in
2024-01-15 10:24:01 ERROR Database connection failed
2024-01-15 10:25:30 INFO  User bob logged in
2024-01-15 10:26:45 WARNING Disk usage at 85%
2024-01-16 09:00:12 INFO  User alice logged in
2024-01-16 09:15:33 ERROR File not found: /data/report.csv
2024-01-16 09:20:00 INFO  User charlie logged in
2024-01-16 10:00:00 ERROR Database connection failed
2024-01-16 10:05:00 WARNING Memory usage high
2024-01-17 08:00:00 INFO  User alice logged in
2024-01-17 08:30:00 INFO  User bob logged in
2024-01-17 09:00:00 ERROR Timeout on API call
```

**Functions to write:**

1. `parse_log(filename)` — reads the log file and returns a list of dicts with keys: `date`, `time`, `level`, `message`.
2. `count_by_level(entries)` — returns a dict of `{level: count}` (e.g., `{"INFO": 6, "ERROR": 3, ...}`).
3. `filter_by_level(entries, level)` — returns only entries matching that level.
4. `errors_by_date(entries)` — returns a dict of `{date: [list of error messages]}`.
5. `unique_users(entries)` — extracts usernames from "User X logged in" messages and returns a **set** of unique users.
6. `print_summary(entries)` — uses all the above to print a summary report.

```python
entries = parse_log("server.log")
print_summary(entries)
```

**Expected output:**

```
===== LOG SUMMARY =====
Total entries: 12

By Level:
  INFO:    6
  ERROR:   3
  WARNING: 2

Errors by Date:
  2024-01-15:
    - Database connection failed
  2024-01-16:
    - File not found: /data/report.csv
    - Database connection failed
  2024-01-17:
    - Timeout on API call

Unique Users: alice, bob, charlie
=======================
```

**Concepts used:** file I/O, string methods (`.split()`, `.startswith()`), dictionaries, lists, sets, functions, loops, conditionals, formatted output.

---

## Problem 8: Inventory Manager

Build an inventory management system that tracks products, stock levels, and generates alerts.

**Functions to write:**

1. `create_inventory()` — returns an empty inventory (a dictionary).
2. `add_product(inventory, name, price, quantity)` — adds a product. Return `False` if it already exists.
3. `restock(inventory, name, quantity)` — increases the stock of an existing product. Return `False` if product not found.
4. `sell(inventory, name, quantity)` — decreases the stock. Return `False` if product not found or not enough stock.
5. `get_low_stock(inventory, threshold=5)` — returns a list of `(name, quantity)` tuples for products at or below the threshold.
6. `inventory_value(inventory)` — returns the total value of all stock (price * quantity for each product).
7. `print_inventory(inventory)` — prints a formatted inventory table.

```python
inv = create_inventory()

add_product(inv, "Laptop", 999.99, 10)
add_product(inv, "Mouse", 29.99, 50)
add_product(inv, "Keyboard", 59.99, 25)
add_product(inv, "Monitor", 399.99, 3)
add_product(inv, "USB Cable", 9.99, 100)

sell(inv, "Laptop", 7)
sell(inv, "Mouse", 48)
sell(inv, "Monitor", 2)

print("--- Current Inventory ---")
print_inventory(inv)

print("\n--- Low Stock Alert ---")
low = get_low_stock(inv)
for name, qty in low:
    print(f"  WARNING: {name} only has {qty} left!")

print(f"\nTotal inventory value: ${inventory_value(inv):.2f}")
```

**Expected output:**

```
--- Current Inventory ---
Product      Price      Stock
------------------------------
Laptop       $999.99    3
Mouse        $29.99     2
Keyboard     $59.99     25
Monitor      $399.99    1
USB Cable    $9.99      100

--- Low Stock Alert ---
  WARNING: Laptop only has 3 left!
  WARNING: Mouse only has 2 left!
  WARNING: Monitor only has 1 left!

Total inventory value: $5489.67
```

**Concepts used:** dictionaries, functions, default parameters, loops, conditionals, tuples, formatted output.

---

## Bonus Problem: Mini Database

Build a simple in-memory database that supports creating tables, inserting rows, querying with filters, and saving/loading from a file.

**Functions to write:**

1. `create_table(db, table_name, columns)` — creates a new table in the database. `db` is a dictionary, `columns` is a list of column names.
2. `insert(db, table_name, row)` — inserts a row (dict) into the table. Validate that the row has the correct columns.
3. `select(db, table_name, where=None)` — returns all rows, or only rows matching the `where` function (a filter function like those used with `filter()`).
4. `update(db, table_name, where, **changes)` — updates rows matching the `where` function with the given changes.
5. `delete(db, table_name, where)` — removes rows matching the `where` function.
6. `save_db(db, filename)` — writes the database to a file (pick any format you like).
7. `load_db(filename)` — reads the database back from the file.

```python
db = {}

create_table(db, "users", ["name", "age", "city"])

insert(db, "users", {"name": "Alice", "age": 30, "city": "NYC"})
insert(db, "users", {"name": "Bob", "age": 25, "city": "LA"})
insert(db, "users", {"name": "Charlie", "age": 35, "city": "NYC"})
insert(db, "users", {"name": "Diana", "age": 28, "city": "LA"})

print("All users:")
for row in select(db, "users"):
    print(f"  {row}")

print("\nUsers in NYC:")
for row in select(db, "users", where=lambda r: r["city"] == "NYC"):
    print(f"  {row}")

print("\nUsers over 27:")
for row in select(db, "users", where=lambda r: r["age"] > 27):
    print(f"  {row}")

update(db, "users", where=lambda r: r["name"] == "Bob", age=26)
bob = select(db, "users", where=lambda r: r["name"] == "Bob")
print(f"\nUpdated Bob: {bob[0]}")

delete(db, "users", where=lambda r: r["city"] == "LA")
print(f"\nAfter deleting LA users: {len(select(db, 'users'))} remaining")

save_db(db, "mydb.txt")
loaded = load_db("mydb.txt")
print(f"\nLoaded from file: {len(select(loaded, 'users'))} users")
```

**Expected output:**

```
All users:
  {'name': 'Alice', 'age': 30, 'city': 'NYC'}
  {'name': 'Bob', 'age': 25, 'city': 'LA'}
  {'name': 'Charlie', 'age': 35, 'city': 'NYC'}
  {'name': 'Diana', 'age': 28, 'city': 'LA'}

Users in NYC:
  {'name': 'Alice', 'age': 30, 'city': 'NYC'}
  {'name': 'Charlie', 'age': 35, 'city': 'NYC'}

Users over 27:
  {'name': 'Alice', 'age': 30, 'city': 'NYC'}
  {'name': 'Charlie', 'age': 35, 'city': 'NYC'}
  {'name': 'Diana', 'age': 28, 'city': 'LA'}

Updated Bob: {'name': 'Bob', 'age': 26, 'city': 'LA'}

After deleting LA users: 2 remaining

Loaded from file: 2 users
```

**Concepts used:** dictionaries (nested), lists, functions, `**kwargs`, lambda functions, file I/O, loops, conditionals, modularisation, default parameters.
