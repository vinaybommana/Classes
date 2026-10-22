# HTML Forms & Basic CSS Cheatsheet

Everything we have shown the browser so far has been **one-way**:

```
 server  ──────────────►  browser        (we send a page, they read it)
```

A **form** is how the browser talks back:

```
 browser ──────────────►  server         (they fill it in, we receive it)
```

This is the missing half. Once a form can reach your Python, you can build a
login, a signup, a search box, a comment section — the whole interactive web.

---

## 1. The Three Ideas

A form is only three tags. Learn these and every form on the internet makes sense.

```html
<form action="/login" method="POST">
  <input name="username">
  <button>Send</button>
</form>
```

| Tag | Job | Analogy |
|---|---|---|
| `<form>` | the envelope — **where** to send it and **how** | the address on a parcel |
| `<input>` | the fields — what the user types | what goes inside the parcel |
| `<button>` | the stamp — send it | dropping it in the postbox |

### Key Points

- A form sends data **to a URL**, using an **HTTP method**. That's it.
- The browser builds the request for you. You never write networking code.
- Pressing the button causes a **page navigation** — the browser leaves the
  current page and loads the response.

---

## 2. `name=` — The Most Important Attribute

```html
<input name="username">
       ^^^^^^^^^^^^^^^
       this is the label on the box
```

An input **without** a `name` is **not sent at all**. The browser silently
ignores it. This is the single most common reason a form "doesn't work".

Think of the browser building a dictionary as the user types:

```python
{"username": "whatever they typed"}
```

The `name=` is the **key**. The typed text is the **value**. In Flask you read
it back with exactly that key:

```python
request.form["username"]
```

### The chain, end to end

```
 HTML                      what travels                 Python
 ────                      ────────────                 ──────
 <input name="username">   username=joel         request.form["username"]
                 ▲                ▲                                ▲
                 └────────────────┴────────────────────────────────┘
                        these three strings must match
```

### Key Points

- No `name`, no data. Check this first when a field "disappears".
- `request.form` behaves like a **dictionary** — the same `[]` and `.get()`
  you already know.

---

## 3. `action` and `method` — Where and How

```html
<form action="/login" method="POST">
```

| Attribute | Means | If you leave it out |
|---|---|---|
| `action` | **which URL** receives the data | sends to the page you're already on |
| `method` | **how** the data travels | defaults to `GET` |

Leaving `action` out is common and useful — one Flask route can show the form
*and* receive it.

### GET vs POST

This is the same GET/POST from the Flask cheatsheet, seen from the browser side.

| | `GET` | `POST` |
|---|---|---|
| Data goes in | the **URL** | the request **body** |
| Looks like | `/search?query=shoes` | `/login` (clean URL) |
| Visible in address bar | yes | no |
| Saved in browser history | yes | no |
| Can be bookmarked / shared | yes | no |
| Safe to re-run by refreshing | yes | no — browser warns "resubmit?" |
| Read in Flask with | `request.args` | `request.form` |
| Use it for | searches, filters, page numbers | logins, signups, anything that **changes** something |

```html
<!-- GET: the data ends up in the URL, in plain sight -->
<form action="/search" method="GET">
  <input name="query">
  <button>Search</button>
</form>
<!-- submits to:  /search?query=shoes  -->

<!-- POST: the data travels in the body -->
<form action="/login" method="POST">
  <input name="password" type="password">
  <button>Log in</button>
</form>
<!-- submits to:  /login   (nothing in the URL) -->
```

### Key Points

- **Reading something? `GET`. Changing something? `POST`.**
- A login form is **always** `POST`. You do not want `?password=hunter2`
  sitting in the browser history of a shared laptop.
- `POST` is not *secure*, just not *visible*. Only HTTPS makes it secret.

---

## 4. Labels — and the `id` vs `name` Trap

```html
<label for="email">Email address</label>
<input id="email" name="email" type="email">
```

A **placeholder** is grey text that vanishes the moment you type. If the user
looks away mid-form, they have lost the question. A **label** is permanent.

> Use labels for the question. Use placeholders for an example
> (`e.g. joel@gmail.com`).

### Why `for` / `id` must match

Clicking the **word** then focuses the box — a real usability win on phones,
and it's how screen readers announce the field to blind users.

### The trap

There are now two identifier attributes that do completely different jobs:

| Attribute | Who it's for | Used by |
|---|---|---|
| `id="email"` | the **browser** | `<label for>`, CSS, JavaScript |
| `name="email"` | the **server** | `request.form["email"]` |

They're usually spelled the same, which is exactly why people confuse them.
**Only `name` is ever sent over the network.**

---

## 5. The Input Zoo

Every field below is the same `<input>` tag. What changes is `type=`.

The type decides three things at once: how it looks, what the browser lets you
type, and what keyboard appears on a phone.

```html
<input name="name"     type="text">
<input name="password" type="password">
<input name="email"    type="email">
<input name="age"      type="number" min="1" max="120">
<input name="dob"      type="date">
<input name="role"     type="radio"    value="student">
<input name="likes"    type="checkbox" value="python">
<input name="post_id"  type="hidden"   value="42">
```

| Type | What you get | Arrives in Python as |
|---|---|---|
| `text` | a plain box (the default) | a string |
| `password` | characters shown as dots | a string |
| `email` | refuses to submit without `@`; `@` on phone keyboards | a string |
| `number` | spinner arrows, numeric keyboard, `min`/`max` | **still a string** — `int()` it |
| `date` | a real calendar picker | `"2026-10-14"` (`YYYY-MM-DD`) |
| `radio` | pick exactly one from a group | the chosen `value` |
| `checkbox` | pick any number, including none | the `value`, **or nothing** |
| `hidden` | invisible on the page, still submitted | a string |

### Not inputs, but still fields

```html
<select name="city">
  <option value="">-- choose one --</option>
  <option value="hyd">Hyderabad</option>
  <option value="blr">Bengaluru</option>
</select>

<textarea name="bio" rows="4"></textarea>
```

- `<select>` — a dropdown. The `name` is on the `<select>`, the data is on the
  `<option>`. Use it when the list is long.
- `<textarea>` — multi-line text. It needs a closing tag, and anything between
  the tags becomes the starting text, so keep it empty and on one line.

### Three gotchas worth saying out loud

**1. Radios group by `name`.** Radios that share the same `name` become one
group, and only one can be on. Give them different names and you can tick them
all — this bug catches everybody once.

```html
<label><input name="role" type="radio" value="student" checked> Student</label>
<label><input name="role" type="radio" value="teacher"> Teacher</label>
```

**2. An unticked checkbox sends nothing.** The key is simply *absent*.

```python
request.form["newsletter"]                  # KeyError → 400 Bad Request
"newsletter" in request.form                # True / False   ← do this
request.form.get("newsletter", "")          # safe default   ← or this
```

**3. An empty text box still sends its key**, with an empty value: `email=`.
So "the key exists" does **not** mean "the user typed something":

```python
username = request.form.get("username", "").strip()
if not username:
    ...
```

**Bonus:** a checkbox group sends the same key multiple times. `request.form["likes"]`
gives you only the first. Use `request.form.getlist("likes")` → `["python", "web"]`.

---

## 6. Browser-Side Validation — Free, and Not a Defence

```html
<input name="username" type="text"     required>
<input name="password" type="password" required minlength="4">
<input name="age"      type="number"   min="1" max="120">
```

| Attribute | Effect |
|---|---|
| `required` | browser refuses to submit if empty |
| `minlength` / `maxlength` | character count limits |
| `min` / `max` | numeric limits |
| `pattern` | must match a regular expression |
| `autofocus` | cursor starts in this box |

Try submitting an empty `required` field — the browser stops you with its own
pop-up. No code written.

> ### The whole lesson in security, in one line
>
> **Browser-side checks are a convenience, never a defence.**

Anyone can open developer tools, delete the word `required`, and submit an
empty form — or skip the browser entirely and send the request from a Python
script. **Your server must check the data again when it arrives. Always.**

Same for `type="hidden"`: "the user never sees it" means never sees it *on the
page*. It is right there in View Source, fully editable. Never put a price or a
user id you trust in a hidden field.

---

## 7. What Actually Travels

When the user submits this:

```html
<form action="/login" method="POST">
  <input name="username" value="joel">
  <input name="password" value="secret123">
</form>
```

the browser builds and sends:

```
POST /login HTTP/1.1
Host: localhost:5000
Content-Type: application/x-www-form-urlencoded

username=joel&password=secret123
```

Flask receives that last line and hands it to you as a dictionary:

```python
request.form        # {"username": "joel", "password": "secret123"}
```

Had it been `method="GET"`, the same pairs would have gone in the URL instead:

```
GET /login?username=joel&password=secret123 HTTP/1.1
```

…and you would read them with `request.args` instead of `request.form`.

### Key Points

- `&` separates pairs, `=` separates key from value. That's the whole format.
- Spaces and special characters get **URL-encoded** (`a b` → `a+b`, `@` → `%40`).
  Flask decodes this for you automatically.

---

## 8. Receiving a Form in Flask

One route, both jobs — the pattern you will use every time:

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not username or not password:
            return render_template("login.html", error="Fill in both fields.")

        return f"Welcome, {username}!"

    # GET — just show the empty form
    return render_template("login.html")
```

| The situation | What happens |
|---|---|
| User visits `/login` | `GET` → falls through to the bottom → empty form |
| User submits the form | `POST` → the `if` block runs → data is read |
| `methods=` left off the route | `405 Method Not Allowed` on submit |
| `name=` doesn't match the `[]` key | `400 Bad Request` (a `KeyError` underneath) |

### Key Points

- The route must list **both** methods: `methods=["GET", "POST"]`.
- Prefer `.get()` over `[]` so a missing field gives `""` instead of a 400.
- `.strip()` the text. Users type trailing spaces constantly.

---

## 9. CSS — The Other Half

```
HTML  =  WHAT it is      (a heading, a field, a button)
CSS   =  HOW it looks    (the font, the spacing, the colour)
```

Keeping them apart is the same instinct as keeping `app.py` separate from
`templates/` — logic in one place, presentation in another.

### Anatomy of a rule

```css
button {
  background: #0b5fff;
  color: white;
}
│         │          │
│         │          └── value
│         └───────────── property
└─────────────────────── selector: WHICH tags this applies to
```

Read it as: *"for every `<button>`, set the background to blue and the text to white."*

### Three ways to attach CSS

| Way | How | Verdict |
|---|---|---|
| **Inline** | `<p style="color: red;">` | one-off experiments only — to change all your red text you'd have to find every tag |
| **Internal** | `<style>` block in `<head>` | OK for a single throwaway page; page 2 can't share it |
| **External** | `<link rel="stylesheet" href="style.css">` | **always use this** |

```html
<head>
  <link rel="stylesheet" href="style.css">
</head>
```

One file, every page. Change it once and the whole site updates — and the
browser caches it, so the site loads faster. Same copy-paste-versus-write-a-function
argument you already know from Python.

In Flask, the file goes in `static/` and you link it with `url_for`:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

---

## 10. Selectors — Choosing What to Style

```css
button        { }    /* every <button> on the page           */
.card         { }    /* every tag with class="card"          */
#login-form   { }    /* the one tag with id="login-form"     */
.card input   { }    /* every <input> INSIDE a .card         */
input:focus   { }    /* an input, while the cursor is in it  */
```

| Selector | Symbol | Matches |
|---|---|---|
| **Tag** | *(none)* | every tag of that type |
| **Class** | `.` | every tag with that `class=` — **reusable** |
| **Id** | `#` | the one tag with that `id=` — unique |
| **Descendant** | a space | one inside the other |
| **Pseudo-class** | `:` | a *state*: `:hover`, `:focus`, `:disabled` |

### Class vs id, again

```html
<form class="card">      <!-- as many tags as you like can share this -->
<form id="login-form">   <!-- only one tag on the page may have this  -->
```

A class is a **name you invent** and stick on any tags you want to style
together. Use classes for styling; keep ids for `<label for>` and JavaScript.

```css
.card { border: 1px solid #ddd; }    /* styles both cards, written once */
```

---

## 11. The Box Model — Why Things Are Spaced Oddly

**Every** element on a page is a rectangular box, and each box has four layers:

```
 ┌───────────────────────────────────────┐
 │  margin        (space OUTSIDE)        │
 │  ┌─────────────────────────────────┐  │
 │  │  border     (the visible line)  │  │
 │  │  ┌───────────────────────────┐  │  │
 │  │  │  padding  (space INSIDE)  │  │  │
 │  │  │  ┌─────────────────────┐  │  │  │
 │  │  │  │      content        │  │  │  │
 │  │  │  └─────────────────────┘  │  │  │
 │  │  └───────────────────────────┘  │  │
 │  └─────────────────────────────────┘  │
 └───────────────────────────────────────┘
```

| Property | Where | Mnemonic |
|---|---|---|
| `padding` | **inside** the border | breathing room *around the text* |
| `border` | the visible edge | the line itself |
| `margin` | **outside** the border | distance *to the next element* |

If two elements look too close together, you want `margin`. If text is jammed
against its own border, you want `padding`. Nine out of ten layout questions
are this distinction.

### Units

| Unit | Means | Use for |
|---|---|---|
| `px` | pixels, fixed | borders, tiny precise things |
| `rem` | multiples of the base font size | **almost everything** — spacing, widths |
| `%` | percent of the parent | widths that should flex |

```css
padding: 0.75rem;              /* all four sides            */
padding: 0.5rem 1rem;          /* top+bottom, then left+right */
margin: 0 auto;                /* no top/bottom; auto = centre horizontally */
```

`margin: 0 auto` with a `max-width` is the standard way to centre a page.

---

## 12. A Form Stylesheet, Line by Line

This is enough CSS to make a login form look deliberate. Nothing here is
decorative — every rule fixes a specific default that looks bad.

```css
body {
  font-family: system-ui, sans-serif;  /* use the OS font — instantly modern */
  line-height: 1.6;                    /* default 1.2 is cramped             */
  max-width: 24rem;                    /* stop lines running edge to edge    */
  margin: 2rem auto;                   /* centre the page horizontally       */
  padding: 0 1rem;                     /* breathing room on phones           */
  color: #222;                         /* near-black is softer than #000     */
}

.card {
  border: 1px solid #ddd;
  border-radius: 8px;                  /* rounded corners                    */
  padding: 1.5rem;
  margin-bottom: 1.5rem;
}

label {
  display: block;                      /* ← the important one, see below     */
  margin-top: 1rem;
  font-weight: 600;
}

input {
  display: block;
  width: 100%;                         /* fill the card                      */
  padding: 0.5rem;
  margin-top: 0.25rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;                     /* stops iPhones zooming on focus     */
  box-sizing: border-box;              /* ← see the warning below            */
}

input:focus {
  outline: 2px solid #0b5fff;          /* show which box has the cursor      */
  border-color: #0b5fff;
}

button {
  margin-top: 1.25rem;
  width: 100%;
  padding: 0.6rem;
  font-size: 1rem;
  background: #0b5fff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;                     /* hand cursor — it looks clickable   */
}

button:hover {
  background: #0a4fd6;                 /* feedback on mouse-over             */
}

.error {
  background: #fde8e8;
  border-left: 4px solid #b00020;
  padding: 0.75rem;
  margin-bottom: 1rem;
}
```

### Two rules that do the heavy lifting

**`display: block` on labels and inputs.** By default they are *inline* — they
sit side by side on one line like words in a sentence. `display: block` makes
each one take a full line, which is what a stacked form needs.

**`box-sizing: border-box` on inputs.** Without it, `width: 100%` means *the
content is 100% wide* — then padding and border are added **on top**, and your
input overflows its card. With it, `width: 100%` means *the whole box including
padding and border is 100% wide*, which is what you meant. Many stylesheets set
this on everything:

```css
* { box-sizing: border-box; }
```

### Colours

| Form | Example | Notes |
|---|---|---|
| Named | `red`, `white` | ~140 of them, fine for prototypes |
| Hex | `#0b5fff` | `#RRGGBB`, two hex digits per channel |
| RGB | `rgb(11, 95, 255)` | same thing, decimal |
| RGBA | `rgba(0, 0, 0, 0.5)` | the 4th value is opacity |

Hex is what you'll see most. `#fff` is shorthand for `#ffffff` (white).

---

## 13. The Complete Login Page

Everything above, assembled. This is the file we turn into a Flask template next.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Log in</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <form class="card" action="/login" method="POST">
    <h2>Log in</h2>

    <label for="username">Username</label>
    <input id="username" name="username" type="text" required autofocus>

    <label for="password">Password</label>
    <input id="password" name="password" type="password" required>

    <button type="submit">Log in</button>
  </form>

</body>
</html>
```

Read it against the checklist:

- [x] `method="POST"` — logging in changes something
- [x] `action="/login"` — the Flask route that will receive it
- [x] `name=` on both inputs — otherwise nothing is sent
- [x] `type="password"` — dots, not characters
- [x] `<label for>` matching `id` — clickable, accessible
- [x] `required` — free check, re-checked on the server anyway
- [x] `class="card"` — styling lives in the CSS, not the HTML

---

## Quick Reference

| Concept | Syntax |
|---|---|
| Form | `<form action="/url" method="POST">` |
| Text field | `<input name="key" type="text">` |
| Password field | `<input name="key" type="password">` |
| Label | `<label for="x">Text</label>` + `<input id="x">` |
| Dropdown | `<select name="k"><option value="v">Text</option></select>` |
| Multi-line | `<textarea name="k"></textarea>` |
| Submit | `<button type="submit">Go</button>` |
| Make it required | `required` |
| Read POST data (Flask) | `request.form.get("key", "")` |
| Read GET data (Flask) | `request.args.get("key", "")` |
| Allow both methods | `@app.route("/x", methods=["GET", "POST"])` |
| Link a stylesheet | `<link rel="stylesheet" href="style.css">` |
| Tag selector | `button { }` |
| Class selector | `.card { }` + `class="card"` |
| Id selector | `#login { }` + `id="login"` |
| Space inside the border | `padding` |
| Space outside the border | `margin` |
| Stack elements vertically | `display: block` |
| Make `width: 100%` sane | `box-sizing: border-box` |
| Centre the page | `max-width: 24rem; margin: 0 auto;` |

---

## Common Problems

| What you see | What's wrong | Fix |
|---|---|---|
| A field never arrives in Python | no `name=` on the input | add `name="..."` |
| `400 Bad Request` on submit | `name=` doesn't match `request.form["..."]` | make the two strings identical, or use `.get()` |
| `405 Method Not Allowed` | route doesn't allow POST | `methods=["GET", "POST"]` |
| Password appears in the address bar | the form is `GET` | change to `method="POST"` |
| Checkbox causes a `KeyError` | unticked boxes send nothing | `"key" in request.form` or `.get()` |
| Only one checkbox value arrives | `[]` returns the first match | `request.form.getlist("key")` |
| All radios can be ticked at once | they have different `name=` values | give the whole group one `name` |
| Clicking the label does nothing | `for` doesn't match `id` | make them identical |
| CSS has no effect | wrong path, or the browser cached it | check the file loads directly; hard refresh `Cmd/Ctrl + Shift + R` |
| Input overflows its container | `width: 100%` plus padding | add `box-sizing: border-box` |
| Label and input share a line | they're inline by default | `display: block` |
| Form "works" but page is blank | it submitted to a URL with no route | check `action=` matches a real route |

---

## Concepts Map — What You Already Know → Forms

| You Already Know | Form Equivalent |
|---|---|
| **Dictionaries** → `{"key": "value"}` | `request.form` — a dict built from `name=` attributes |
| **`.get()` with a default** → `d.get("k", "")` | the safe way to read an optional field |
| **`in`** → `"k" in d` | how you test whether a checkbox was ticked |
| **`input()`** → asking the user in the terminal | a form — the same question, asked in a browser |
| **`int()` on `input()`** | `int(request.form["age"])` — it's still a string |
| **`.strip()`** on user text | still needed; users type trailing spaces |
| **Validating input before using it** | exactly the same, because the browser can't be trusted |
| **Functions vs copy-paste** | an external `.css` file vs inline `style=` |
| **Separating logic from output** | HTML (*what it is*) vs CSS (*how it looks*) |

---

## Where This Goes Next

You can now describe a form and read it in Flask. The missing piece is
**remembering** what you received — right now the data vanishes the moment the
function returns.

Next: `examples/flask_login/` — the same form, wired to Python, with the users
saved to a **file** using the file I/O you already know. After that, a database.
