# Returning HTML Pages — Flask Templates

The follow-on to `examples/flask_basics/`. There we returned **strings**; here we
return proper **HTML pages** using `render_template()`.

Read `app.py` top to bottom, then open each template it mentions. Every file is
commented — the templates teach as much as the Python does.

---

## The one idea

```
app.py        →  the LOGIC    (Python works out the data)
templates/    →  the LAYOUT   (HTML decides how it looks)
static/       →  CSS, images, JS  (served unchanged)
```

`render_template("page.html", name="Joel")` opens `templates/page.html`, replaces
the blanks with the values you passed, and returns the finished HTML.

---

## Folder layout — this part is not optional

```
flask_templates/
├── app.py
├── templates/          ← Flask looks here, by this exact name
│   ├── base.html
│   ├── index.html
│   ├── hello.html
│   ├── square.html
│   ├── fruits.html
│   ├── users.html
│   ├── user.html
│   ├── user_not_found.html
│   └── convert.html
└── static/             ← and here, by this exact name
    └── style.css
```

You never configure these folders. `Flask(__name__)` tells Flask where `app.py`
lives, and it looks for `templates/` and `static/` right next to it. Name them
anything else and you get `TemplateNotFound`.

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

## Things to try

| URL | What it shows | Concept |
|---|---|---|
| http://localhost:5000/old-way | a page built as one big Python string | the problem |
| http://localhost:5000/ | the same page, done properly | `render_template()` |
| http://localhost:5000/hello/Joel | Hello, Joel! | passing one variable |
| http://localhost:5000/square/7 | 7 squared is 49 | passing several |
| http://localhost:5000/fruits | a table of 4 fruits | `{% for %}` loop |
| http://localhost:5000/users | a list with links | looping a dict |
| http://localhost:5000/users/1 | Alice, active, admin | `{% if %}` |
| http://localhost:5000/users/3 | Charlie, deactivated | the `else` branch |
| http://localhost:5000/users/99 | a styled 404 page | template **+ status code** |
| http://localhost:5000/convert | a working form | GET vs POST |
| http://localhost:5000/static/style.css | the raw CSS | static files |

Compare `/old-way` with `/` first. Same output, completely different code.

---

## The two kinds of brackets

This is the one piece of new syntax, and it is the thing students mix up.

| Syntax | Means | Example |
|---|---|---|
| `{{ ... }}` | **print** this value into the page | `{{ user.name }}` |
| `{% ... %}` | **do** this — for, if, extends, block | `{% for f in fruits %}` |
| `{# ... #}` | a comment the browser never sees | `{# TODO #}` |

Curly-curly puts something on the screen. Curly-percent controls what happens.

```html
{% if user.active %}              <!-- do: a decision -->
  <p>{{ user.name }} is active</p>  <!-- print: a value -->
{% endif %}                       <!-- do: end the decision -->
```

Two differences from Python worth saying out loud:

1. **Indentation means nothing.** That's why every `{% for %}` needs an
   `{% endfor %}` and every `{% if %}` needs an `{% endif %}`.
2. **`{{ }}` only prints.** You can't assign or define functions in it.

The template language is called **Jinja2**. It ships with Flask — nothing extra
to install.

---

## Python → Jinja, side by side

```python
# Python                           # Template
f"Hello, {name}!"                  Hello, {{ name }}!

for fruit in fruits:               {% for fruit in fruits %}
    print(fruit["name"])             {{ fruit.name }}
                                   {% endfor %}

if user.active:                    {% if user.active %}
    print("Active")                  <p>Active</p>
else:                              {% else %}
    print("Inactive")                <p>Inactive</p>
                                   {% endif %}

len(fruits)                        {{ fruits|length }}
name.upper()                       {{ name|upper }}
round(x, 1)                        {{ x|round(1) }}
```

In a template, `fruit.name` and `fruit["name"]` both work on a dictionary. Use
the dot form — it reads better.

---

## Two things worth pointing out in class

### `url_for()` — never type a URL by hand

```html
<a href="/users/1">Alice</a>                               <!-- fragile -->
<a href="{{ url_for('user_profile', user_id=1) }}">Alice</a>  <!-- good -->
```

`url_for` takes the **function name**, not the path. Rename the route from
`/users/<id>` to `/people/<id>` and every link fixes itself.

### `{% extends %}` — write the skeleton once

`base.html` holds the `<head>`, the nav bar and the footer. Every other page
starts with `{% extends "base.html" %}` and fills in the holes:

```html
{% extends "base.html" %}
{% block title %}Fruits{% endblock %}
{% block content %}
  <h1>Fruits</h1>
{% endblock %}
```

Add a link to the nav in `base.html` and it appears on all nine pages. Same
reasoning as writing a function instead of copy-pasting the body.

---

## Experiments

`debug=True` reloads on save — just refresh the browser.

1. Add a fifth fruit to `fruit_list` in `app.py`. Don't touch the HTML. Refresh.
2. Add a `"stock"` key to each fruit and a `Stock` column to the table.
3. In `fruits.html`, colour expensive rows: wrap the price in
   `{% if fruit.price > 200 %}<strong>...</strong>{% endif %}`.
4. Delete every fruit from the list. The `{% else %}` on the for-loop fires.
5. Add a `/goodbye/<name>` route and a `goodbye.html` that extends `base.html`.
6. Add a "Fahrenheit to Celsius" box to `convert.html` as a second form.
7. Change the nav background in `style.css`. One file, every page.
8. **Break it:** rename `templates/` to `html/` and refresh. Read the
   `TemplateNotFound` error, then rename it back.
9. **Break it:** remove an `{% endfor %}`. Read that error too — Jinja errors
   name the template and the line.

---

## Common problems

| What you see | What's wrong | Fix |
|---|---|---|
| `jinja2.exceptions.TemplateNotFound: index.html` | the file isn't in `templates/`, or the folder is misnamed/misplaced | it must be `templates/`, next to `app.py` |
| The page shows `{{ name }}` literally | you opened the `.html` file directly instead of visiting the URL | go through `http://localhost:5000/` — the server has to render it |
| A variable renders as empty | you forgot to pass it to `render_template` | undefined names render as nothing, silently — check the call |
| `Encountered unknown tag 'endfor'` | an `{% endfor %}`/`{% endif %}` is missing or out of order | count your open/close tags |
| CSS has no effect | wrong path, or the file isn't in `static/` | use `url_for('static', filename='style.css')`; check <http://localhost:5000/static/style.css> loads |
| CSS change doesn't show | the browser cached it | hard refresh: `Cmd/Ctrl + Shift + R` |
| `400 Bad Request` on form submit | the `name=` attribute doesn't match `request.form["..."]` | make the two strings identical |
| Form submits but nothing happens | `methods=["GET", "POST"]` missing from the route | add it |

---

## Where this goes next

Templates render data. The remaining piece is where the data comes from — right
now `users` and `fruit_list` are hard-coded in `app.py` and vanish when the
server restarts. The next step is persisting them: a file (you already know
file I/O) or a database.
