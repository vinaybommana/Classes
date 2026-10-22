# ============================================================
# Your First Flask Web Application
# ============================================================
#
# So far, every program we wrote ran once, printed to the terminal, and exited.
# A WEB SERVER is different: it starts up and then WAITS, forever, for someone
# to ask it for something. When a request arrives, it runs a function and sends
# the return value back.
#
# That's the whole idea:
#
#     Browser asks for a URL  ->  Flask finds the matching function
#                             ->  Flask runs it
#                             ->  whatever you RETURN goes back to the browser
#
# A "route" is just the glue between a URL and a function.
#
# To run this file:
#     pip install flask
#     python app.py
# Then open http://localhost:5000/ in your browser.
#

from flask import Flask, request, jsonify

# Create the application object.
# `__name__` is the special variable holding this module's name - Flask uses it
# to figure out where this file lives (same `__name__` from modularisation).
app = Flask(__name__)


# --------------------------------------------------
# Example 1: The simplest possible route
# --------------------------------------------------
# @app.route("/") is a DECORATOR. Read it as:
#   "Flask, when somebody visits the path '/', call the function below."
#
# The function itself is an ordinary Python function. Nothing magic.
# Whatever it RETURNS becomes the response body.

@app.route("/")
def home():
    return "Hello, World!"


# Try: http://localhost:5000/


# --------------------------------------------------
# Example 2: More routes = more pages
# --------------------------------------------------
# Each route needs its own URL path AND its own function name.
# Returning a string containing HTML tags works too - the browser renders it.

@app.route("/about")
def about():
    return "This is the about page."


@app.route("/contact")
def contact():
    return """
        <h1>Contact Us</h1>
        <p>Email: hello@example.com</p>
    """


# Try: http://localhost:5000/about
#      http://localhost:5000/contact


# --------------------------------------------------
# Example 3: Dynamic routes - URLs with variables
# --------------------------------------------------
# <name> in the URL means "capture whatever is here and pass it to the
# function as a parameter". This is exactly like a function parameter -
# the URL supplies the argument instead of your code.

@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}!"


# By default captured values are STRINGS. Use <int:...> to get a real int,
# so you can do maths with it without calling int() yourself.

@app.route("/square/<int:number>")
def square(number):
    return f"{number} squared is {number ** 2}"


# You can capture more than one value.

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return f"{a} + {b} = {a + b}"


# Try: http://localhost:5000/hello/Joel
#      http://localhost:5000/square/7
#      http://localhost:5000/add/3/5


# --------------------------------------------------
# Example 4: Query parameters - the ?key=value part
# --------------------------------------------------
# Anything after the `?` in a URL is a query parameter. Flask collects them
# all in `request.args`, which behaves like a dictionary.
#
# Use .get("key", default) rather than ["key"] - just like with dictionaries,
# .get() returns the default instead of crashing when the key is missing.

@app.route("/greet")
def greet():
    name = request.args.get("name", "stranger")
    times = request.args.get("times", 1, type=int)

    return f"Hello, {name}! " * times


# Try: http://localhost:5000/greet
#      http://localhost:5000/greet?name=Joel
#      http://localhost:5000/greet?name=Joel&times=3


# --------------------------------------------------
# Example 5: Returning JSON instead of HTML
# --------------------------------------------------
# HTML is for humans looking at a browser.
# JSON is for other PROGRAMS - mobile apps, scripts, other servers.
#
# jsonify() takes a Python dict or list and turns it into a JSON response.
# Notice we are just returning the data structures we already know.

@app.route("/api/fruits")
def get_fruits():
    fruits = [
        {"name": "Apple", "color": "Red"},
        {"name": "Banana", "color": "Yellow"},
        {"name": "Grape", "color": "Purple"},
    ]
    return jsonify(fruits)


# --------------------------------------------------
# Example 6: Status codes - saying what happened
# --------------------------------------------------
# Return a TUPLE of (response, status_code) to control the status code.
# If you don't, Flask sends 200 OK.
#
#   200 OK          - it worked
#   404 Not Found   - you asked for something that doesn't exist
#
# This is also our first bit of real "logic in a route": a dictionary lookup
# plus an if/else, exactly like you'd write anywhere else.

users = {
    1: "Alice",
    2: "Bob",
    3: "Charlie",
}


@app.route("/api/users/<int:user_id>")
def get_user(user_id):
    if user_id in users:
        return jsonify({"id": user_id, "name": users[user_id]}), 200
    else:
        return jsonify({"error": "User not found"}), 404


# Try: http://localhost:5000/api/fruits
#      http://localhost:5000/api/users/1
#      http://localhost:5000/api/users/99      <- 404


# ============================================================
# Starting the server
# ============================================================
# This is the same `if __name__ == "__main__"` guard from modularisation:
# only start the server when this file is RUN directly, not when imported.
#
# debug=True gives you two things while developing:
#   1. the server restarts automatically every time you save this file
#   2. errors show a detailed page in the browser instead of a blank 500
# Never use debug=True on a real public server.
#
# ON A MAC: if every page gives you "403 Forbidden", port 5000 is being used
# by Apple's AirPlay Receiver, not by us. Either turn AirPlay Receiver off in
# System Settings > General > AirDrop & Handoff, or just use another port:
#
#     app.run(debug=True, port=5001)
#
# ...and then visit http://localhost:5001/ instead.

if __name__ == "__main__":
    app.run(debug=True)
