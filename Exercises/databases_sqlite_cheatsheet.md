# Databases & SQLite Cheatsheet

In `examples/flask_login/` we saved users to a text file:

```
joel,secret123
alice,hunter2
```

It worked. It also forced us into some strange rules — no commas in a username,
read the *whole* file to check *one* login, and "add an email field" means
breaking every line already written.

A **database** is the tool built for exactly this job. This cheatsheet covers
what a database is, the SQL you need, and how to drive one from Python — and it
finishes by replacing `load_users()` and `save_user()` with database calls.

```
 Today:      Python  ──►  open("users.txt")  ──►  a text file
 By the end: Python  ──►  sqlite3            ──►  users.db
```

Nothing else in that app changes. That was the point of keeping those two
functions separate from the routes.

---

## 1. What a Database Actually Is

A database is a program that stores your data **for** you, so you stop writing
the storage code yourself.

With a file, *you* write the parsing, *you* keep it consistent, *you* search it.
With a database, you describe what you want and it does the work:

| You want | File version | Database version |
|---|---|---|
| One user by name | read every line, split, compare | `SELECT * FROM users WHERE username = ?` |
| Reject duplicates | load everything, check `in` | `UNIQUE` — the database refuses |
| Delete a user | read all, filter, rewrite the file | `DELETE FROM users WHERE username = ?` |
| Add an email column | invent a new format, old lines break | `ALTER TABLE users ADD COLUMN email TEXT` |
| Two signups at once | both append, lines can interleave | the database serialises them |

### The honest argument

The text file is not *wrong*, it is just **small**. Here is exactly where it
stops working:

- **Searching is linear.** `load_users()` reads the entire file on every single
  login. Fine for 5 users. Unusable at 50,000.
- **The format is fragile.** A comma inside a username corrupts the row, so we
  had to *ban commas* — a rule about our users that exists only because of how
  we store bytes on disk.
- **There are no types.** Everything is a string. `"25"` and `25` are the same.
- **There is no "half-done".** If the program crashes between writing two
  related lines, the file is left in a broken state and nothing fixes it.
- **One writer only.** Two requests appending at the same moment can interleave.

### Key Points

- A database is **a program**, not a file format — even when it lives in a file.
- You stop writing parsing code. You start writing **queries**.
- The rules (unique, required, numeric) live **with the data**, not scattered
  through your Python.

---

## 2. The Vocabulary

You already know this shape — it is a list of dictionaries:

```python
users = [
    {"id": 1, "username": "joel",  "password": "secret123"},
    {"id": 2, "username": "alice", "password": "hunter2"},
]
```

A database calls the same thing a **table**:

```
                     columns  (the keys — fixed for everybody)
              ┌──────────┬──────────┬────────────┐
              │    id    │ username │  password  │
              ├──────────┼──────────┼────────────┤
   a row  ──► │    1     │   joel   │ secret123  │
   a row  ──► │    2     │  alice   │  hunter2   │
              └──────────┴──────────┴────────────┘
```

| Database word | You already call it | Meaning |
|---|---|---|
| **Database** | the whole `users.db` file | a collection of tables |
| **Table** | a list of dicts | one kind of thing — users, posts, orders |
| **Row** (record) | one dict | one user |
| **Column** (field) | one key | one piece of information, same for every row |
| **Schema** | — | the table's definition: its columns and their rules |
| **Primary key** | — | the column that uniquely identifies a row |
| **Query** | — | a question or instruction, written in SQL |

### The one real difference

In a list of dicts, each dict can have whatever keys it likes. In a table,
**every row has exactly the same columns** — that is enforced, not a convention.
That rigidity is the feature: you can never again read a row and wonder whether
it has an `email` key.

### Key Points

- Table = list of records. Row = one record. Column = one field.
- The **schema** is written down once and the database enforces it forever.
- A **primary key** is how you point at one specific row.

---

## 3. SQLite — What It Is and Isn't

Most databases are a **server**: a separate program you install, start, log in
to, and talk to over the network (PostgreSQL, MySQL).

**SQLite is not a server.** It is a *library* — code that runs inside your
program — and your entire database is **one ordinary file** on disk.

```
 PostgreSQL:   your app  ──network──►  database server  ──►  files it manages
 SQLite:       your app  ──function call──►  users.db
```

| | SQLite | PostgreSQL / MySQL |
|---|---|---|
| Install | nothing — it ships with Python | install and run a server |
| The database is | one file: `users.db` | managed by the server process |
| Start it | you don't | a service that must be running |
| Users/passwords | none — file permissions are the security | roles, grants, logins |
| Copy/backup it | copy the file | `pg_dump`, replication |
| Good for | learning, desktop apps, phones, one modest website | many apps, many servers, heavy writes |
| Bad at | lots of **simultaneous writers** | being simple |

SQLite is not a toy. It is on every phone you own, in every browser, in
aeroplanes and cars — most-deployed database in the world. It is the right
choice here because there is **nothing to install and nothing to run**: it is
part of the Python standard library.

```python
import sqlite3        # that's the whole installation
```

### Key Points

- SQLite = **a file + a library**. No server, no port, no password.
- Same SQL you would write against Postgres — switch later by changing the
  connection, not the queries.
- Its one real weakness is many writers at once; for a class project and for
  most small sites, irrelevant.

---

## 4. Creating a Table

**SQL** (Structured Query Language) is the language you talk to the database in.
It reads almost like English and it is *not* Python — it is a separate little
language you send across as a string.

```sql
CREATE TABLE users (
    id       INTEGER PRIMARY KEY,
    username TEXT    NOT NULL UNIQUE,
    password TEXT    NOT NULL
);
```

Read it as: *make a table called `users` with three columns.*

### The types

SQLite has only five, and you will use three:

| Type | Holds | Python equivalent |
|---|---|---|
| `INTEGER` | whole numbers | `int` |
| `REAL` | decimals | `float` |
| `TEXT` | strings | `str` |
| `BLOB` | raw bytes (images, files) | `bytes` |
| `NULL` | nothing at all | `None` |

There is **no boolean and no date type**. Use `INTEGER` `0`/`1` for yes/no, and
`TEXT` in the format `"2026-10-22 14:30:00"` for dates — that format sorts
correctly as plain text, which is why it is the standard one.

> SQLite is relaxed about types: it will happily let you put `"hello"` in an
> `INTEGER` column. Most databases refuse. Don't rely on the relaxation.

### The constraints — rules the database enforces

| Constraint | Means | What it replaces in `app.py` |
|---|---|---|
| `PRIMARY KEY` | unique identifier for the row | — |
| `NOT NULL` | this column can never be empty | `if not username: ...` |
| `UNIQUE` | no two rows may share this value | `if username in users: ...` |
| `DEFAULT x` | fill this in if nobody says otherwise | — |
| `CHECK (...)` | any condition you like | `if len(password) < 4: ...` |

```sql
CREATE TABLE users (
    id         INTEGER PRIMARY KEY,
    username   TEXT    NOT NULL UNIQUE,
    password   TEXT    NOT NULL,
    email      TEXT,                                    -- optional: may be NULL
    created_at TEXT    DEFAULT CURRENT_TIMESTAMP,       -- filled in automatically
    is_admin   INTEGER NOT NULL DEFAULT 0               -- 0 = no, 1 = yes
);
```

Notice what just happened: **"username is already taken" is now a property of
the table**, not a check you have to remember to write in every route that
creates a user. Rules next to the data cannot be forgotten.

### `INTEGER PRIMARY KEY` is special

In SQLite, a column declared exactly `INTEGER PRIMARY KEY` **fills itself in**.
Insert a row without an `id` and you get the next number automatically.

```python
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("joel", "x"))
print(cursor.lastrowid)      # 1  — the id the database just assigned
```

You may see `AUTOINCREMENT` written after it. You almost never need it; it only
guarantees ids are never *reused* after deletion, at a small cost.

### `IF NOT EXISTS`

Running `CREATE TABLE` twice is an error. Since our app creates the table on
startup, every restart would crash:

```sql
CREATE TABLE IF NOT EXISTS users (...);
```

This is the same instinct as the `try/except FileNotFoundError` in
`load_users()` — "set it up if it isn't there yet, otherwise carry on."

### Key Points

- The schema is written **once** and enforced **forever**.
- `NOT NULL` and `UNIQUE` are validation you cannot forget to run.
- `INTEGER PRIMARY KEY` gives you free, automatic ids.
- Always `CREATE TABLE IF NOT EXISTS` in code that runs at startup.

---

## 5. The Four Verbs

Everything you do to data is one of four statements. Learn these and you can
use any SQL database on earth.

| Verb | Does | Python-ish equivalent |
|---|---|---|
| `INSERT` | add a row | `list.append()` |
| `SELECT` | read rows | a `for` loop with an `if` |
| `UPDATE` | change rows | `d["key"] = value` |
| `DELETE` | remove rows | `list.remove()` |

### INSERT — add a row

```sql
INSERT INTO users (username, password) VALUES ('joel', 'secret123');
```

Name the columns you are filling; anything left out gets its `DEFAULT`, or
`NULL`. You can add several at once:

```sql
INSERT INTO users (username, password) VALUES ('joel', 'x'), ('alice', 'y');
```

### SELECT — read rows

```sql
SELECT * FROM users;                              -- every column, every row
SELECT username FROM users;                       -- one column, every row
SELECT username, email FROM users;                -- two columns
SELECT * FROM users WHERE username = 'joel';      -- one row  ← the login query
```

`*` means "all columns". Handy at the `sqlite3` prompt; in real code prefer
naming the columns, so adding a column later cannot change what your code gets
back.

**`WHERE` is the filter** — the `if` of SQL:

```sql
SELECT * FROM users WHERE id = 3;
SELECT * FROM users WHERE username = 'joel' AND is_admin = 1;
SELECT * FROM users WHERE email IS NULL;             -- not  = NULL
SELECT * FROM users WHERE username LIKE 'jo%';       -- starts with "jo"
SELECT * FROM users WHERE id IN (1, 2, 3);
```

| Operator | Means |
|---|---|
| `=` `!=` `<` `>` `<=` `>=` | compare (note: **one** `=`, not `==`) |
| `AND` `OR` `NOT` | combine conditions |
| `IS NULL` / `IS NOT NULL` | empty or not — `= NULL` never matches anything |
| `LIKE 'jo%'` | pattern: `%` is any text, `_` is one character |
| `IN (…)` | matches any value in the list |
| `BETWEEN a AND b` | inclusive range |

**Sorting and limiting:**

```sql
SELECT * FROM users ORDER BY username;              -- A→Z
SELECT * FROM users ORDER BY created_at DESC;       -- newest first
SELECT * FROM users ORDER BY id DESC LIMIT 5;       -- the 5 most recent
```

**Counting** — this is the one that shows off what a database is for:

```sql
SELECT COUNT(*) FROM users;                          -- how many users
SELECT COUNT(*) FROM users WHERE is_admin = 1;
```

In the file version, counting admins meant reading and parsing every line into
Python. Here the database counts them and hands back one number.

### UPDATE — change rows

```sql
UPDATE users SET password = 'newpass' WHERE username = 'joel';
```

> **`UPDATE` without `WHERE` changes every row in the table.** There is no undo.
> Write the `WHERE` first, then go back and write the `SET`.

### DELETE — remove rows

```sql
DELETE FROM users WHERE username = 'joel';
```

> Same warning, worse: `DELETE FROM users;` empties the table.

Compare that one line to the file version — read the whole file, filter the
lines, rewrite the file, hope nothing crashes halfway.

### Key Points

- Four verbs: `INSERT`, `SELECT`, `UPDATE`, `DELETE`.
- `WHERE` is the `if`. `ORDER BY` is `sorted()`. `LIMIT` is a slice.
- **Always write the `WHERE` on an `UPDATE` or `DELETE` first.**
- `IS NULL`, never `= NULL`.

---

## 6. SQLite from Python

The module is in the standard library. Four objects, in order:

```python
import sqlite3

conn = sqlite3.connect("users.db")     # 1. open the file (creates it if missing)
cursor = conn.cursor()                 # 2. something to run queries with

cursor.execute("SELECT * FROM users")  # 3. run the SQL
rows = cursor.fetchall()               # 4. collect the results

conn.commit()                          # save any changes
conn.close()                           # close the file
```

| Step | Object | Think of it as |
|---|---|---|
| `connect()` | `Connection` | `open()` — the file is now in use |
| `.cursor()` | `Cursor` | your place in the results; you run queries through it |
| `.execute(sql)` | — | send one statement |
| `.fetchone()` / `.fetchall()` | — | collect what came back |
| `.commit()` | on the connection | **save** — without it, writes are discarded |
| `.close()` | on the connection | `f.close()` |

`sqlite3.connect("users.db")` **creates the file if it doesn't exist**. No
`FileNotFoundError`, no `try/except` — this is one of the chores a database
takes off your hands.

### Getting results out

```python
cursor.execute("SELECT username, password FROM users")

cursor.fetchone()    # the next row, as a tuple, or None if there are none left
cursor.fetchall()    # all remaining rows, as a list of tuples
```

```python
# one row expected — the login case
row = cursor.fetchone()
if row is None:
    print("no such user")
else:
    username, password = row         # tuple unpacking, exactly as you know it

# many rows — just loop over the cursor
for row in cursor.execute("SELECT username FROM users"):
    print(row[0])
```

`fetchone()` returning `None` is the direct replacement for
`users.get(username)` returning `None`. Same shape of code, same `if`.

### Tuples are awkward — use `sqlite3.Row`

```python
row = cursor.fetchone()
print(row[1])          # which column was 1 again?
```

Positional indexes break the moment someone adds a column. One line fixes it:

```python
conn.row_factory = sqlite3.Row         # set this right after connect()

row = cursor.fetchone()
print(row["username"])                 # now it reads like a dictionary
print(dict(row))                       # {'id': 1, 'username': 'joel', ...}
```

Set it **before** creating the cursor. `sqlite3.Row` behaves like a read-only
dict that also still supports `row[0]`.

### Closing properly

`with` works on a connection, but **it does not do what you expect**:

```python
with sqlite3.connect("users.db") as conn:    # commits on success, rolls back on error
    ...                                      # ...and does NOT close the connection
```

Unlike `with open(...)`, this manages the **transaction**, not the file. To be
sure of both, close explicitly:

```python
conn = sqlite3.connect("users.db")
try:
    ...
    conn.commit()
finally:
    conn.close()
```

In Python 3.12+ you can use `sqlite3.connect(...)` with `closing()` from
`contextlib`, but for class code the `try/finally` above — or a small helper
function — is clearer.

### Key Points

- `connect` → `cursor` → `execute` → `fetch` → `commit` → `close`.
- `connect()` creates the file. No missing-file handling needed.
- `fetchone()` gives `None` when there is no row — check for it.
- `conn.row_factory = sqlite3.Row` turns tuples into dict-like rows. Always do it.
- `with conn:` commits; it does **not** close.

---

## 7. Placeholders — the Most Important Rule in This Document

You need a username from a variable inside a query. The obvious thing is an
f-string. **Never do this:**

```python
# ☠️ NEVER
cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
```

Because the user controls `username`, and so the user is now writing your SQL.
Suppose they type this into the login box:

```
' OR '1'='1
```

The string you built is:

```sql
SELECT * FROM users WHERE username = '' OR '1'='1'
```

`'1'='1'` is always true, so this matches **every row**, `fetchone()` returns the
first user, and the attacker is logged in as them — without a password. This is
**SQL injection**, and it is still one of the most common serious bugs on the
web.

### The fix: `?`

Pass the values *separately*, as a tuple. The database then treats them as
**data** and never as SQL:

```python
# ✅ ALWAYS
cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
```

```python
cursor.execute(
    "INSERT INTO users (username, password) VALUES (?, ?)",
    (username, password),
)
```

Now typing `' OR '1'='1` searches for a user literally named `' OR '1'='1`,
finds nobody, and login fails. Which is correct.

### Three things people trip on

```python
cursor.execute("... WHERE username = ?", (username))    # ✗ not a tuple!
cursor.execute("... WHERE username = ?", (username,))   # ✓ note the comma
```

A single-element tuple needs the trailing comma. Without it Python sees a plain
string, treats each *character* as a value, and you get:

```
sqlite3.ProgrammingError: Incorrect number of bindings supplied.
The current statement uses 1, and there are 4 supplied.
```

```python
cursor.execute("... WHERE username = '?'", (username,))  # ✗ no quotes round ?
cursor.execute("... WHERE username = ?",   (username,))  # ✓
```

The `?` is not a string-formatting hole; quoting is the database's job. Quote it
and SQLite reads `'?'` as the literal text `"?"`, so the statement needs **zero**
bindings and you get `Incorrect number of bindings supplied ... uses 0`.

```python
cursor.execute(f"SELECT * FROM {table_name}")            # ✗ and unavoidable
```

Placeholders work for **values only** — never table or column names. If you
genuinely need a dynamic table name, check it against a hard-coded list of
allowed names yourself.

### Named placeholders

For queries with many values, `:name` with a dict is more readable:

```python
cursor.execute(
    "INSERT INTO users (username, password) VALUES (:user, :pw)",
    {"user": username, "pw": password},
)
```

### Many rows at once

```python
people = [("joel", "x"), ("alice", "y"), ("sam", "z")]
cursor.executemany("INSERT INTO users (username, password) VALUES (?, ?)", people)
```

### Key Points

- **Every single value from outside your program goes in as `?`.** No exceptions.
- No quotes around `?`. One value still needs a trailing comma: `(x,)`.
- Placeholders are for values, never for table or column names.
- This is also faster, and it handles apostrophes in names (`O'Brien`) for free.

> **Footnote for the curious:** Python's `execute()` refuses to run more than one
> statement, so the famous `'; DROP TABLE users; --` attack fails here. The
> `' OR '1'='1` login bypass above needs only one statement — so it works
> perfectly. Do not take comfort in the first fact.

---

## 8. Commit — Why Your Data Disappeared

Everybody hits this once.

```python
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("joel", "x"))
conn.close()
# restart the program... joel is gone.
```

Changes live in a **transaction** until you commit them. No `commit()` means the
database throws the work away when the connection closes.

```python
cursor.execute("INSERT ...")
conn.commit()                 # ← now it is really on disk
```

### Why transactions exist

A transaction is **all-or-nothing**. Transferring money is the classic example:

```python
cursor.execute("UPDATE accounts SET balance = balance - 100 WHERE id = 1")
# ← if the program crashes HERE...
cursor.execute("UPDATE accounts SET balance = balance + 100 WHERE id = 2")
conn.commit()
```

Without transactions, that crash destroys £100. With them, the uncommitted first
update is rolled back and the database is exactly as it was. Either **both**
statements happen or **neither** does.

```python
conn.commit()      # make all of it permanent
conn.rollback()    # throw all of it away
```

This is the thing a text file fundamentally cannot do. A crash midway through
writing `users.txt` leaves a half-written file and no way back.

### Key Points

- `SELECT` needs no commit. `INSERT`, `UPDATE`, `DELETE` all do.
- Forgot to commit = the write silently never happened.
- A transaction is all-or-nothing; that guarantee is a core reason databases exist.

---

## 9. Looking at Your Data

You do not have to write Python to inspect the database. SQLite ships a terminal
tool (and it is already installed on macOS):

```bash
sqlite3 users.db
```

```
sqlite> .tables                        -- list the tables
sqlite> .schema users                  -- show the CREATE TABLE statement
sqlite> .headers on                    -- show column names in results
sqlite> .mode column                   -- line the output up in columns
sqlite> SELECT * FROM users;           -- normal SQL, semicolon required
sqlite> .quit
```

Commands starting with `.` are the tool's own; everything else is SQL and
**needs a trailing semicolon** (if the prompt turns into `...>`, you forgot it —
type `;` and press enter).

This is the direct replacement for the `/debug/users-file` route in
`flask_login`: a way to see that your data is really there. Prefer a graphical
tool? **DB Browser for SQLite** is free and shows the table as a spreadsheet.

The one thing to notice: open `users.db` in a text editor and it is mostly
unreadable binary. That is the trade. You gave up "I can read it in Notepad" and
got indexes, types, constraints and transactions in return.

> ⚠️ `users.db` should go in `.gitignore`, just like `users.txt` — it is data,
> not code, and it contains your users' passwords.

---

## 10. Replacing the File with a Database

Here is the whole point. From `examples/flask_login/app.py`:

> *"The routes handle the WEB, these functions handle the DATA. Tomorrow we swap
> the file for a database — and ONLY these two functions change."*

Let's do it.

### Before — the text file

```python
USERS_FILE = "users.txt"

def load_users():
    users = {}
    try:
        with open(USERS_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                username, password = line.split(",", 1)
                users[username] = password
    except FileNotFoundError:
        pass
    return users

def save_user(username, password):
    with open(USERS_FILE, "a") as f:
        f.write(f"{username},{password}\n")
```

### After — SQLite

```python
import sqlite3

DB_FILE = "users.db"


def get_db():
    """Open a connection with dict-like rows."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Create the table if it isn't there yet. Safe to call on every startup."""
    conn = get_db()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id       INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def load_users():
    """Same signature, same return value: {username: password}."""
    conn = get_db()
    rows = conn.execute("SELECT username, password FROM users").fetchall()
    conn.close()
    return {row["username"]: row["password"] for row in rows}


def save_user(username, password):
    """Append one new user — now a row, not a line."""
    conn = get_db()
    conn.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, password),
    )
    conn.commit()
    conn.close()


init_db()        # runs once, when the module is imported
```

Both functions keep their **names, arguments and return types**, so every route
in `app.py` works untouched. That is what "separate the storage layer" buys you.

> `conn.execute(...)` is a shortcut: the connection makes a cursor for you and
> returns it. For one-statement calls it saves a line.

### Then do it properly

`load_users()` still loads **every user in the database** just to check one
login — the exact problem we set out to fix. The database can answer the real
question, so ask it:

```python
def get_user(username):
    """Return one user's row, or None if there is no such user."""
    conn = get_db()
    row = conn.execute(
        "SELECT * FROM users WHERE username = ?",
        (username,),
    ).fetchone()
    conn.close()
    return row
```

The login route barely changes, because `fetchone()` returning `None` behaves
just like `dict.get()` returning `None`:

```python
# before
users = load_users()
stored_password = users.get(username)
if stored_password is None or stored_password != password:
    ...error...

# after
user = get_user(username)
if user is None or user["password"] != password:
    ...error...
```

One row crosses the wire instead of the entire user table. With an index on
`username` — and `UNIQUE` creates one automatically — this stays fast at a
million users.

### Let the database reject duplicates

The register route checks `if username in users`. With a `UNIQUE` column the
database enforces that itself, and tells you by raising:

```python
def save_user(username, password):
    conn = get_db()
    try:
        conn.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password),
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False          # UNIQUE constraint failed: users.username
    finally:
        conn.close()
```

Keep the Python check too — it gives a nicer error message — but now a *second*
guard exists that no future route can forget. Note also that this version has no
race: between `if username in users` and `save_user(...)`, another request could
sneak the same name in. `UNIQUE` cannot be raced.

### What disappears

| In the file version | In the database version |
|---|---|
| `try/except FileNotFoundError` | gone — `connect()` creates the file |
| `.strip()` on every line | gone — no line endings to clean |
| `line.split(",", 1)` | gone — columns are columns |
| **"Sorry, no commas allowed"** | **gone — and good riddance** |
| `"a"` vs `"w"` mode bug | gone — `INSERT` cannot wipe the table |
| `if username in users` | still there, but `UNIQUE` backs it up |
| Reading the whole file per login | gone — `WHERE username = ?` |

That comma rule is worth pausing on. We made our *users* obey a restriction
because of our *file format*. The storage layer was leaking into the product.
Changing the storage made the rule vanish.

### Adding a column is now easy

Remember experiment 7 in the `flask_login` README — add an email field, and count
how many places change? Here:

```sql
ALTER TABLE users ADD COLUMN email TEXT;
```

Existing rows get `NULL` for it. Nothing breaks. Then add it to the form and to
the `INSERT`.

### Flask-specific note: one connection per request

SQLite connections cannot be shared between threads, and Flask's dev server
handles requests in several threads. **Do not make one global connection.** Open
and close inside the function, as above — that is simple and correct.

The tidier pattern, once you want it, uses Flask's `g` (one connection per
request, closed automatically at the end):

```python
from flask import g

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_FILE)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()
```

### And the passwords are still in plain text

Swapping the file for a database **did nothing** about the real security
problem. A stolen `users.db` is exactly as bad as a stolen `users.txt`. That fix
is still the one from the `flask_login` README:

```python
from werkzeug.security import generate_password_hash, check_password_hash

save_user(username, generate_password_hash(password))      # registering
check_password_hash(user["password"], password)            # logging in
```

Make the column wide enough — `TEXT` has no length limit in SQLite, so it
already is.

---

## 11. One More Idea: Relationships

The reason these are called **relational** databases: tables can point at each
other. Say every user can write posts.

```sql
CREATE TABLE posts (
    id      INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    title   TEXT    NOT NULL,
    body    TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

`user_id` holds the `id` of the user who wrote the post — a **foreign key**. You
store the author *once*, in `users`, and point at it from everywhere else.

A `JOIN` reassembles them in a single query:

```sql
SELECT users.username, posts.title
FROM posts
JOIN users ON posts.user_id = users.id
ORDER BY posts.id DESC;
```

```
username | title
---------+------------------
joel     | My second post
alice    | Hello world
```

That is a proper topic for another day — but it is the answer to "where does
this go?". Try writing *that* across two text files.

> In SQLite, foreign keys are **not enforced by default**. Run
> `conn.execute("PRAGMA foreign_keys = ON")` on each connection if you want the
> database to actually reject a `user_id` that doesn't exist.

---

## Quick Reference

### Python

| Task | Code |
|---|---|
| Import | `import sqlite3` |
| Connect (creates the file) | `conn = sqlite3.connect("users.db")` |
| Dict-like rows | `conn.row_factory = sqlite3.Row` |
| Run a statement | `cur = conn.execute(sql, params)` |
| One row, or `None` | `cur.fetchone()` |
| All rows, as a list | `cur.fetchall()` |
| Insert many | `conn.executemany(sql, list_of_tuples)` |
| Id of the row just inserted | `cur.lastrowid` |
| Rows changed by UPDATE/DELETE | `cur.rowcount` |
| Save changes | `conn.commit()` |
| Undo uncommitted changes | `conn.rollback()` |
| Close | `conn.close()` |
| Duplicate / `NOT NULL` violation | `except sqlite3.IntegrityError:` |

### SQL

| Task | Statement |
|---|---|
| Create a table | `CREATE TABLE IF NOT EXISTS t (id INTEGER PRIMARY KEY, name TEXT NOT NULL)` |
| Add a column | `ALTER TABLE t ADD COLUMN email TEXT` |
| Delete a table | `DROP TABLE t` |
| Insert | `INSERT INTO t (a, b) VALUES (?, ?)` |
| Read everything | `SELECT * FROM t` |
| Read some columns | `SELECT a, b FROM t` |
| Filter | `SELECT * FROM t WHERE a = ?` |
| Empty check | `WHERE a IS NULL` |
| Pattern match | `WHERE a LIKE 'jo%'` |
| Sort | `ORDER BY a` / `ORDER BY a DESC` |
| First n | `LIMIT 5` |
| Count | `SELECT COUNT(*) FROM t` |
| Update | `UPDATE t SET a = ? WHERE id = ?` |
| Delete | `DELETE FROM t WHERE id = ?` |

### The `sqlite3` shell

| Command | Does |
|---|---|
| `sqlite3 users.db` | open (or create) the database |
| `.tables` | list tables |
| `.schema users` | show a table's definition |
| `.headers on` | show column names |
| `.mode column` | aligned output |
| `.quit` | leave |

---

## Common Problems

| What you see | What's wrong | Fix |
|---|---|---|
| Data gone after restart | no `conn.commit()` | commit after every `INSERT`/`UPDATE`/`DELETE` |
| `no such table: users` | the table was never created, or you opened a different `.db` file | call `init_db()`; check your working directory |
| `table users already exists` | `CREATE TABLE` run twice | `CREATE TABLE IF NOT EXISTS` |
| `UNIQUE constraint failed: users.username` | the username is taken | catch `sqlite3.IntegrityError` and show an error |
| `NOT NULL constraint failed: users.password` | you inserted `None`/nothing for a required column | validate before inserting |
| `Incorrect number of bindings supplied ... uses 1, and there are 4 supplied` | missing comma in a one-item tuple, so the string's characters were counted | `(username,)` not `(username)` |
| `Incorrect number of bindings supplied ... uses 0` | you wrote `'?'` in quotes, so SQLite sees literal text | drop the quotes round `?` |
| `parameters are of unsupported type` | you passed a bare value instead of a tuple | `(value,)` |
| `near "?": syntax error` | a `?` used for a table or column name | placeholders are for values only |
| Query matches nothing, but the row exists | `= NULL`, or a stray space in the stored value | use `IS NULL`; `.strip()` before inserting |
| `TypeError: 'NoneType' object is not subscriptable` | `fetchone()` found no row | `if row is None:` before using it |
| `row[1]` is the wrong column | positional indexing after a schema change | `conn.row_factory = sqlite3.Row`, then `row["name"]` |
| `database is locked` | another connection is mid-write (or you left the `sqlite3` shell open in a transaction) | close connections; don't hold them open |
| `SQLite objects created in a thread…` | a connection shared between threads | open one per request, not one global |
| Everybody can log in with `' OR '1'='1` | you built SQL with an f-string | use `?` placeholders |

---

## Concepts Map — What You Already Know → Databases

| You Already Know | Database Equivalent |
|---|---|
| **List of dictionaries** | a table — rows and columns |
| **One dictionary** | one row |
| **A dict key** | a column |
| **`list.append(x)`** | `INSERT INTO ... VALUES (...)` |
| **`for x in list: if ...`** | `SELECT ... WHERE ...` |
| **`d.get(k)` → `None`** | `cursor.fetchone()` → `None` |
| **`sorted(list, reverse=True)`** | `ORDER BY col DESC` |
| **`list[:5]`** | `LIMIT 5` |
| **`len(list)`** | `SELECT COUNT(*)` |
| **`d[k] = v`** | `UPDATE ... SET ... WHERE ...` |
| **`list.remove(x)`** | `DELETE FROM ... WHERE ...` |
| **`open()` / `close()`** | `connect()` / `close()` |
| **`try/except FileNotFoundError`** | unnecessary — `connect()` creates the file |
| **Saving with `f.write()`** | `conn.commit()` |
| **`if username in users`** | a `UNIQUE` column |
| **`if not username`** | a `NOT NULL` column |
| **Never trusting `request.form`** | never f-stringing it into SQL — use `?` |

---

## Where This Goes Next

The pattern to remember is the one that made today easy:

```
 routes  →  storage functions  →  wherever the data lives
            ^^^^^^^^^^^^^^^^^
            change only this
```

`examples/flask_login/` was written that way on purpose, and the swap cost two
functions. Next time the destination is PostgreSQL on a server somewhere, or an
ORM like SQLAlchemy writing the SQL for you — and if the seam is still clean, it
is still two functions.

After this: hashing those passwords properly, then relationships and `JOIN`s
between tables.
