# Flask Basics — Your First Web Application

A single, heavily-commented Flask app (`app.py`) that walks through the core ideas
one at a time. Read it top to bottom; each section builds on the one before.

For the theory behind this (HTTP, URLs, methods, status codes, JSON), see:

- `Exercises/web_development_overview.md` — how the web works, before any code
- `Exercises/flask_webservers_cheatsheet.md` — the Flask reference
- `Exercises/virtual_environments_cheatsheet.md` — what `venv` is and why we use it

---

## Setup

Flask isn't part of Python's standard library, so we install it first.

```bash
# 1. Create a virtual environment (an isolated place for this project's packages)
python3 -m venv .venv

# 2. Activate it  (your prompt will change to show "(.venv)")
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows

# 3. Install Flask
pip install flask
```

> **Why a virtual environment?** It keeps this project's packages separate from
> every other project on your machine. Not strictly required — `pip install flask`
> alone works — but it's the normal way to do it.
> Full explanation: `Exercises/virtual_environments_cheatsheet.md`.

---

## Running it

```bash
python app.py
```

You should see:

```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

The server is now **running and waiting**. It will not exit on its own — that's
the whole point. Leave this terminal open and switch to your browser.

Press `Ctrl+C` in the terminal to stop it.

---

## Things to try

Open each of these in your browser:

| URL | What it shows | Concept |
|---|---|---|
| http://localhost:5000/ | Hello, World! | the simplest route |
| http://localhost:5000/about | a second page | multiple routes |
| http://localhost:5000/contact | a heading and a paragraph | returning HTML |
| http://localhost:5000/hello/Joel | Hello, Joel! | dynamic route `<name>` |
| http://localhost:5000/square/7 | 7 squared is 49 | type converter `<int:n>` |
| http://localhost:5000/add/3/5 | 3 + 5 = 8 | two URL variables |
| http://localhost:5000/greet | Hello, stranger! | query param default |
| http://localhost:5000/greet?name=Joel&times=3 | the greeting, 3 times | `request.args` |
| http://localhost:5000/api/fruits | a JSON list | `jsonify()` |
| http://localhost:5000/api/users/1 | `{"id": 1, "name": "Alice"}` | JSON + lookup |
| http://localhost:5000/api/users/99 | `{"error": "User not found"}` | **404** status code |
| http://localhost:5000/nope | Flask's own 404 page | no route matches |

You can also test from the terminal with `curl` (use a second terminal window —
the first one is busy running the server):

```bash
curl http://localhost:5000/hello/Joel
curl -i http://localhost:5000/api/users/99     # -i shows the status code too
```

---

## Experiments

Small changes to make, to prove to yourself how it works. `debug=True` means
the server reloads the moment you save — just refresh the browser.

1. Change `"Hello, World!"` to your own message. Save, refresh.
2. Add a new route `/joke` that returns a joke.
3. Change `/square` to `/cube` and make the maths match.
4. Add a route `/multiply/<int:a>/<int:b>`.
5. Add yourself to the `users` dictionary and visit your own id.
6. **Break it on purpose:** change `return f"Hello, {name}!"` to
   `return f"Hello, {nmae}!"` and refresh. Read the error page — that's what
   `debug=True` is for. Then fix it.

---

## Common problems

| What you see | What's wrong | Fix |
|---|---|---|
| `ModuleNotFoundError: No module named 'flask'` | Flask isn't installed (or the venv isn't active) | `pip install flask` |
| **403 Forbidden on every page (macOS)** | Apple's AirPlay Receiver owns port 5000, not Flask | use `app.run(debug=True, port=5001)`, or turn AirPlay Receiver off in System Settings → General → AirDrop & Handoff |
| `Address already in use` | an older server is still running | `Ctrl+C` it, or use a different port |
| `404 Not Found` on a URL you wrote | path typo, or the route isn't `@app.route`-decorated | check the spelling of the path |
| Browser shows nothing / spinner | the server isn't running | check the terminal, run `python app.py` |
| Your change doesn't appear | the file wasn't saved, or `debug=True` is missing | save, and check the terminal for "Restarting with stat" |

---

## The one idea to take away

A route handler is **just a function**. Everything you already know applies —
parameters, `return`, `if`/`else`, dictionaries, f-strings. The only new part is
that the browser is the one calling your function, and the URL is how it passes
the arguments.

```python
# Before: you call the function
def greet(name):
    return f"Hello, {name}!"

greet("Joel")


# Now: the browser calls the function, via a URL
@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}!"

# visiting /hello/Joel  ->  Flask calls hello("Joel")  ->  you see the result
```

`print()` goes to your terminal. `return` goes to the browser. That distinction
matters more here than it ever did before.

---

## Next

Returning strings gets awkward the moment a page is more than a few lines.
`examples/flask_templates/` picks up here and shows how to return real HTML
pages with `render_template()`.
