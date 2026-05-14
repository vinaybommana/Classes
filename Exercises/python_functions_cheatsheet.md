# Python Functions Cheatsheet

---

## 1. Basic Function

A **function** is a reusable block of code that performs a specific task. You define it once and call it whenever you need it.

### Defining and Calling

```python
def say_hello():
    print("Hello!")

say_hello()        # Hello!
say_hello()        # Hello!
```

### Key Points

- Use `def` keyword followed by the function name and parentheses `()`.
- The function body is **indented** (4 spaces).
- A function does nothing until you **call** it with `()`.

---

## 2. Parameters and Arguments

**Parameters** are the variables listed in the function definition. **Arguments** are the actual values you pass when calling the function.

### Syntax

```python
def greet(name):          # 'name' is a parameter
    print(f"Hi, {name}!")

greet("Alice")            # "Alice" is an argument
```

### Multiple Parameters

```python
def add(a, b):
    return a + b

result = add(3, 5)       # result = 8
```

### Key Points

- Parameters are **placeholders** in the definition.
- Arguments are **actual values** passed during the call.
- The number of arguments must match the number of parameters (unless defaults are used).

---

## 3. Return Values

The `return` keyword sends a value **back to the caller**. Without `return`, a function returns `None` by default.

### return vs print

| | `return` | `print` |
|---|---|---|
| **Purpose** | Sends value back to caller | Displays text on screen |
| **Can store result?** | Yes: `x = func()` | No: `x = None` |
| **Can use result later?** | Yes | No |

### Examples

```python
def square(n):
    return n * n

result = square(4)       # result = 16
print(result + 10)       # 26

def square_print(n):
    print(n * n)

result = square_print(4) # prints 16, but result = None
```

### Returning Multiple Values

```python
def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder    # returns a tuple

q, r = divide(17, 5)             # q = 3, r = 2
```

### Key Points

- A function **stops executing** as soon as it hits a `return` statement.
- You can return **any type**: numbers, strings, lists, dictionaries, tuples.
- Returning multiple values creates a **tuple** that you can unpack.

---

## 4. Default Parameters

You can give parameters **default values**. If the caller doesn't provide that argument, the default is used.

### Syntax

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")                # Hello, Alice!
greet("Bob", "Good morning")  # Good morning, Bob!
```

### Rules

| Rule | Example | Valid? |
|---|---|---|
| Defaults come **after** non-defaults | `def f(a, b=10)` | Yes |
| Non-default after default | `def f(a=10, b)` | No (SyntaxError) |
| Multiple defaults | `def f(a, b=10, c=20)` | Yes |

### Key Points

- Default parameters make arguments **optional**.
- Parameters with defaults must come **after** parameters without defaults.
- Default values are evaluated **once** when the function is defined — avoid using mutable defaults like `[]` or `{}`.

---

## 5. Keyword Arguments

When calling a function, you can pass arguments **by name** instead of by position.

### Positional vs Keyword

```python
def describe(name, age, city):
    print(f"{name}, age {age}, from {city}")

# Positional — order matters
describe("Alice", 30, "NYC")

# Keyword — order doesn't matter
describe(city="NYC", name="Alice", age=30)

# Mixed — positional first, then keyword
describe("Alice", city="NYC", age=30)
```

### Key Points

- Keyword arguments let you pass arguments **in any order**.
- You can mix positional and keyword, but **positional must come first**.
- Keyword arguments make function calls more **readable**.

---

## 6. *args (Variable Positional Arguments)

Use `*args` to accept **any number** of positional arguments. Inside the function, `args` is a **tuple**.

### Syntax

```python
def add_all(*args):
    total = 0
    for num in args:
        total += num
    return total

add_all(1, 2, 3)        # 6
add_all(10, 20)          # 30
add_all()                # 0
```

### Combining with Regular Parameters

```python
def greet(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

greet("Hello", "Alice", "Bob", "Charlie")
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!
```

### Key Points

- `*args` collects extra positional arguments into a **tuple**.
- The name `args` is a convention — you can use any name like `*numbers`.
- Regular parameters must come **before** `*args`.

---

## 7. **kwargs (Variable Keyword Arguments)

Use `**kwargs` to accept **any number** of keyword arguments. Inside the function, `kwargs` is a **dictionary**.

### Syntax

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="NYC")
# name: Alice
# age: 30
# city: NYC
```

### Combining Everything

```python
def func(a, b=10, *args, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")

func(1, 2, 3, 4, x=100, y=200)
# a=1, b=2
# args=(3, 4)
# kwargs={'x': 100, 'y': 200}
```

### Parameter Order

| Position | Type | Example |
|---|---|---|
| 1st | Regular parameters | `a, b` |
| 2nd | Default parameters | `c=10` |
| 3rd | `*args` | `*args` |
| 4th | `**kwargs` | `**kwargs` |

---

## 8. Scope — Local vs Global

Variables defined **inside** a function are **local** — they exist only within that function. Variables defined **outside** are **global**.

### Example

```python
x = 10                  # global variable

def my_func():
    x = 20              # local variable (different from global x)
    print(x)            # 20

my_func()
print(x)                # 10 (global x unchanged)
```

### The `global` Keyword

```python
count = 0

def increment():
    global count        # refers to the global variable
    count += 1

increment()
print(count)            # 1
```

### Key Points

- Local variables are **created when the function runs** and **destroyed when it ends**.
- A function **can read** global variables but **cannot modify** them without `global`.
- Avoid using `global` when possible — pass values as parameters and return results instead.

---

## 9. Lambda Functions

A **lambda** is a small anonymous function written in one line. It can take any number of arguments but has only **one expression**.

### Syntax

```python
# Regular function
def square(x):
    return x * x

# Lambda equivalent
square = lambda x: x * x

print(square(5))        # 25
```

### Common Uses

| Function | What it does | Example |
|---|---|---|
| `sorted()` | Sort with custom key | `sorted(items, key=lambda x: x[1])` |
| `filter()` | Keep items matching condition | `list(filter(lambda x: x > 0, nums))` |
| `map()` | Transform each item | `list(map(lambda x: x * 2, nums))` |

### Examples

```python
# Sort by second element
pairs = [(1, 'b'), (2, 'a'), (3, 'c')]
sorted(pairs, key=lambda x: x[1])    # [(2, 'a'), (1, 'b'), (3, 'c')]

# Filter even numbers
nums = [1, 2, 3, 4, 5, 6]
list(filter(lambda x: x % 2 == 0, nums))   # [2, 4, 6]

# Double each number
list(map(lambda x: x * 2, nums))           # [2, 4, 6, 8, 10, 12]
```

### Key Points

- Lambdas are best for **short, simple operations** — use regular `def` for anything complex.
- A lambda **always returns** the result of its expression (no `return` keyword needed).
- Lambdas are most useful when passed to `sorted()`, `filter()`, and `map()`.

---

## 10. Recursion

A **recursive** function is a function that **calls itself**. Every recursive function needs a **base case** to stop the recursion.

### Example — Factorial

```python
def factorial(n):
    if n <= 1:           # base case
        return 1
    return n * factorial(n - 1)   # recursive case

factorial(5)   # 5 * 4 * 3 * 2 * 1 = 120
```

### How It Works

```
factorial(5)
  → 5 * factorial(4)
    → 4 * factorial(3)
      → 3 * factorial(2)
        → 2 * factorial(1)
          → 1              (base case)
        → 2 * 1 = 2
      → 3 * 2 = 6
    → 4 * 6 = 24
  → 5 * 24 = 120
```

### Key Points

- Every recursion needs a **base case** — otherwise it runs forever (and crashes with `RecursionError`).
- Python has a default **recursion limit of 1000** calls.
- Recursion is elegant for problems like tree traversal, nested structures, and divide-and-conquer algorithms.

---

## Quick Reference

| Concept | Syntax | Example |
|---|---|---|
| Define a function | `def name():` | `def greet(): print("Hi")` |
| Parameters | `def name(param):` | `def greet(name): ...` |
| Return a value | `return value` | `return x + y` |
| Default parameter | `param=default` | `def f(x, y=10): ...` |
| Keyword arguments | `name=value` | `f(x=1, y=2)` |
| Variable positional | `*args` | `def f(*args): ...` |
| Variable keyword | `**kwargs` | `def f(**kwargs): ...` |
| Lambda | `lambda params: expr` | `lambda x: x * 2` |
| Recursion | Function calls itself | `def f(n): return f(n-1)` |
| Scope | Local vs Global | `global x` to modify global |
