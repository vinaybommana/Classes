# Python Data Structures Cheatsheet

---

## 1. Strings

A **string** is an ordered, immutable sequence of characters. Strings are enclosed in single quotes (`'...'`) or double quotes (`"..."`).

### Creating Strings

```python
empty = ""
greeting = "hello"
multiline = """this is
a multiline string"""
```

### Common Operations

| Operation | Example | Result |
|---|---|---|
| Length | `len("hello")` | `5` |
| Access by index | `"hello"[1]` | `"e"` |
| Slicing | `"hello"[1:4]` | `"ell"` |
| Concatenation | `"hi" + " there"` | `"hi there"` |
| Repetition | `"ha" * 3` | `"hahaha"` |
| Membership | `"ell" in "hello"` | `True` |

### Common Methods

| Method | Description | Example | Result |
|---|---|---|---|
| `.upper()` | Converts to uppercase | `"hello".upper()` | `"HELLO"` |
| `.lower()` | Converts to lowercase | `"HELLO".lower()` | `"hello"` |
| `.strip()` | Removes leading/trailing whitespace | `"  hi  ".strip()` | `"hi"` |
| `.split(sep)` | Splits into a list | `"a,b,c".split(",")` | `["a", "b", "c"]` |
| `.join(list)` | Joins a list into a string | `"-".join(["a","b"])` | `"a-b"` |
| `.replace(old, new)` | Replaces substrings | `"hello".replace("l","r")` | `"herro"` |
| `.find(sub)` | Returns index of substring, or -1 | `"hello".find("ll")` | `2` |
| `.count(sub)` | Counts occurrences | `"hello".count("l")` | `2` |
| `.startswith(s)` | Checks prefix | `"hello".startswith("he")` | `True` |
| `.endswith(s)` | Checks suffix | `"hello".endswith("lo")` | `True` |

### Key Points

- Strings are **immutable** — you cannot change a character in place. Methods like `.upper()` return a **new** string.
- Use f-strings for formatting: `f"Hello, {name}!"`

---

## 2. Lists

A **list** is an ordered, mutable collection that can hold items of any type. Lists are enclosed in square brackets (`[...]`).

### Creating Lists

```python
empty = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]
from_range = list(range(5))       # [0, 1, 2, 3, 4]
```

### Common Operations

| Operation | Example | Result |
|---|---|---|
| Length | `len([1, 2, 3])` | `3` |
| Access by index | `[10, 20, 30][1]` | `20` |
| Slicing | `[10, 20, 30, 40][1:3]` | `[20, 30]` |
| Concatenation | `[1, 2] + [3, 4]` | `[1, 2, 3, 4]` |
| Repetition | `[0] * 3` | `[0, 0, 0]` |
| Membership | `3 in [1, 2, 3]` | `True` |

### Common Methods

| Method | Description | Example |
|---|---|---|
| `.append(x)` | Adds item to the end | `nums.append(4)` |
| `.insert(i, x)` | Inserts item at index i | `nums.insert(0, 99)` |
| `.remove(x)` | Removes first occurrence of x | `nums.remove(3)` |
| `.pop(i)` | Removes and returns item at index i (default: last) | `nums.pop()` |
| `.sort()` | Sorts the list in place | `nums.sort()` |
| `.reverse()` | Reverses the list in place | `nums.reverse()` |
| `.index(x)` | Returns index of first occurrence of x | `nums.index(2)` |
| `.count(x)` | Counts occurrences of x | `nums.count(2)` |
| `.extend(list)` | Adds all items from another list | `nums.extend([7, 8])` |
| `.copy()` | Returns a shallow copy | `nums.copy()` |

### Key Points

- Lists are **mutable** — you can change, add, and remove items.
- Use list comprehensions for concise creation: `[x ** 2 for x in range(5)]`

---

## 3. Tuples

A **tuple** is an ordered, immutable collection. Tuples are enclosed in parentheses (`(...)`).

### Creating Tuples

```python
empty = ()
single = (42,)                  # note the trailing comma
coordinates = (10, 20)
mixed = (1, "two", 3.0)
from_list = tuple([1, 2, 3])   # (1, 2, 3)
```

### Common Operations

| Operation | Example | Result |
|---|---|---|
| Length | `len((1, 2, 3))` | `3` |
| Access by index | `(10, 20, 30)[1]` | `20` |
| Slicing | `(10, 20, 30, 40)[1:3]` | `(20, 30)` |
| Concatenation | `(1, 2) + (3, 4)` | `(1, 2, 3, 4)` |
| Repetition | `(0,) * 3` | `(0, 0, 0)` |
| Membership | `3 in (1, 2, 3)` | `True` |
| Unpacking | `x, y = (10, 20)` | `x=10, y=20` |

### Common Methods

| Method | Description | Example | Result |
|---|---|---|---|
| `.count(x)` | Counts occurrences of x | `(1, 2, 2, 3).count(2)` | `2` |
| `.index(x)` | Returns index of first occurrence of x | `(1, 2, 3).index(3)` | `2` |

### Key Points

- Tuples are **immutable** — once created, you cannot change, add, or remove items.
- Tuples only have 2 methods (`.count()` and `.index()`) because they can't be modified.
- Use tuples when the data should not change (e.g., coordinates, RGB colors, database rows).

---

## 4. Sets

A **set** is an unordered collection of unique items. Sets are enclosed in curly braces (`{...}`).

### Creating Sets

```python
empty = set()               # NOT {} — that creates an empty dict
numbers = {1, 2, 3, 4, 5}
from_list = set([1, 2, 2, 3])  # {1, 2, 3} — duplicates removed
```

### Common Operations

| Operation | Example | Result |
|---|---|---|
| Length | `len({1, 2, 3})` | `3` |
| Membership | `3 in {1, 2, 3}` | `True` |
| Union | `{1, 2} \| {2, 3}` | `{1, 2, 3}` |
| Intersection | `{1, 2, 3} & {2, 3, 4}` | `{2, 3}` |
| Difference | `{1, 2, 3} - {2, 3}` | `{1}` |
| Symmetric Difference | `{1, 2, 3} ^ {2, 3, 4}` | `{1, 4}` |

### Common Methods

| Method | Description | Example |
|---|---|---|
| `.add(x)` | Adds an item | `s.add(4)` |
| `.remove(x)` | Removes an item (raises error if missing) | `s.remove(3)` |
| `.discard(x)` | Removes an item (no error if missing) | `s.discard(3)` |
| `.pop()` | Removes and returns an arbitrary item | `s.pop()` |
| `.union(set)` | Returns union of two sets | `s.union({4, 5})` |
| `.intersection(set)` | Returns common items | `s.intersection({2, 3})` |
| `.difference(set)` | Returns items in s but not in other | `s.difference({2, 3})` |
| `.issubset(set)` | Checks if s is a subset | `{1, 2}.issubset({1, 2, 3})` |
| `.issuperset(set)` | Checks if s is a superset | `{1, 2, 3}.issuperset({1, 2})` |
| `.clear()` | Removes all items | `s.clear()` |

### Key Points

- Sets are **unordered** — items have no index, so you cannot access by position.
- Sets only store **unique** items — duplicates are automatically removed.
- Use sets when you need fast membership checks or to remove duplicates from a list.

---

## 5. Dictionaries

A **dictionary** is an unordered collection of key-value pairs. Dictionaries are enclosed in curly braces (`{key: value, ...}`).

### Creating Dictionaries

```python
empty = {}
person = {"name": "Alice", "age": 25, "city": "NYC"}
from_pairs = dict([("a", 1), ("b", 2)])  # {'a': 1, 'b': 2}
```

### Common Operations

| Operation | Example | Result |
|---|---|---|
| Length | `len({"a": 1, "b": 2})` | `2` |
| Access by key | `person["name"]` | `"Alice"` |
| Set/update value | `person["age"] = 26` | updates age to 26 |
| Membership (keys) | `"name" in person` | `True` |
| Delete a key | `del person["city"]` | removes "city" |

### Common Methods

| Method | Description | Example |
|---|---|---|
| `.keys()` | Returns all keys | `person.keys()` |
| `.values()` | Returns all values | `person.values()` |
| `.items()` | Returns all key-value pairs as tuples | `person.items()` |
| `.get(key, default)` | Returns value for key, or default if missing | `person.get("age", 0)` |
| `.pop(key)` | Removes key and returns its value | `person.pop("city")` |
| `.update(other)` | Merges another dict into this one | `person.update({"age": 30})` |
| `.setdefault(key, val)` | Returns value if key exists, else sets and returns val | `person.setdefault("age", 0)` |
| `.copy()` | Returns a shallow copy | `person.copy()` |
| `.clear()` | Removes all items | `person.clear()` |

### Key Points

- Dictionaries are **mutable** — you can change, add, and remove key-value pairs.
- Keys must be **immutable** types (strings, numbers, tuples) — lists and sets cannot be keys.
- Use dict comprehensions for concise creation: `{x: x ** 2 for x in range(5)}`

---

## Quick Comparison

| Feature | String | List | Tuple | Set | Dict |
|---|---|---|---|---|---|
| Syntax | `"abc"` | `[1, 2, 3]` | `(1, 2, 3)` | `{1, 2, 3}` | `{"a": 1}` |
| Ordered | Yes | Yes | Yes | No | No* |
| Mutable | No | Yes | No | Yes | Yes |
| Duplicates | Yes | Yes | Yes | No | Keys: No |
| Indexed | Yes | Yes | Yes | No | By key |

\* Dictionaries preserve insertion order (Python 3.7+), but are not considered a "sequence" type.
