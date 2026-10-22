# ============================================================
# A Login System — Forms In, Data Saved to a File
# ============================================================
#
# In flask_templates we rendered pages and read one form. Here we build the
# thing every website has: register, log in, stay logged in, log out.
#
# Three new ideas, and nothing else:
#
#   1. READING A FORM      request.form, and checking it properly
#   2. REMEMBERING DATA    writing users to a file, reading them back
#   3. REMEMBERING THE USER  session — so page 2 knows who logged in on page 1
#
# Everything else you already know: routes, render_template, if/else, and the
# file I/O from Exercises/fileoperations.py.
#
#     flask_login/
#     ├── app.py
#     ├── users.txt            <- created automatically on first signup
#     ├── templates/
#     │   ├── base.html
#     │   ├── register.html
#     │   ├── login.html
#     │   └── dashboard.html
#     └── static/
#         └── style.css
#
# To run this file:
#     pip install flask
#     python app.py
# Then open http://localhost:5000/ in your browser.
#

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)


# --------------------------------------------------
# The secret key
# --------------------------------------------------
# session (further down) needs this. Flask stores the session in a cookie in
# the user's browser, and signs that cookie with this key so nobody can edit
# it and claim to be somebody else.
#
# Hard-coding it is fine for a classroom demo. In a real app it comes from an
# environment variable and is never committed to git:
#
#     import os
#     app.secret_key = os.environ["SECRET_KEY"]
#
# If you forget this line entirely, the first session write crashes with
# "The session is unavailable because no secret key was set."

app.secret_key = "dev-only-change-me"


# --------------------------------------------------
# Where the data lives
# --------------------------------------------------
# One line per user, username and password separated by a comma:
#
#     joel,secret123
#     alice,hunter2
#
# This is a CSV file, written by hand. We are using it because you already
# know open(), read, write and split — no new Python at all.
#
# Note it sits NEXT TO app.py, not inside templates/ or static/.
# Anything inside static/ is downloadable by the whole internet, which would
# mean publishing your password file. Keep data out of static/.

USERS_FILE = "users.txt"


# ============================================================
# PART 1 — The storage layer (plain Python, no Flask)
# ============================================================
# Notice these two functions have NO @app.route and import nothing from Flask.
# They are ordinary functions you could test from the terminal.
#
# That separation is deliberate and it is the habit worth stealing from this
# file: the routes handle the WEB, these functions handle the DATA. Tomorrow
# we swap the file for a database — and ONLY these two functions change.


def load_users():
    """Read the whole file and return {username: password}."""

    users = {}

    # The file won't exist until the first person registers, and open() in
    # read mode would raise FileNotFoundError. Handle it rather than crash.
    try:
        with open(USERS_FILE, "r") as f:
            for line in f:

                # Trailing newline on every line, plus possible blank lines at
                # the end of the file. Clean first, skip empties.
                line = line.strip()
                if not line:
                    continue

                # "joel,secret123"  ->  ["joel", "secret123"]
                #
                # split(",", 1) splits on the FIRST comma only. Not important
                # here because we ban commas on the way in, but it is the
                # right habit: it stops one stray comma shifting every column.
                username, password = line.split(",", 1)
                users[username] = password

    except FileNotFoundError:
        # No file yet simply means no users yet. An empty dict is correct.
        pass

    return users


def save_user(username, password):
    """Append one new user to the end of the file."""

    # "a" = APPEND. This matters enormously.
    #
    #     "w"  wipes the file and starts over   <- would delete every user
    #     "a"  adds to the end                  <- what we want
    #
    # Open in "w" by mistake and your second signup erases your first. It is
    # a one-character bug that deletes all your data.
    with open(USERS_FILE, "a") as f:
        f.write(f"{username},{password}\n")

    # The \n matters too. Without it, every user ends up on one giant line
    # and load_users() reads them all as a single broken record.


# ============================================================
# PART 2 — Register: receiving a form and validating it
# ============================================================
# One route, two jobs — the pattern from the forms cheatsheet:
#
#     GET  /register   -> show the empty form
#     POST /register   -> read what was typed, check it, save it
#
# The route MUST list both methods, or submitting gives 405 Method Not Allowed.

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        # ---- Read the form -----------------------------------------
        # request.form is a dictionary. The keys are the name= attributes
        # from register.html:
        #
        #     <input name="username">   ->   request.form["username"]
        #
        # Use .get() rather than [] so a missing field gives "" instead of a
        # 400 Bad Request. Our own form always sends both, but a browser is
        # not the only thing that can POST here.
        #
        # .strip() because users type trailing spaces constantly, and
        # "joel " and "joel" would otherwise be two different accounts.

        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        # Note: we strip the username but NOT the password. A space is a
        # perfectly legal password character and silently deleting it would
        # lock the user out of their own account.

        # ---- Check it ----------------------------------------------
        # register.html already has `required` and `minlength="4"` on these
        # fields, so why check again?
        #
        # Because `required` is a browser convenience, not a defence. Anyone
        # can delete it in developer tools, or skip the browser entirely:
        #
        #     curl -X POST -d "username=&password=" localhost:5000/register
        #
        # The server is the only place a rule is actually enforced. Treat
        # everything arriving in request.form as untrusted. Always.
        #
        # The pattern below is just a chain of if/return. The first failing
        # check renders the form again WITH an error message and the username
        # still filled in — never make someone retype a correct field.

        users = load_users()

        if not username or not password:
            return render_template(
                "register.html",
                error="Please fill in both fields.",
            )

        if len(password) < 4:
            return render_template(
                "register.html",
                error="Password must be at least 4 characters.",
                username=username,
            )

        # Our storage format is "username,password" — one comma per line. A
        # comma inside a username would add a second one and corrupt the row.
        #
        # This check is a bit silly, and that is the point: it exists only
        # because of how we chose to store the data. A database would have no
        # such rule. Keep it in mind for tomorrow.
        if "," in username or "," in password:
            return render_template(
                "register.html",
                error="Sorry, no commas allowed (our file format uses them).",
            )

        if username in users:
            return render_template(
                "register.html",
                error=f"The username '{username}' is already taken.",
                username=username,
            )

        # ---- Save it -----------------------------------------------
        save_user(username, password)

        # Send them to the login page with a success message.
        #
        # Why redirect instead of just rendering a page here? Because after a
        # POST, the URL in the address bar is still /register. Hitting refresh
        # would re-submit the form and try to register them twice.
        #
        # A redirect tells the browser "go and GET this other URL instead", so
        # the address bar ends up on a plain GET page that is safe to refresh.
        # This is called Post/Redirect/Get and it is the standard fix.
        #
        # url_for("login") builds the URL from the FUNCTION name, same as in
        # the templates. The ?registered=1 on the end is a query parameter,
        # which login() reads back out of request.args.
        return redirect(url_for("login", registered=1))

    # ---- GET: just show the empty form ------------------------------
    return render_template("register.html")


# ============================================================
# PART 3 — Login: checking the form against the file
# ============================================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        users = load_users()

        # The entire check is one dictionary lookup and one comparison.
        #
        #     users.get(username)   -> the stored password, or None if no
        #                              such user
        #
        # Using .get() rather than users[username] means an unknown username
        # gives None instead of a KeyError, so both failure cases fall into
        # the same branch below.
        stored_password = users.get(username)

        if stored_password is None or stored_password != password:

            # Deliberately vague: "username or password is incorrect".
            #
            # If we said "no such user" for one and "wrong password" for the
            # other, anyone could type usernames at this form until one came
            # back "wrong password" and learn who has an account here. Tell
            # the attacker nothing; the honest user knows which one they got
            # wrong anyway.
            return render_template(
                "login.html",
                error="Username or password is incorrect.",
                username=username,
            )

        # ---- They are who they say they are -------------------------
        # Now the actual "login" bit, which is one line:
        session["username"] = username

        # WHAT JUST HAPPENED
        # ------------------
        # HTTP has no memory. Every request is a stranger knocking at the
        # door — the next page load knows nothing about this one. So how does
        # a site keep you logged in?
        #
        # Flask writes {"username": "joel"} into a cookie, signs it with
        # app.secret_key, and the browser sends that cookie back with EVERY
        # subsequent request automatically. Any route can then read it:
        #
        #     session["username"]     ->  "joel"
        #
        # So `session` behaves like a dictionary that survives between
        # requests, and is private to this one browser. That is all a login
        # is: a note saying who you are, carried along with each request.
        #
        # Signed means tamper-proof, NOT hidden. The user can decode and read
        # their own cookie. Never put anything secret in the session.

        return redirect(url_for("dashboard"))

    # ---- GET: show the form -----------------------------------------
    # request.args is request.form's twin: .form holds POST body data,
    # .args holds the ?key=value bits of the URL. register() redirected here
    # with ?registered=1, so this is how we show the success message.
    just_registered = request.args.get("registered") == "1"

    return render_template("login.html", registered=just_registered)


# ============================================================
# PART 4 — A page only logged-in users can see
# ============================================================

@app.route("/dashboard")
def dashboard():

    # The guard. Three lines, and it goes at the top of every private route.
    #
    # Without it, anyone could type /dashboard in the address bar and walk
    # straight in — the login page is not a door, it is just a page. The
    # ONLY thing keeping people out is this check.
    username = session.get("username")

    if username is None:
        return redirect(url_for("login"))

    # Again .get(), not session["username"], because a logged-out visitor has
    # no such key and [] would raise a KeyError (a 500 error page) instead of
    # politely redirecting.

    return render_template("dashboard.html", username=username)


@app.route("/logout")
def logout():

    # Logging out is just forgetting. pop() with a default of None means this
    # doesn't crash if they were never logged in to begin with.
    session.pop("username", None)

    # session.clear() would empty the whole session instead — use that when
    # you're storing several things and want all of them gone.

    return redirect(url_for("login"))


# ============================================================
# PART 5 — Home
# ============================================================

@app.route("/")
def home():
    # Logged in? Go to the dashboard. Otherwise, go and log in.
    if "username" in session:
        return redirect(url_for("dashboard"))

    return redirect(url_for("login"))


# ============================================================
# PART 6 — A teaching route: look at the raw file
# ============================================================
# Not something you would ever ship. It exists so you can see, in the browser,
# that your data really is sitting in a plain text file on disk — and see the
# problem with that.
#
# Register two users, then open /debug/users-file. Then stop the server with
# Ctrl+C, start it again, and log in. The users are still there. THAT is
# persistence, and it is the whole reason we touched a file at all.

@app.route("/debug/users-file")
def debug_users_file():
    try:
        with open(USERS_FILE, "r") as f:
            contents = f.read()
    except FileNotFoundError:
        contents = "(no file yet — register someone first)"

    return render_template("debug_file.html", contents=contents, path=USERS_FILE)


# ============================================================
# Starting the server
# ============================================================
# On a Mac, if every page is "403 Forbidden", AirPlay Receiver owns port 5000.
# Use app.run(debug=True, port=5001) instead.

if __name__ == "__main__":
    app.run(debug=True)
