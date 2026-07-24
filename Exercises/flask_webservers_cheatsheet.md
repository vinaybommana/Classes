# Web Servers & Flask Cheatsheet

---

## 1. What is a Web Server?

A **web server** is a program that listens for requests from clients (like web browsers) and sends back responses. It's like a restaurant:

| Restaurant Analogy | Web Concept |
|---|---|
| Customer walks in | Client (browser) connects |
| Customer places an order | Client sends a **request** |
| Kitchen prepares food | Server **processes** the request |
| Waiter brings the food | Server sends a **response** |
| Menu tells what's available | **Routes** define what the server can handle |

### How It Works (The Big Picture)

```
 Browser (Client)                         Server (Your Python Code)
 ┌──────────────┐    HTTP Request         ┌──────────────────┐
 │              │  ──────────────────────► │                  │
 │  Types URL   │   GET /hello            │  Receives request │
 │  or clicks   │                         │  Finds matching   │
 │  a link      │   HTTP Response         │  function (route) │
 │              │  ◄────────────────────── │  Runs function    │
 │  Displays    │   "Hello, World!"       │  Sends response   │
 └──────────────┘                         └──────────────────┘
```

### Key Points

- A server is just a program that **runs continuously**, waiting for requests.
- You already know how to write functions that take input and return output — a web server is the same idea, but the input comes from a browser and the output goes back to it.
- The communication happens over **HTTP** (HyperText Transfer Protocol).

---

## 2. HTTP — The Language of the Web

**HTTP** is the protocol (set of rules) that browsers and servers use to communicate. Every interaction is a **request-response** pair.

### HTTP Request

When your browser visits `http://localhost:5000/hello`, it sends a request like:

```
GET /hello HTTP/1.1
Host: localhost:5000
```

The key parts:

| Part | What it is | Example |
|---|---|---|
| **Method** | What action to perform | `GET`, `POST`, `PUT`, `DELETE` |
| **Path** | Which resource to access | `/hello`, `/users`, `/about` |
| **Headers** | Extra info (metadata) | `Host: localhost:5000` |
| **Body** | Data sent with the request (optional) | Form data, JSON |

### HTTP Methods

| Method | Purpose | Example Use |
|---|---|---|
| `GET` | **Read** / retrieve data | View a webpage, get user info |
| `POST` | **Create** / send data | Submit a form, create an account |
| `PUT` | **Update** / replace data | Update a profile |
| `DELETE` | **Remove** data | Delete an account |

Think of it like file operations you already know:

| File Operation | HTTP Equivalent |
|---|---|
| Reading a file (`"r"`) | `GET` — retrieve information |
| Writing a file (`"w"`) | `POST` / `PUT` — send/update information |
| Deleting a file | `DELETE` — remove information |

### HTTP Response

The server sends back:

```
HTTP/1.1 200 OK
Content-Type: text/html

Hello, World!
```

| Part | What it is | Example |
|---|---|---|
| **Status Code** | Did it work? | `200`, `404`, `500` |
| **Headers** | Metadata about the response | `Content-Type: text/html` |
| **Body** | The actual content | HTML, JSON, plain text |

### Common Status Codes

| Code | Meaning | When You See It |
|---|---|---|
| `200` | OK | Everything worked |
| `201` | Created | New resource created successfully |
| `400` | Bad Request | Client sent invalid data |
| `404` | Not Found | The URL doesn't exist on the server |
| `405` | Method Not Allowed | Used GET when only POST is allowed, etc. |
| `500` | Internal Server Error | Something crashed on the server |

### Key Points

- Every HTTP interaction is a **request** followed by a **response**.
- The **method** tells the server what you want to do; the **path** tells it what you want to do it to.
- Status codes are how the server says "it worked" (`2xx`), "you messed up" (`4xx`), or "I messed up" (`5xx`).

---

## 3. What is Flask?

**Flask** is a Python library (called a "micro-framework") that makes it easy to build web servers. It handles all the HTTP plumbing so you can focus on writing Python functions.

### Installing Flask

```bash
pip install flask
```

### Your First Flask App

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
```

Save this as `app.py` and run it:

```bash
python app.py
```

Then open your browser and go to: `http://localhost:5000/`

You'll see: **Hello, World!**

### Breaking It Down

| Line | What It Does |
|---|---|
| `from flask import Flask` | Imports the Flask class |
| `app = Flask(__name__)` | Creates a Flask application instance |
| `@app.route("/")` | A **decorator** — maps the URL `/` to the function below |
| `def home():` | A regular Python function (called a **view function**) |
| `return "Hello, World!"` | The string sent back to the browser as the response |
| `app.run(debug=True)` | Starts the server; `debug=True` auto-reloads on code changes |

### Key Points

- Flask turns your Python functions into web endpoints.
- The `@app.route()` decorator is the glue between a **URL** and a **function**.
- `debug=True` is useful during development — it shows error details and reloads when you save.

---

## 4. Routes — Mapping URLs to Functions

A **route** tells Flask: "When someone visits this URL, run this function." This is just like how you used functions before — but now the "caller" is a web browser.

### Basic Routes

```python
@app.route("/")
def home():
    return "Welcome to the home page!"

@app.route("/about")
def about():
    return "This is the about page."

@app.route("/contact")
def contact():
    return "Contact us at hello@example.com"
```

| URL Visited | Function Called | Response |
|---|---|---|
| `localhost:5000/` | `home()` | "Welcome to the home page!" |
| `localhost:5000/about` | `about()` | "This is the about page." |
| `localhost:5000/contact` | `contact()` | "Contact us at hello@example.com" |

### How This Connects to What You Know

```python
# Before Flask — calling functions directly
def greet(name):
    return f"Hello, {name}!"

result = greet("Alice")    # You call the function in code


# With Flask — the browser calls the function via a URL
@app.route("/greet")
def greet():
    return "Hello, visitor!"
# Browser visits /greet → Flask calls greet() → response sent back
```

### Key Points

- Each route needs a **unique URL path** and a **unique function name**.
- The function must **return** something (a string, HTML, JSON) — this is the response.
- Remember `return` vs `print` from functions? Here it matters even more — `print` goes to your terminal, `return` goes to the browser.

---

## 5. Dynamic Routes — URLs with Variables

Just like functions can accept **parameters**, routes can have **variable parts** in the URL.

### Syntax

```python
@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}!"
```

| URL Visited | `name` value | Response |
|---|---|---|
| `/hello/Alice` | `"Alice"` | "Hello, Alice!" |
| `/hello/Bob` | `"Bob"` | "Hello, Bob!" |
| `/hello/Charlie` | `"Charlie"` | "Hello, Charlie!" |

### Type Converters

By default, URL variables are strings. You can specify types:

```python
@app.route("/square/<int:number>")
def square(number):
    return f"{number} squared is {number ** 2}"

@app.route("/price/<float:amount>")
def price(amount):
    return f"The price is ${amount:.2f}"
```

| Converter | What it does | Example |
|---|---|---|
| `<name>` | String (default) | `/hello/Alice` → `"Alice"` |
| `<int:name>` | Integer | `/square/5` → `5` |
| `<float:name>` | Float | `/price/9.99` → `9.99` |

### Multiple Variables

```python
@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return f"{a} + {b} = {a + b}"
```

Visiting `/add/3/5` returns: `3 + 5 = 8`

### Key Points

- Dynamic routes use `<variable_name>` in the URL — Flask extracts the value and passes it to your function as a parameter.
- This is exactly like function parameters — the URL provides the arguments.
- Use type converters (`int:`, `float:`) to automatically convert URL segments to the right type.

---

## 6. HTTP Methods in Flask

By default, a route only responds to `GET` requests. You can allow other methods:

### Handling GET and POST

```python
from flask import Flask, request

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        return f"Logging in as {username}..."
    else:
        return """
            <form method="POST">
                <input name="username" placeholder="Username">
                <input name="password" type="password" placeholder="Password">
                <button type="submit">Login</button>
            </form>
        """
```

### How It Works

| Step | What Happens |
|---|---|
| 1. Browser visits `/login` | Sends a `GET` request |
| 2. Server returns the HTML form | User sees the form |
| 3. User fills in form and clicks Submit | Browser sends a `POST` request with form data |
| 4. Server reads the form data | Processes login |

### The `request` Object

Flask gives you a `request` object to access everything about the incoming request:

| Attribute | What It Contains | Example |
|---|---|---|
| `request.method` | The HTTP method | `"GET"` or `"POST"` |
| `request.form` | Form data (from POST) | `request.form["username"]` |
| `request.args` | Query parameters (from URL) | `request.args.get("q")` |
| `request.json` | JSON body data | `request.json["key"]` |

### Query Parameters

Query parameters come after `?` in the URL: `/search?q=python&page=1`

```python
@app.route("/search")
def search():
    query = request.args.get("q", "")
    page = request.args.get("page", 1, type=int)
    return f"Searching for '{query}' on page {page}"
```

### Key Points

- Specify allowed methods with `methods=["GET", "POST"]`.
- Use `request.form` for form submissions (POST) and `request.args` for URL query parameters (GET).
- `request.args.get("key", default)` is safer than `request.args["key"]` — it won't crash if the key is missing (similar to `dict.get()`).

---

## 7. Returning JSON — Building APIs

Instead of returning HTML for browsers, you can return **JSON** for other programs to consume. This is how APIs work.

### Returning JSON

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/user")
def get_user():
    user = {
        "name": "Alice",
        "age": 25,
        "city": "NYC"
    }
    return jsonify(user)
```

Response:
```json
{"name": "Alice", "age": 25, "city": "NYC"}
```

### Returning a List of Items

```python
@app.route("/api/fruits")
def get_fruits():
    fruits = [
        {"name": "Apple", "color": "Red"},
        {"name": "Banana", "color": "Yellow"},
        {"name": "Grape", "color": "Purple"}
    ]
    return jsonify(fruits)
```

### Connecting to What You Know

JSON looks exactly like Python dictionaries and lists:

| Python | JSON |
|---|---|
| `dict` → `{"key": "value"}` | `{"key": "value"}` |
| `list` → `[1, 2, 3]` | `[1, 2, 3]` |
| `True` / `False` | `true` / `false` |
| `None` | `null` |

### Key Points

- Use `jsonify()` to convert Python dicts/lists to JSON responses.
- JSON APIs are how frontend apps, mobile apps, and other services talk to your server.
- JSON is just dictionaries and lists in a text format — you already know how to work with them.

---

## 8. Status Codes — Telling the Client What Happened

You can return a status code along with your response:

```python
@app.route("/api/user/<int:user_id>")
def get_user(user_id):
    users = {1: "Alice", 2: "Bob", 3: "Charlie"}

    if user_id in users:
        return jsonify({"name": users[user_id]}), 200
    else:
        return jsonify({"error": "User not found"}), 404
```

### Common Patterns

```python
# Success
return jsonify({"message": "Created!"}), 201

# Client error
return jsonify({"error": "Missing required field"}), 400

# Not found
return jsonify({"error": "Not found"}), 404
```

### Key Points

- Return a tuple of `(response, status_code)` to set the status code.
- If you don't specify a status code, Flask defaults to `200` (OK).
- Use meaningful status codes — they help clients know what happened without parsing the response body.

---

## 9. A Complete Example — Todo API

Putting it all together — a simple in-memory Todo API using everything above:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

todos = []
next_id = 1


@app.route("/api/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)


@app.route("/api/todos", methods=["POST"])
def create_todo():
    global next_id

    data = request.json
    if not data or "task" not in data:
        return jsonify({"error": "task is required"}), 400

    todo = {
        "id": next_id,
        "task": data["task"],
        "done": False
    }
    todos.append(todo)
    next_id += 1

    return jsonify(todo), 201


@app.route("/api/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    data = request.json

    for todo in todos:
        if todo["id"] == todo_id:
            todo["task"] = data.get("task", todo["task"])
            todo["done"] = data.get("done", todo["done"])
            return jsonify(todo)

    return jsonify({"error": "Todo not found"}), 404


@app.route("/api/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            todos.pop(i)
            return jsonify({"message": "Deleted"})

    return jsonify({"error": "Todo not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
```

### Testing with curl

```bash
# Get all todos
curl http://localhost:5000/api/todos

# Create a todo
curl -X POST http://localhost:5000/api/todos \
  -H "Content-Type: application/json" \
  -d '{"task": "Learn Flask"}'

# Update a todo
curl -X PUT http://localhost:5000/api/todos/1 \
  -H "Content-Type: application/json" \
  -d '{"done": true}'

# Delete a todo
curl -X DELETE http://localhost:5000/api/todos/1
```

### What This Demonstrates

| Concept | Where It's Used |
|---|---|
| Routes | Each endpoint has a URL path |
| HTTP Methods | GET, POST, PUT, DELETE for different actions |
| Dynamic routes | `<int:todo_id>` to target specific todos |
| Request data | `request.json` to read incoming JSON |
| JSON responses | `jsonify()` for all responses |
| Status codes | `201` for created, `404` for not found, `400` for bad input |
| Lists and dicts | `todos` list stores dict items — data structures you already know |
| Global state | `global next_id` — remember scope from functions? |

---

## 10. Running and Debugging

### Starting the Server

```python
if __name__ == "__main__":
    app.run(debug=True)
```

| Option | What It Does | Default |
|---|---|---|
| `debug=True` | Auto-reload on changes + show error pages | `False` |
| `host="0.0.0.0"` | Allow connections from other devices | `"127.0.0.1"` |
| `port=8080` | Change the port number | `5000` |

### What `if __name__ == "__main__"` Means

Remember from modularisation — this check ensures the server only starts when you run the file directly, not when it's imported as a module.

### Debug Mode

When `debug=True`:
- The server **restarts automatically** when you save changes to your code.
- If your code crashes, Flask shows a **detailed error page** in the browser instead of a generic "500 Internal Server Error".
- **Never use `debug=True` in production** — it exposes internal details.

---

## Quick Reference

| Concept | Syntax | Example |
|---|---|---|
| Create app | `app = Flask(__name__)` | — |
| Basic route | `@app.route("/path")` | `@app.route("/hello")` |
| Dynamic route | `@app.route("/<var>")` | `@app.route("/user/<name>")` |
| Type converter | `<int:var>` | `@app.route("/id/<int:n>")` |
| Allow methods | `methods=["GET", "POST"]` | `@app.route("/login", methods=...)` |
| Read form data | `request.form["key"]` | `request.form["username"]` |
| Read query params | `request.args.get("key")` | `request.args.get("q", "")` |
| Read JSON body | `request.json` | `request.json["task"]` |
| Return JSON | `jsonify(data)` | `return jsonify({"ok": True})` |
| Set status code | `return data, code` | `return jsonify(err), 404` |
| Run server | `app.run(debug=True)` | — |

---

## Concepts Map — What You Already Know → Flask

| You Already Know | Flask Equivalent |
|---|---|
| **Functions** → take input, return output | **Route handlers** → take requests, return responses |
| **Parameters** → `def greet(name)` | **URL variables** → `@app.route("/greet/<name>")` |
| **Return values** → `return result` | **Responses** → `return "Hello"` or `return jsonify(data)` |
| **Dictionaries** → `{"key": "value"}` | **JSON** → the data format APIs use |
| **if/elif/else** → branching logic | **Method checks** → `if request.method == "POST"` |
| **Lists of dicts** → `[{"name": "Alice"}, ...]` | **API data** → what your endpoints return |
| **File I/O** → reading/writing data | **HTTP** → reading requests / writing responses |
| **Scope** → local vs global variables | **App state** → data stored across requests |
| **`__name__`** → module name check | **`Flask(__name__)`** → tells Flask where to find resources |
