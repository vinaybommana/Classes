# A Login System — Forms In, Data Saved to a File

The follow-on to `examples/flask_templates/`. There we rendered pages; here we
**receive** data, **save** it, and **remember who is logged in**.

Read `Exercises/html_forms_css_cheatsheet.md` first — it covers the HTML and CSS
this app uses. Then read `app.py` top to bottom; every file is commented.

---

## The three new ideas

| Idea | The code | In one line |
|---|---|---|
| **Read a form** | `request.form.get("username", "")` | the `name=` attributes arrive as a dictionary |
| **Remember data** | `open("users.txt", "a")` | the file I/O you already know, nothing more |
| **Remember the user** | `session["username"] = username` | a signed note in the browser, sent with every request |

Everything else is routes, `render_template`, and `if`/`else`.

---

## Folder layout

```
flask_login/
├── app.py
├── users.txt            ← created automatically on first signup
├── templates/
│   ├── base.html        ← nav changes depending on login state
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html   ← only reachable when logged in
│   └── debug_file.html  ← prints users.txt, for teaching
└── static/
    └── style.css
```

`users.txt` sits **next to `app.py`, not inside `static/`**. Anything in
`static/` is downloadable by the whole internet — putting a password file there
would publish it.

---

## Setup and running

```bash
python3 -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows
pip install flask

python app.py
```

Then open <http://localhost:5000/>.

On macOS, if every page is **403 Forbidden**, AirPlay Receiver owns port 5000 —
use `app.run(debug=True, port=5001)`.

---

## The walkthrough

Do these in order. Each step is one concept.

| # | Do this | Watch for |
|---|---|---|
| 1 | Open <http://localhost:5000/> | `/` redirects you to `/login` |
| 2 | Click **Register**, submit it empty | the browser blocks you — that's `required`, free |
| 3 | Register with a 2-character password | the browser blocks you — that's `minlength` |
| 4 | Register properly | redirected to login with a green message |
| 5 | Look at **users.txt** in the nav | your account, on disk, in plain text |
| 6 | Log in with the **wrong** password | "Username or password is incorrect" |
| 7 | Log in properly | the dashboard, and the nav bar changes |
| 8 | Click **Log out**, then type `/dashboard` in the address bar | bounced back — the guard in `app.py` |
| 9 | Register the same username twice | "already taken" |
| 10 | `Ctrl+C`, restart, refresh | the account survived; the login survived too |

---

## The one pattern to take away

```python
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # the form was submitted — read it, check it, act on it
        ...
        return redirect(url_for("dashboard"))

    # otherwise just show the empty form
    return render_template("login.html")
```

One route, two jobs. `GET` shows the form, `POST` receives it. You will write
this shape for the rest of your life.

```
 GET  /login   →  render login.html                    (empty form)
 POST /login   →  read request.form → check → session  (then redirect)
```

### Why redirect after a POST?

After a `POST`, the address bar still says `/login`. Pressing refresh would
**re-submit the form**. Redirecting sends the browser off to do a plain `GET`
on another URL, which is safe to refresh. This is the **Post/Redirect/Get**
pattern and it is standard practice.

---

## The storage layer

Two functions in `app.py`, both plain Python — no Flask, no decorators:

```python
def load_users():
    """Read the whole file and return {username: password}."""

def save_user(username, password):
    """Append one new user to the end of the file."""
```

The routes handle the **web**. These two handle the **data**. That line matters:
tomorrow we swap the file for a database and **only these two functions change**.

### The file format

```
joel,secret123
alice,hunter2
```

| Detail | Why |
|---|---|
| `"a"` mode, not `"w"` | `"w"` wipes the file — your second signup would erase your first |
| `"\n"` at the end | without it, every user ends up on one unreadable line |
| `try/except FileNotFoundError` | the file doesn't exist until the first signup |
| `.split(",", 1)` | split on the **first** comma only — one stray comma can't shift the columns |
| commas rejected at signup | our format uses commas as separators, so a comma in a username corrupts the row |

That last one is worth pointing at. It is a silly rule that exists **only because
of how we chose to store the data**. A database would have no such restriction.

---

## Sessions — how a site remembers you

HTTP has **no memory**. Every request is a stranger knocking at the door; the
next page load knows nothing about the last one. So how does a site keep you
logged in?

```
 1. You POST a correct username + password
 2. Flask puts {"username": "joel"} in a cookie, SIGNED with app.secret_key
 3. Your browser stores that cookie
 4. Your browser sends it back with EVERY request, automatically
 5. Any route can read it:   session["username"]  →  "joel"
```

So `session` is a dictionary that survives between requests and is private to
one browser. **That is all a login is**: a note saying who you are, carried
along with each request.

```python
session["username"] = username     # log in
session.get("username")            # who is this?  (None if nobody)
session.pop("username", None)      # log out
```

| | Lives where | Survives a server restart? | Survives closing the browser? |
|---|---|---|---|
| `session` | the user's browser (a cookie) | yes, while `secret_key` is unchanged | depends on the browser |
| `users.txt` | your disk | yes | yes, it has nothing to do with the browser |

Two things worth saying out loud:

- **Signed means tamper-proof, not hidden.** The user can decode and read their
  own cookie. Never put anything secret in the session.

  Demo this live. Log in, open developer tools → Application → Cookies, and
  copy the `session` value. The first chunk (before the first `.`) is just
  base64:

  ```bash
  python3 -c "import base64; print(base64.urlsafe_b64decode('eyJ1c2VybmFtZSI6ImpvZWwifQ=='))"
  # b'{"username":"joel"}'
  ```

  There is your session, in plain sight. The parts after the dots are a
  timestamp and the signature — change a single character of the data and the
  signature stops matching, so Flask throws the whole cookie away. You can
  **read** it; you cannot **forge** it.

- **`app.secret_key` is what makes it tamper-proof.** Hard-coding it is fine for
  a classroom. In a real app it comes from an environment variable and is never
  committed to git. Change the key and every existing login is invalidated.

### Protecting a page

```python
@app.route("/dashboard")
def dashboard():
    username = session.get("username")
    if username is None:
        return redirect(url_for("login"))
    ...
```

Three lines at the top of every private route. Without them, **anyone can type
the URL and walk straight in** — the login page is not a door, it's just a page.
Hiding the link in the nav bar is not security either.

---

## Validation — and why we check everything twice

`register.html` already has `required` and `minlength="4"`. `app.py` checks both
again. That is not redundancy.

> **Browser-side checks are a convenience, never a defence.**

Anyone can delete `required` in developer tools, or skip the browser entirely:

```bash
curl -X POST -d "username=&password=" http://localhost:5000/register
```

Try that while the server is running. The browser's rules never ran at all — the
server's did. **The server is the only place a rule is actually enforced.**

Four checks run in `register()`, in order:

1. Both fields non-empty
2. Password at least 4 characters
3. No commas (our file format needs this)
4. Username not already taken

Each one re-renders the form with an `error` message **and the username still
filled in**. Never make someone retype a field they got right.

### Why the login error is deliberately vague

```python
"Username or password is incorrect."
```

Not "no such user" or "wrong password". If those were different messages, anyone
could type usernames at the form until one came back "wrong password" and learn
who has an account here. Tell the attacker nothing; the honest user knows which
one they got wrong anyway.

---

## ⚠️ What's wrong with this app

This is a teaching app. Three things in it would be serious bugs in production,
and it's worth naming them out loud so nobody copies this into something real.

### 1. The passwords are stored in plain text

Open `/debug/users-file` and look. Anyone who reads that file owns every
account — and because people reuse passwords, probably their email too.

**Real apps never store a password.** They store a one-way *hash*: a scrambled
version that can be checked against but not reversed. Flask ships with the tools
already (`werkzeug` is a Flask dependency), and it's a two-line change:

```python
from werkzeug.security import generate_password_hash, check_password_hash

# when registering — store the hash, never the password
save_user(username, generate_password_hash(password))

# when logging in — compare, never decrypt
if not check_password_hash(stored_password, password):
    ...error...
```

Make that change, delete `users.txt`, register again, and look at the file. You
cannot read the passwords any more — and neither can anyone who steals the file.
`check_password_hash` works by hashing the attempt and comparing the two hashes;
there is no "unhash" step, which is exactly the point.

*(Hashes contain `:` and `$` but no commas, so our file format still survives.)*

### 2. A text file is not a database

| Problem | What happens |
|---|---|
| Every login reads the **whole file** | fine for 5 users, unusable at 50,000 |
| Two signups at the same moment | both append, and the file can interleave into garbage |
| A comma in a username | breaks the row — hence the silly rule |
| Want to store an email too? | change the format, and every existing line is now invalid |
| Delete a user? | read the entire file, filter, rewrite it |

This is the honest argument for databases, and it is tomorrow's lesson.

### 3. Small things

- `debug=True` must never run in production — it exposes a Python console.
- `app.secret_key` is hard-coded. Real apps load it from the environment.
- No rate limiting: a script can try a million passwords at `/login`.
- No CSRF protection (ask about `flask-wtf` once the basics are solid).

---

## Experiments

`debug=True` reloads on save — just refresh the browser.

1. Delete `users.txt` while the server is running, then refresh `/debug/users-file`.
   Read how `load_users()` handles the missing file.
2. Open `users.txt` in your editor and add a line by hand:
   `test,test1234`. Now log in as `test`. Nothing magic is happening.
3. Change `"a"` to `"w"` in `save_user()`. Register two people. Watch the first
   one vanish. Change it back.
4. Remove the `\n` from the `f.write(...)`. Register two people. Read the file.
5. Delete `required` from `login.html` and submit an empty form. The server
   catches it — because `app.py` checks too.
6. Comment out the guard in `dashboard()`, log out, and visit `/dashboard`.
   `{{ username }}` renders as nothing. The page has no idea who you are.
7. Add a third field — email — to the register form. You will need to change:
   the template, `save_user()`, `load_users()`, and the file format. Count how
   many places one new field touches. That's the point.
8. Swap in `generate_password_hash` as shown above.
9. Add a `/users` page listing every registered username (not passwords).
10. **Break it:** change `name="username"` to `name="user"` in `login.html` and
    submit. Read the error, then fix it.

---

## Common problems

| What you see | What's wrong | Fix |
|---|---|---|
| `405 Method Not Allowed` | the route doesn't allow POST | `methods=["GET", "POST"]` |
| `400 Bad Request` on submit | `name=` doesn't match the key in `request.form` | make the strings identical, or use `.get()` |
| `RuntimeError: The session is unavailable...` | no `app.secret_key` | set it, near the top of `app.py` |
| `KeyError: 'username'` from `session` | reading `session["username"]` when logged out | use `session.get("username")` |
| `FileNotFoundError` | reading `users.txt` before anyone registered | the `try/except` in `load_users()` |
| Everyone's account disappears on signup | `open(file, "w")` instead of `"a"` | use append mode |
| All users on one line in the file | missing `\n` in `f.write` | add it |
| Login always fails, even when correct | a trailing `\n` or space in the stored value | `.strip()` each line in `load_users()` |
| Refreshing after signup registers twice | no redirect after the POST | `return redirect(url_for(...))` |
| Logged in as the wrong person | you're testing two accounts in one browser | use a private window for the second |
| CSS change doesn't show | the browser cached it | hard refresh: `Cmd/Ctrl + Shift + R` |

---

## Where this goes next

The storage layer is two functions and a text file. Everything in the
"a text file is not a database" table above is a problem a database solves:
fast lookups by key, many writers at once, real columns, and deleting a row
without rewriting the world.

Tomorrow: the same app, with `load_users()` and `save_user()` talking to
SQLite instead. **Nothing else in this folder has to change.**
