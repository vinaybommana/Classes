# ============================================================
# Returning HTML Pages — Templates
# ============================================================
#
# In flask_basics we returned STRINGS. A string with a couple of <h1> tags in
# it is fine for a demo, but a real page is 50+ lines of HTML, and you do NOT
# want 50 lines of HTML jammed inside a Python function.
#
# So we separate them:
#
#     app.py        -> the LOGIC    (Python: work out the data)
#     templates/    -> the LAYOUT   (HTML: decide how it looks)
#
# render_template() is the bridge. It:
#   1. finds the .html file inside the `templates/` folder
#   2. fills in the blanks with the values you pass it
#   3. returns the finished HTML as a string, which Flask sends to the browser
#
# IMPORTANT: the folder MUST be called `templates` and MUST sit next to app.py.
# Flask looks there automatically — that's what Flask(__name__) was for.
#
#     flask_templates/
#     ├── app.py
#     ├── templates/        <- HTML goes here
#     │   ├── base.html
#     │   ├── index.html
#     │   └── ...
#     └── static/           <- CSS, images, JS go here
#         └── style.css
#
# To run this file:
#     pip install flask
#     python app.py
# Then open http://localhost:5000/ in your browser.
#

from flask import Flask, render_template, request

app = Flask(__name__)


# --------------------------------------------------
# Example 0: The problem we are solving
# --------------------------------------------------
# This is how we did it before. It WORKS — but look at it. The HTML is trapped
# inside the Python. You can't get syntax highlighting, you can't hand it to a
# designer, and it gets unreadable fast.
#
# Keep this route around so you can compare it with /  below.

@app.route("/old-way")
def old_way():
    return """
        <!DOCTYPE html>
        <html>
        <head><title>The Old Way</title></head>
        <body>
            <h1>Hello, World!</h1>
            <p>This whole page is one big Python string. Imagine 200 lines.</p>
        </body>
        </html>
    """


# Try: http://localhost:5000/old-way


# --------------------------------------------------
# Example 1: render_template — your first real page
# --------------------------------------------------
# Same output, but the HTML now lives in templates/index.html where it belongs.
#
# render_template("index.html") means:
#   "open templates/index.html, process it, and give me back the finished HTML"
#
# Note we pass just the FILENAME, not the path. Flask already knows the folder.

@app.route("/")
def home():
    return render_template("index.html")


# Try: http://localhost:5000/


# --------------------------------------------------
# Example 2: Passing a variable into the page
# --------------------------------------------------
# Any extra keyword argument you give render_template becomes a variable that
# the template can use.
#
#   render_template("hello.html", name="Joel")
#                                 ^^^^^^^^^^^
#                                 inside the HTML this is written as {{ name }}
#
# This is the same idea as an f-string, just living in the HTML file:
#
#     Python:    f"Hello, {name}!"
#     Template:  Hello, {{ name }}!

@app.route("/hello/<name>")
def hello(name):
    return render_template("hello.html", name=name)


# You can pass as many as you like, and they can be any Python type —
# strings, numbers, lists, dictionaries.

@app.route("/square/<int:number>")
def square(number):
    return render_template(
        "square.html",
        number=number,
        answer=number ** 2,
    )


# Try: http://localhost:5000/hello/Joel
#      http://localhost:5000/square/7


# --------------------------------------------------
# Example 3: Loops in a template — showing a list
# --------------------------------------------------
# Here is the real payoff. We have a list of dictionaries (something you have
# written a hundred times) and we want a row in a table for each one.
#
# We do NOT build the HTML in Python. We hand the LIST to the template and let
# the template loop over it with:
#
#     {% for fruit in fruits %}
#         ... repeated HTML ...
#     {% endfor %}
#
# Two kinds of brackets, and the difference matters:
#
#     {{ ... }}   PRINT this value into the page      (an expression)
#     {% ... %}   DO this                             (a statement: for, if)
#
# Rule of thumb: curly-curly puts something on the screen, curly-percent
# controls what happens. And unlike Python, indentation means nothing here —
# that's why every {% for %} needs an explicit {% endfor %}.

@app.route("/fruits")
def fruits():
    fruit_list = [
        {"name": "Apple", "color": "Red", "price": 120},
        {"name": "Banana", "color": "Yellow", "price": 60},
        {"name": "Grape", "color": "Purple", "price": 250},
        {"name": "Mango", "color": "Orange", "price": 300},
    ]
    return render_template("fruits.html", fruits=fruit_list)


# Try: http://localhost:5000/fruits


# --------------------------------------------------
# Example 4: if/else in a template
# --------------------------------------------------
# Same if/else you already know, in {% %} brackets. Use it to show a different
# page depending on the data — here, a "not found" message instead of a profile.
#
# Notice the 404: `return render_template(...), 404` — an HTML page and a status
# code together. Templates and status codes are independent; you can mix them.

users = {
    1: {"name": "Alice", "role": "admin", "active": True},
    2: {"name": "Bob", "role": "student", "active": True},
    3: {"name": "Charlie", "role": "student", "active": False},
}


@app.route("/users")
def user_list():
    return render_template("users.html", users=users)


@app.route("/users/<int:user_id>")
def user_profile(user_id):
    # Do the LOGIC in Python...
    user = users.get(user_id)

    # ...and let the template worry about how to display it.
    if user is None:
        return render_template("user_not_found.html", user_id=user_id), 404

    return render_template("user.html", user=user, user_id=user_id)


# Try: http://localhost:5000/users
#      http://localhost:5000/users/1
#      http://localhost:5000/users/3       <- inactive, renders differently
#      http://localhost:5000/users/99      <- 404 page


# --------------------------------------------------
# Example 5: A form that posts back to a page
# --------------------------------------------------
# A plain HTML page is one-way: server -> browser. A FORM makes it two-way.
#
# The template contains:
#     <form method="POST">
#       <input name="celsius">
#     </form>
#
# When the user hits submit, the browser sends a POST to the same URL, with the
# input values in `request.form`. So one route handles both:
#
#     GET  -> show the empty form
#     POST -> read the data, calculate, show the form again WITH the answer
#
# Same `methods=["GET", "POST"]` idea as before — the only new part is that the
# answer goes back through the template.

@app.route("/convert", methods=["GET", "POST"])
def convert():
    result = None

    if request.method == "POST":
        celsius = float(request.form["celsius"])
        result = celsius * 9 / 5 + 32

    # On a GET, result is None and the template hides the answer box.
    return render_template("convert.html", result=result)


# Try: http://localhost:5000/convert


# ============================================================
# Starting the server
# ============================================================
# On a Mac, if every page is "403 Forbidden", AirPlay Receiver owns port 5000.
# Use app.run(debug=True, port=5001) instead.

if __name__ == "__main__":
    app.run(debug=True)
