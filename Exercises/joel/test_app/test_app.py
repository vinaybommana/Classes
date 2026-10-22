from flask import Flask, request, jsonify
from flask import render_template


app = Flask(__name__)


@app.route("/") # default
def hello():
    return "<p>Hello world</p>"


@app.route("/multiply/<a>/<b>") # a & b are slugs
def multiply(a, b):
    mul = int(a) * int(b)
    return f"here's the product: {mul}"


@app.route("/greet")
def say_hello():
    name = request.args.get("name")
    day = request.args.get("day")

    return f"Hey {name}, it's {day}"

    # return jsonify(request.args)


@app.route("/<name>")
def greet(name):
    return f"Hello {name}"


# user registration
@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "GET":
        return render_template("registerform.html")

    if request.method == "POST":
        username = request.form.get("username", "") # dict["key"] or dict.get("key")
        password = request.form.get("password", "")

        with open("userdetails.txt", "a+") as f:
            f.write(f"{username}, {password}\n")

        return f"Hi {username}, thanks for registering"


# user login
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":

        return render_template("login.html")

    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        userdetails = {}
        with open("userdetails.txt", "r") as f:

            for line in f:
                duser, dpassword = line.split(",")
                userdetails[duser] = dpassword.strip() # string manipulation

        # print(userdetails.keys())

        if username in userdetails.keys():
            if password == userdetails[username]:
                return f"Hi {username}, you're logged in"
            else:
                # print(password, userdetails[username])
                return f"Password incorrect, please login with correct credentials"
        else:
            return "Username not present, please register"

