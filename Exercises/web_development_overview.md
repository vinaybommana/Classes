# Web Application Development — Concepts & Techniques

An overview of how the web works and what goes into building a web application, before writing any code.

---

## 1. How the Web Works

When you type a URL into your browser and hit Enter, a chain of events happens in milliseconds:

```
 You (Browser)                Internet               Server (Someone's Computer)
 ┌────────────┐              ┌────────┐              ┌──────────────────┐
 │ Type URL   │──────────────│        │──────────────│ Receives request │
 │            │  1. Request  │ Network│  2. Arrives  │ Finds the right  │
 │            │              │        │              │ code to run      │
 │ See the    │──────────────│        │──────────────│ Sends back data  │
 │ web page   │  4. Renders  │        │  3. Response │ (HTML, JSON, etc)│
 └────────────┘              └────────┘              └──────────────────┘
```

### Key Terms

| Term | What It Means | Analogy |
|---|---|---|
| **Client** | The program making the request (usually a browser) | Customer at a restaurant |
| **Server** | The program responding to requests | The kitchen + waitstaff |
| **URL** | The address of a resource on the web | The restaurant's street address |
| **HTTP** | The protocol (rules) for how clients and servers talk | The language the customer and waiter both speak |
| **Request** | A message from client to server asking for something | "I'd like the pasta, please" |
| **Response** | A message from server to client with the result | The plate of pasta arriving |

---

## 2. URLs — Anatomy of a Web Address

A URL (Uniform Resource Locator) tells the browser exactly where to go and what to ask for.

```
https://www.example.com:443/products/shoes?color=red&size=10#reviews
──┬──   ───────┬───────  ┬  ─────┬──────  ────────┬────────  ───┬──
  │            │         │       │                │             │
scheme       host       port    path          query string   fragment
```

| Part | Purpose | Example |
|---|---|---|
| **Scheme** | How to connect (protocol) | `https` (secure), `http` (not secure) |
| **Host** | Which server to talk to | `www.example.com`, `localhost` |
| **Port** | Which "door" on the server | `443` (HTTPS default), `80` (HTTP), `5000` (Flask default) |
| **Path** | Which resource to request | `/products/shoes` |
| **Query String** | Extra parameters (key=value pairs) | `?color=red&size=10` |
| **Fragment** | A section within the page (browser-only) | `#reviews` |

### localhost

During development, your server runs on your **own computer**. The special hostname `localhost` (or `127.0.0.1`) means "this machine." So `http://localhost:5000/hello` means:

> "Use HTTP to connect to my own computer on port 5000 and request `/hello`."

---

## 3. Client vs Server — Frontend vs Backend

A web application has two halves:

```
┌─────────────────────────────────┐     ┌─────────────────────────────────┐
│          FRONTEND               │     │           BACKEND               │
│        (Client-Side)            │     │         (Server-Side)           │
│                                 │     │                                 │
│  What the user sees and         │     │  What runs on the server,       │
│  interacts with in the browser  │     │  hidden from the user           │
│                                 │     │                                 │
│  • HTML  → structure/content    │     │  • Python (Flask) → logic       │
│  • CSS   → styling/appearance   │     │  • Database → stores data       │
│  • JavaScript → interactivity   │     │  • File system → reads/writes   │
│                                 │     │  • Authentication → who are you │
└─────────────────────────────────┘     └─────────────────────────────────┘
         ▲                                          ▲
         │              HTTP Request                │
         │  ◄────────────────────────────────────── │
         │              HTTP Response               │
         │  ──────────────────────────────────────► │
```

| | Frontend | Backend |
|---|---|---|
| **Runs on** | The user's browser | The server (your computer or a cloud machine) |
| **Languages** | HTML, CSS, JavaScript | Python, Java, Go, Ruby, etc. |
| **What it does** | Displays pages, handles clicks, shows data | Processes logic, talks to databases, sends responses |
| **Who sees it** | The user (anyone can "View Source" in a browser) | Only the developer — code is private |
| **Our focus** | We'll return simple HTML and JSON | We'll write Python (Flask) for this |

### What We'll Focus On

In this course, we focus on the **backend** — writing Python code that handles requests and returns responses. We'll return simple HTML strings or JSON data, not build complex frontends.

---

## 4. HTTP — The Protocol

HTTP (HyperText Transfer Protocol) is a set of rules for how clients and servers communicate. Every interaction follows the same pattern: **request → response**.

### HTTP Request — What the Client Sends

```
GET /products?category=shoes HTTP/1.1
Host: www.example.com
Accept: text/html
```

A request has:

| Part | What it tells the server |
|---|---|
| **Method** | What action to perform (`GET`, `POST`, `PUT`, `DELETE`) |
| **Path** | Which resource (`/products`, `/users/5`, `/login`) |
| **Headers** | Metadata — who I am, what format I accept, cookies, etc. |
| **Body** (optional) | Data being sent — form submissions, JSON payloads |

### HTTP Methods — The Four Main Actions

| Method | Purpose | Real-World Example | Like File I/O |
|---|---|---|---|
| `GET` | Read / retrieve | View a product page | Reading a file (`"r"`) |
| `POST` | Create / submit | Submit a registration form | Writing a new file (`"w"`) |
| `PUT` | Update / replace | Edit your profile | Overwriting a file (`"w"`) |
| `DELETE` | Remove | Delete your account | Deleting a file |

These map to **CRUD** — the four basic operations on any data:

| CRUD | HTTP Method | SQL (databases) | Meaning |
|---|---|---|---|
| **C**reate | `POST` | `INSERT` | Make something new |
| **R**ead | `GET` | `SELECT` | Get existing data |
| **U**pdate | `PUT` | `UPDATE` | Change existing data |
| **D**elete | `DELETE` | `DELETE` | Remove data |

### HTTP Response — What the Server Sends Back

```
HTTP/1.1 200 OK
Content-Type: text/html

<h1>Welcome!</h1>
```

A response has:

| Part | What it tells the client |
|---|---|
| **Status Code** | Did it work? (`200 OK`, `404 Not Found`, `500 Server Error`) |
| **Headers** | Metadata — content type, caching rules, cookies |
| **Body** | The actual content — HTML page, JSON data, image, etc. |

### Status Codes at a Glance

| Range | Category | Meaning |
|---|---|---|
| `1xx` | Informational | "Hold on, still working..." |
| `2xx` | Success | "Here you go, it worked!" |
| `3xx` | Redirect | "Go look somewhere else" |
| `4xx` | Client Error | "You made a mistake" |
| `5xx` | Server Error | "I (the server) messed up" |

Common ones you'll use:

| Code | Name | When |
|---|---|---|
| `200` | OK | Request succeeded |
| `201` | Created | New resource was created |
| `400` | Bad Request | Client sent invalid data |
| `404` | Not Found | URL doesn't exist |
| `405` | Method Not Allowed | Wrong HTTP method for this URL |
| `500` | Internal Server Error | Server code crashed |

---

## 5. Data Formats — How Data Travels

When a server sends data to a client (or vice versa), it needs to be in a format both sides understand.

### HTML — For Humans (Browsers)

HTML (HyperText Markup Language) is the language browsers understand for displaying web pages.

```html
<html>
  <body>
    <h1>Hello, World!</h1>
    <p>This is a paragraph.</p>
    <ul>
      <li>Item 1</li>
      <li>Item 2</li>
    </ul>
  </body>
</html>
```

HTML uses **tags** (`<h1>`, `<p>`, `<ul>`) to define the structure of a page. The browser reads these tags and renders them visually.

### JSON — For Programs (APIs)

JSON (JavaScript Object Notation) is the standard format for programs to exchange data. It looks almost identical to Python dictionaries and lists:

```json
{
    "name": "Alice",
    "age": 25,
    "hobbies": ["reading", "coding"],
    "address": {
        "city": "NYC",
        "zip": "10001"
    }
}
```

| Python Type | JSON Equivalent |
|---|---|
| `dict` | `{ }` object |
| `list` | `[ ]` array |
| `str` | `"string"` |
| `int`, `float` | `number` |
| `True` / `False` | `true` / `false` |
| `None` | `null` |

### When to Use Which?

| Situation | Format | Why |
|---|---|---|
| Browser displays a page | HTML | Browsers render HTML visually |
| Mobile app fetches data | JSON | Apps parse JSON into native objects |
| Two servers communicate | JSON | Language-neutral, easy to parse |
| API response | JSON | Standard for APIs |

---

## 6. APIs — How Programs Talk to Each Other

An **API** (Application Programming Interface) is a way for programs to communicate with each other, just like a web page is a way for servers to communicate with humans.

### Web Page vs API

| | Web Page | API |
|---|---|---|
| **Client** | Human using a browser | Another program (app, script, service) |
| **Response format** | HTML (visual) | JSON (data) |
| **Interaction** | Click links, fill forms | Send HTTP requests programmatically |
| **Example URL** | `example.com/products` (shows a page) | `example.com/api/products` (returns JSON) |

### REST — A Set of Conventions for APIs

**REST** (Representational State Transfer) is a widely used pattern for designing APIs. It combines URLs and HTTP methods in a predictable way:

| Action | Method | URL | Description |
|---|---|---|---|
| List all users | `GET` | `/api/users` | Get all users |
| Get one user | `GET` | `/api/users/5` | Get user with ID 5 |
| Create a user | `POST` | `/api/users` | Create a new user (data in body) |
| Update a user | `PUT` | `/api/users/5` | Update user 5 (data in body) |
| Delete a user | `DELETE` | `/api/users/5` | Delete user 5 |

The pattern: **the URL identifies the resource**, the **method identifies the action**.

### Connecting to What You Know

Think of an API as a **set of functions** that another program can call over the internet:

```python
# Regular Python function
def get_user(user_id):
    return users[user_id]

result = get_user(5)        # called directly in code


# API endpoint (same idea, but called via HTTP)
# GET /api/users/5          → called by any program, over the network
# Response: {"name": "Alice", "age": 25}
```

---

## 7. Web Frameworks — Why Not Build From Scratch?

A **web framework** is a library that handles the repetitive, low-level plumbing of web development so you can focus on your application's logic.

### What a Framework Handles For You

| Task | Without a Framework | With Flask |
|---|---|---|
| Listen for connections | Write socket code | `app.run()` |
| Parse HTTP requests | Manually split raw text | `request.method`, `request.form` |
| Map URLs to code | Giant if/elif chain | `@app.route("/path")` |
| Send HTTP responses | Manually format headers + body | `return "Hello"` |
| Handle errors | try/except everything | Built-in error handlers |

### Python Web Frameworks

| Framework | Size | Best For |
|---|---|---|
| **Flask** | Micro (small, flexible) | Learning, small-to-medium apps, APIs |
| **Django** | Full (batteries included) | Large apps with admin panels, auth, ORM |
| **FastAPI** | Modern (async, fast) | High-performance APIs |

We use **Flask** because it's the simplest — it gets out of your way and lets you see how things work.

---

## 8. Architecture — How a Web App is Structured

A typical web application has three layers:

```
┌────────────────────────────────────────────────┐
│                   CLIENT                        │
│          (Browser / Mobile App)                 │
│                                                 │
│  Sends requests, displays responses             │
└───────────────────┬────────────────────────────┘
                    │ HTTP
                    ▼
┌────────────────────────────────────────────────┐
│                APPLICATION                      │
│            (Flask / Python)                     │
│                                                 │
│  Routes → Functions → Business Logic            │
│  Receives requests, processes them,             │
│  returns responses                              │
└───────────────────┬────────────────────────────┘
                    │ Read / Write
                    ▼
┌────────────────────────────────────────────────┐
│                 DATA STORE                      │
│        (Database / Files / Memory)              │
│                                                 │
│  Stores persistent data: users, products,       │
│  orders, settings                               │
└────────────────────────────────────────────────┘
```

### Where Our Concepts Fit

| Layer | What You Already Know | How It Applies |
|---|---|---|
| **Client** | — (we're not building frontends) | We'll use a browser or `curl` to test |
| **Application** | Functions, conditionals, loops | Route handlers are just functions |
| **Data Store** | Dictionaries, lists, file I/O | We'll start with in-memory dicts, then files |

### Starting Simple

We don't need all three layers to start. Our first apps will keep data in **Python variables** (lists and dictionaries in memory). This means data disappears when the server restarts — but it lets us focus on the web concepts without worrying about databases yet.

```
Progression:
1. Data in variables (lists/dicts)     ← we start here
2. Data in files (CSV, JSON, txt)      ← you already know this
3. Data in a database (SQLite, etc.)   ← later
```

---

## 9. Development Workflow

Building a web application follows a cycle:

```
    Write Code
        │
        ▼
    Start Server
        │
        ▼
    Test in Browser ──── Does it work? ──── Yes ──► Move to next feature
        │                                   │
        No                                  │
        │                                   │
        ▼                                   │
    Read Error Message                      │
        │                                   │
        ▼                                   │
    Fix the Bug ────────────────────────────┘
```

### Tools You'll Use

| Tool | What It Does | Example |
|---|---|---|
| **Text editor / IDE** | Write your Python code | VS Code, PyCharm |
| **Terminal** | Run the server, see print output and errors | `python app.py` |
| **Browser** | Test GET requests by visiting URLs | `http://localhost:5000/hello` |
| **curl** | Test any HTTP method from the terminal | `curl -X POST localhost:5000/api/todos` |
| **print()** | Debug by printing to your terminal | `print(request.form)` |

### curl — Your API Testing Tool

`curl` is a command-line tool for making HTTP requests. It's useful for testing endpoints that aren't simple GET requests:

```bash
# GET request (same as visiting in browser)
curl http://localhost:5000/api/users

# POST request with JSON data
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "age": 25}'

# PUT request
curl -X PUT http://localhost:5000/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{"age": 26}'

# DELETE request
curl -X DELETE http://localhost:5000/api/users/1
```

| curl Flag | What It Does |
|---|---|
| `-X METHOD` | Sets the HTTP method (POST, PUT, DELETE) |
| `-H "Header"` | Adds a header (like Content-Type) |
| `-d 'data'` | Sends data in the request body |

---

## 10. Putting It All Together — The Big Picture

Here's how everything connects when a user interacts with a web application:

```
1. User types http://localhost:5000/api/todos in browser

2. Browser creates an HTTP request:
   GET /api/todos HTTP/1.1
   Host: localhost:5000

3. Flask receives the request and checks its routes:
   @app.route("/api/todos") → found! → calls get_todos()

4. The get_todos() function runs:
   - Reads data from a list/dict/file
   - Processes it (filtering, sorting, etc.)
   - Returns the result as JSON

5. Flask packages the return value into an HTTP response:
   HTTP/1.1 200 OK
   Content-Type: application/json
   [{"id": 1, "task": "Learn Flask", "done": false}]

6. Browser receives the response and displays the JSON
```

### Concepts Map

| Concept | What It Is | Where It Fits |
|---|---|---|
| **HTTP** | The communication protocol | The rules for how requests and responses work |
| **URL** | The address of a resource | Tells the server what the client wants |
| **Methods** | GET, POST, PUT, DELETE | Tells the server what action to perform |
| **Status Codes** | 200, 404, 500, etc. | The server's way of saying what happened |
| **HTML** | Markup language for pages | What browsers render for humans |
| **JSON** | Data format for APIs | What programs use to exchange data |
| **API** | Interface for programs | URLs + methods that return JSON |
| **REST** | API design conventions | A pattern for organizing API endpoints |
| **Framework** | Library for web plumbing | Flask — handles HTTP so you write Python |
| **Client** | The requester | Browser, mobile app, curl, another server |
| **Server** | The responder | Your Flask application |
| **Route** | URL → function mapping | `@app.route("/path")` → `def handler()` |
