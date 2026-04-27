# File Operations Practice Problems

---

## Problem 1: Write a Greeting

Write a program that creates a file called `greeting.txt` and writes the following three lines to it:

```
Hello, World!
Welcome to Python.
File operations are fun!
```

After writing, open the file again and **read** the entire contents, then print them.

**Hint:** Use `open("greeting.txt", "w")` to write and `open("greeting.txt", "r")` to read. Always use the `with` statement so the file is closed automatically.

```python
with open("greeting.txt", "w") as f:
    # write lines here

with open("greeting.txt", "r") as f:
    # read and print here
```

**Expected output:**

```
Hello, World!
Welcome to Python.
File operations are fun!
```

---

## Problem 2: Count Lines, Words, and Characters

Create a file called `sample.txt` with the following content (copy-paste or write it with code):

```
The quick brown fox
jumps over the lazy dog
Python is awesome
```

Then write a program that opens `sample.txt` and prints:

- The number of **lines**
- The total number of **words**
- The total number of **characters** (including spaces and newlines)

**Hint:** `f.readlines()` returns a list of lines. You can use `split()` on each line to count words.

**Expected output:**

```
Lines: 3
Words: 13
Characters: 53
```

---

## Problem 3: Append to a File

Start with the file `greeting.txt` from Problem 1. Write a program that **appends** two new lines to the file without erasing the existing content:

```
This line was appended.
So was this one!
```

Then read the full file and print it.

**Hint:** Use `"a"` mode instead of `"w"` mode. `"w"` erases the file, `"a"` adds to the end.

**Expected output:**

```
Hello, World!
Welcome to Python.
File operations are fun!
This line was appended.
So was this one!
```

---

## Problem 4: Number Each Line

Given a file called `poem.txt` with this content:

```
Roses are red
Violets are blue
Python is great
And so are you
```

Write a program that reads `poem.txt` and creates a new file called `poem_numbered.txt` where each line is prefixed with its line number.

**Hint:** Use `enumerate()` to get both the index and the line while looping.

**Expected output in `poem_numbered.txt`:**

```
1: Roses are red
2: Violets are blue
3: Python is great
4: And so are you
```

---

## Problem 5: Filter Lines

Given a file called `words.txt` with this content:

```
apple
hi
banana
go
strawberry
ok
watermelon
no
```

Write a program that reads `words.txt` and writes only the words that are **5 or more characters long** to a new file called `long_words.txt`.

**Expected output in `long_words.txt`:**

```
apple
banana
strawberry
watermelon
```

---

## Problem 6: Student Scores to CSV

Given this dictionary:

```python
students = {
    "Alice": 92,
    "Bob": 67,
    "Charlie": 85,
    "Diana": 45,
    "Eve": 73
}
```

Write a program that saves this data to a file called `scores.csv` in comma-separated format with a header row.

**Expected content of `scores.csv`:**

```
Name,Score
Alice,92
Bob,67
Charlie,85
Diana,45
Eve,73
```

---

## Problem 7: Read a CSV and Calculate Average

Using the `scores.csv` file from Problem 6, write a program that:

1. Reads the file
2. Skips the header line
3. Calculates the **average score**
4. Prints each student's name, score, and whether they are above or below average

**Hint:** Use `split(",")` to separate each line into name and score. Remember to convert the score to an `int`.

**Expected output:**

```
Average score: 72.4
Alice: 92 (above average)
Bob: 67 (below average)
Charlie: 85 (above average)
Diana: 45 (below average)
Eve: 73 (above average)
```

---

## Problem 8: Find and Replace

Write a program that reads a file called `story.txt` with this content:

```
The cat sat on the mat.
The cat ate the food.
The cat slept all day.
```

Replace every occurrence of `"cat"` with `"dog"` and write the result to a new file called `story_updated.txt`.

**Hint:** Use the `.replace()` string method.

**Expected content of `story_updated.txt`:**

```
The dog sat on the mat.
The dog ate the food.
The dog slept all day.
```

---

## Problem 9: Merge Two Files

Given two files:

**`file_a.txt`:**
```
Line 1 from file A
Line 2 from file A
Line 3 from file A
```

**`file_b.txt`:**
```
Line 1 from file B
Line 2 from file B
```

Write a program that reads both files and writes their combined content into `merged.txt`, with file A's content first, then a blank line, then file B's content.

**Expected content of `merged.txt`:**

```
Line 1 from file A
Line 2 from file A
Line 3 from file A

Line 1 from file B
Line 2 from file B
```

---

## Problem 10: Log File Analyzer

Write a program that creates a log file called `app.log` with the following content:

```
INFO: Application started
WARNING: Low memory
INFO: User logged in
ERROR: Database connection failed
INFO: Data loaded
WARNING: Slow response time
ERROR: Timeout occurred
INFO: Application stopped
```

Then write a program that reads `app.log` and:

1. Counts how many `INFO`, `WARNING`, and `ERROR` messages there are
2. Writes only the `ERROR` lines to a new file called `errors.txt`

**Expected printed output:**

```
INFO: 4
WARNING: 2
ERROR: 2
```

**Expected content of `errors.txt`:**

```
ERROR: Database connection failed
ERROR: Timeout occurred
```

**Hint:** Use `.startswith()` to check what each line begins with.

---

## Bonus Problem: File Exists Check

Write a program that asks for a filename and checks whether that file exists. If it does, print how many lines it has. If it doesn't, print a message saying the file was not found.

**Hint:** Use the `os.path.exists()` function. You need to `import os` first.

```python
import os

filename = input("Enter a filename: ")
if os.path.exists(filename):
    # open and count lines
else:
    print(f"{filename} was not found.")
```

**Example runs:**

```
Enter a filename: greeting.txt
greeting.txt has 3 lines.
```

```
Enter a filename: missing.txt
missing.txt was not found.
```
