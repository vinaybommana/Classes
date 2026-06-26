# Functions: Scope of Variables Inside and Outside Functions

In Python, **where** you create a variable determines **where** you can use it. This is called **scope**.

- **Local scope** — variables created inside a function. They exist only while the function runs, and cannot be accessed outside it.
- **Global scope** — variables created outside all functions. They can be read inside functions, but **cannot be modified** inside a function unless you use the `global` keyword.
- **The `global` keyword** — lets a function modify a variable that lives in the global scope.

---

## Problem 1: Local vs Global — The Counter

**Read the code below carefully, then answer the questions without running it.**

```python
count = 0

def increment():
    count = count + 1
    print(f"Inside function: count = {count}")

increment()
print(f"Outside function: count = {count}")
```

### Part A: Predict the output

What happens when you run this code? Does it print both lines, or does it crash? If it crashes, what error do you get and why?

### Part B: Fix with `global`

Fix the function so that it **actually modifies** the global `count` variable. After fixing, running this:

```python
count = 0

increment()
increment()
increment()

print(f"Final count: {count}")
```

should produce:

```
Inside function: count = 1
Inside function: count = 2
Inside function: count = 3
Final count: 3
```

### Part C: Fix without `global`

Now rewrite `increment` so it does **not** use the `global` keyword at all. Instead, it should **take** the current count as a parameter, and **return** the new count. The caller is responsible for updating the variable.

```python
count = 0

count = increment(count)
count = increment(count)
count = increment(count)

print(f"Final count: {count}")
```

should produce the same output as Part B.

**Key lesson:**
- Part A shows that Python treats `count` inside the function as a **new local variable** — and since you're reading it before assigning, you get an `UnboundLocalError`.
- Part B works but creates a hidden dependency between the function and the outside world.
- Part C is the cleanest approach — the function is self-contained, takes input, returns output, and doesn't depend on anything outside itself.

---

## Problem 2: The Scoreboard

**Read the code below and predict the output of each `print` statement.** Then run it to check.

```python
player = "Alice"
score = 100

def award_bonus(bonus_points):
    score = bonus_points * 2
    player = "Bob"
    print(f"1. Inside award_bonus: player={player}, score={score}")

def show_score():
    print(f"2. Inside show_score: player={player}, score={score}")

def reset_score():
    global score
    score = 0
    print(f"3. Inside reset_score: score={score}")

award_bonus(50)
print(f"4. After award_bonus: player={player}, score={score}")

show_score()

reset_score()
print(f"6. After reset_score: player={player}, score={score}")
```

### Questions

Write down what each numbered print statement outputs, then verify by running the code.

**Expected output:**

```
1. Inside award_bonus: player=Bob, score=100
2. Inside show_score: player=Alice, score=100
3. Inside reset_score: score=0
4. After award_bonus: player=Alice, score=100
5. Inside show_score: player=Alice, score=100
6. After reset_score: player=Alice, score=0
```

Wait — `award_bonus` set `score = 100` and `player = "Bob"`, so why didn't the global values change?

**Answer each of these:**

1. Why does print #1 show `score=100` when `bonus_points` is 50 and we wrote `score = bonus_points * 2`?
2. Why does print #4 still show `player=Alice` even though we set `player = "Bob"` inside `award_bonus`?
3. Why does `reset_score` actually change the global `score` but `award_bonus` does not?
4. If you wanted `award_bonus` to update the global score **without** using `global`, how would you rewrite it?

**Key lesson:**
- A function can **read** a global variable freely (like `show_score` reads `player` and `score`).
- But the moment you **assign** to a variable inside a function, Python creates a **local** copy — the global is untouched.
- `global` overrides this, but using parameters and return values is usually better.

---

## Problem 3: The Shopping List

This problem has three parts. Each part builds on the previous one.

### Part A: Spot the bug

```python
shopping_list = ["milk", "eggs", "bread"]

def add_item(item):
    shopping_list.append(item)

def clear_list():
    shopping_list = []

add_item("butter")
print(shopping_list)

clear_list()
print(shopping_list)
```

**Predict the output**, then run it.

**Expected output:**

```
['milk', 'eggs', 'bread', 'butter']
['milk', 'eggs', 'bread', 'butter']
```

Why did `add_item` successfully modify the list, but `clear_list` did not?

**Hint:** `append` **mutates** the existing list object (no assignment, so no new local variable is created). But `shopping_list = []` is an **assignment**, which creates a new local variable that shadows the global one.

### Part B: Fix `clear_list` — two ways

Fix `clear_list` so it actually empties the global list. Do it **two different ways**:

1. Using the `global` keyword.
2. Without `global` — use a list method that clears the list **in place** (look up `list.clear()`).

After fixing, this code:

```python
shopping_list = ["milk", "eggs", "bread"]

add_item("butter")
print(f"After adding: {shopping_list}")

clear_list()
print(f"After clearing: {shopping_list}")
```

should produce:

```
After adding: ['milk', 'eggs', 'bread', 'butter']
After clearing: []
```

### Part C: Make it self-contained

Rewrite the entire program so that **no function relies on global variables**. Each function should receive the list as a parameter and return the updated list.

```python
my_list = ["milk", "eggs", "bread"]

my_list = add_item(my_list, "butter")
print(f"After adding: {my_list}")

my_list = clear_list(my_list)
print(f"After clearing: {my_list}")

my_list = add_item(my_list, "juice")
my_list = add_item(my_list, "cheese")
print(f"After adding more: {my_list}")
```

**Expected output:**

```
After adding: ['milk', 'eggs', 'bread', 'butter']
After clearing: []
After adding more: ['juice', 'cheese']
```

**Key lesson:**
- **Mutable objects** (lists, dictionaries) can be modified inside a function without `global` — as long as you **mutate** them (`.append()`, `.clear()`) rather than **reassign** them (`=`).
- This is the difference between changing what's **inside** the box vs. replacing the **entire box** with a new one.
- The safest pattern is Part C: pass data in, return data out. The function doesn't need to know or care about variables outside itself.

---

## Summary

| Concept | Rule |
|---|---|
| **Local variable** | Created inside a function. Dies when the function ends. |
| **Global variable** | Created outside all functions. Visible everywhere. |
| **Reading** a global inside a function | Works automatically. |
| **Assigning** to a variable inside a function | Creates a **new local** variable — does not touch the global. |
| **`global` keyword** | Tells Python "I mean the global one, not a new local one." |
| **Mutating** a global list/dict inside a function | Works without `global` (e.g., `.append()`, `.clear()`). |
| **Best practice** | Pass values in as parameters, return results out. Avoid `global` when possible. |
