# Virtual Environments in Python (`venv`)

---

## 1. The Problem

Until now, every program we wrote used only the **standard library** — the tools
that ship with Python itself (`input`, `open`, `math`, `random`). Nothing to install.

The moment you write `pip install flask`, that changes. You now depend on code
that *isn't* part of Python, and that code gets installed **somewhere**. Where?

By default, into your **system Python** — one shared pile of packages used by every
Python project on your computer.

That works fine until it doesn't:

```
                    ONE SHARED PILE OF PACKAGES
                  ┌──────────────────────────────┐
                  │   Flask 3.1                  │
   Project A ────►│   requests 2.31              │◄──── Project B
   (needs         │   pandas 2.0                 │      (needs
    Flask 3.1)    │   ...                        │       Flask 1.0)
                  └──────────────────────────────┘
                              ▲
                              │
                         Project C
                   (needs pandas 1.5, not 2.0)

   Only ONE version of each package can be installed at a time.
   Projects A, B and C cannot all be happy.
```

### The three things that go wrong

| Problem | What it looks like |
|---|---|
| **Version conflicts** | Project A needs Flask 3, Project B needs Flask 1. Installing one breaks the other. |
| **No record of what you need** | Six months later: "which packages did this project actually need?" No way to tell — your system has 80 installed. |
| **Can't share your project** | You send your code to a classmate. It crashes: `ModuleNotFoundError`. They don't know what to install. |

---

## 2. What a Virtual Environment Is

A **virtual environment** is a private folder containing its own copy of Python
and its own package folder. Each project gets one.

```
             SEPARATE, ISOLATED ENVIRONMENTS
   ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
   │   Project A     │  │   Project B     │  │   Project C     │
   │   .venv/        │  │   .venv/        │  │   .venv/        │
   │                 │  │                 │  │                 │
   │   Flask 3.1     │  │   Flask 1.0     │  │   pandas 1.5    │
   │   requests 2.31 │  │                 │  │                 │
   └─────────────────┘  └─────────────────┘  └─────────────────┘

   Nobody interferes with anybody. Each project gets exactly what it needs.
```

Think of it as a **separate toolbox per project** instead of throwing every tool
you own into one drawer.

`venv` is the tool that creates these. It is **built into Python** — nothing to install.

### Key Points

- A virtual environment is just a **folder**. Nothing magic, nothing registered
  system-wide, nothing hidden.
- One virtual environment **per project**.
- Deleting the folder deletes the environment completely. That's the whole uninstall.

---

## 3. Creating One

From inside your project folder:

```bash
python3 -m venv .venv
```

Breaking that down:

| Part | What it means |
|---|---|
| `python3` | run Python |
| `-m venv` | run the built-in module named `venv` |
| `.venv` | the folder to create (this is the name, and it's your choice) |

> **Why `.venv`?** The leading dot hides it from normal `ls` listings, and it's
> the name editors like VS Code look for automatically. You'll also see `venv`
> or `env` — all fine, but be consistent.

This takes a few seconds and creates a `.venv/` folder. **You only do this once
per project.**

---

## 4. What's Inside

Worth looking at once, so it stops feeling mysterious:

```
.venv/
├── bin/                    (Windows: Scripts/)
│   ├── activate            ← the script that switches you in
│   ├── python              ← this environment's own Python
│   ├── python3
│   └── pip                 ← this environment's own pip
├── include/
├── lib/
│   └── python3.12/
│       └── site-packages/  ← WHERE INSTALLED PACKAGES GO
│           └── pip/
└── pyvenv.cfg              ← a small text file of settings
```

The two parts that matter:

| Path | What it holds |
|---|---|
| `.venv/bin/` | This environment's own `python` and `pip` commands |
| `.venv/lib/python3.12/site-packages/` | Every package you `pip install` |

A brand-new environment contains **only `pip`** — it starts empty on purpose.

### Key Points

- The whole point is that `.venv/bin/python` and `.venv/bin/pip` are *different
  programs* from the system `python3` and `pip3`.
- `site-packages/` is the pile of packages — but now it's a pile that belongs to
  this project alone.

---

## 5. Activating and Deactivating

Creating the environment doesn't switch you into it. **Activating** does.

### Activate

```bash
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows
```

Your prompt changes to show which environment you're in:

```
vbommana@mac Classes %                      ← before
(.venv) vbommana@mac Classes %              ← after
```

### What activation actually does

It is much simpler than it looks. Activation puts `.venv/bin/` at the **front of
your PATH** — the list of folders your shell searches when you type a command.
So `python` now finds `.venv/bin/python` first.

You can see it happen:

```bash
# before activating
$ which python3
/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

# after activating
$ which python
/Users/you/Classes/.venv/bin/python        ← the project's own Python

$ which pip
/Users/you/Classes/.venv/bin/pip           ← the project's own pip
```

That's the whole trick. `pip install` now installs into *this* environment,
because it's a different `pip`.

### Deactivate

```bash
deactivate
```

The `(.venv)` disappears and `python3` points back at your system Python.

### Key Points

- **Activation lasts for one terminal window.** Open a new tab, or close and
  reopen the terminal, and you must activate again. This is normal, not a bug.
- Forgetting to activate is the single most common mistake. Check your prompt
  for `(.venv)`.
- You only `deactivate` to leave early — closing the terminal does it for you.

### You can skip activation entirely

Activation is a convenience. You can always call the environment's Python directly:

```bash
.venv/bin/python app.py
.venv/bin/pip install flask
```

Exactly equivalent. Useful when a script needs to run without a human to activate first.

---

## 6. Installing Packages

With the environment active, `pip install` behaves exactly as you'd expect —
but everything lands inside `.venv/`.

```bash
pip install flask
```

### Seeing what's installed

```bash
pip list
```

A fresh environment:

```
Package Version
------- -------
pip     24.3.1
```

After `pip install flask`:

```
Package      Version
------------ -------
blinker      1.9.0
click        8.5.0
Flask        3.1.3
itsdangerous 2.2.0
Jinja2       3.1.6
MarkupSafe   3.0.4
pip          24.3.1
Werkzeug     3.1.9
```

You asked for one package and got eight. The other seven are **dependencies** —
packages Flask itself needs. `pip` works out the whole tree and installs it for you.

### Useful pip commands

| Command | What it does |
|---|---|
| `pip install flask` | Install the latest version |
| `pip install flask==3.1.3` | Install one exact version |
| `pip install -r requirements.txt` | Install everything listed in a file |
| `pip list` | Show installed packages (human-readable) |
| `pip show flask` | Details about one package — version, location, dependencies |
| `pip uninstall flask` | Remove a package |

### Proof that the isolation is real

```bash
(.venv) $ python -c "import flask"        # works

(.venv) $ deactivate
$ python3 -c "import flask"
ModuleNotFoundError: No module named 'flask'
```

Flask exists inside the environment and nowhere else. Your system Python is untouched.

---

## 7. `requirements.txt` — Recording What You Need

This is how you answer "what does this project need?" — for your classmate,
for a server, and for yourself in six months.

### Save the list

```bash
pip freeze > requirements.txt
```

`pip freeze` prints every installed package with its **exact** version; `>` writes
that into a file (the same output redirection you've seen in the terminal).

The file is plain text:

```
blinker==1.9.0
click==8.5.0
Flask==3.1.3
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.4
Werkzeug==3.1.9
```

### Rebuild from the list

Anyone who has your code and this file can recreate your exact setup:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

```
   Your machine                           Their machine
   ┌──────────────┐                       ┌──────────────┐
   │ .venv/       │   pip freeze >        │              │
   │  Flask 3.1.3 │ ──────────────────►   │ requirements │
   │  click 8.5.0 │   requirements.txt    │    .txt      │
   │  ...         │                       │      │       │
   └──────────────┘                       │      ▼       │
                                          │ pip install  │
   ( .venv is NOT shared —                │  -r ...      │
     the recipe is )                      │      │       │
                                          │      ▼       │
                                          │ .venv/       │
                                          │  Flask 3.1.3 │
                                          │  click 8.5.0 │
                                          └──────────────┘
```

### Key Points

- You share the **recipe** (`requirements.txt`), never the **environment** (`.venv/`).
- Re-run `pip freeze > requirements.txt` whenever you install something new —
  it overwrites the file with the current state.
- `==` pins an exact version, so everyone gets identical packages.

---

## 8. Virtual Environments and Git

**Never commit `.venv/` to git.** For a single Flask install it is already
**18 MB across 1,177 files** — none of which is your work, all of which is
rebuildable from one small text file.

It's also not portable: the environment contains absolute paths to *your* machine,
so it wouldn't work on someone else's computer anyway.

Create a `.gitignore` file in your project root containing:

```
.venv/
__pycache__/
*.pyc
```

| File | Commit it? | Why |
|---|---|---|
| `app.py` and your other code | **Yes** | It's your work |
| `requirements.txt` | **Yes** | Tiny, and it's the recipe |
| `.gitignore` | **Yes** | So the rule travels with the project |
| `.venv/` | **No** | Huge, rebuildable, machine-specific |
| `__pycache__/` | **No** | Auto-generated by Python |

---

## 9. Using a Virtual Environment in VS Code

Your editor needs to be told which Python to use, otherwise it will underline
`import flask` in red even though the code runs fine.

1. `Cmd+Shift+P` (macOS) or `Ctrl+Shift+P` (Windows) to open the command palette
2. Type **Python: Select Interpreter**
3. Choose the one with `.venv` in the path — usually marked *Recommended*

Once selected, VS Code uses that environment for autocomplete, error checking,
and the Run button, and it auto-activates in new integrated terminals.

> A red squiggle under `import flask` while `python app.py` works perfectly means
> the **editor** is looking at the wrong Python. The code is fine — fix the interpreter.

---

## 10. Common Problems

| What you see | What's wrong | Fix |
|---|---|---|
| `ModuleNotFoundError: No module named 'flask'` | Environment not activated, or installed into the wrong one | Check for `(.venv)` in your prompt; activate; `pip install flask` |
| `(.venv)` vanished from the prompt | New terminal tab/window — activation is per-terminal | `source .venv/bin/activate` again |
| `pip: command not found` | No environment active and no system pip | Use `python3 -m pip` instead of `pip` |
| Installed a package but Python can't find it | Installed with system `pip3` while the venv was active (or vice versa) | `which pip` — confirm it points inside `.venv` |
| VS Code underlines a working import | Editor pointed at the wrong interpreter | **Python: Select Interpreter** → pick `.venv` |
| `source: no such file or directory` | Wrong path, or the venv was never created | `ls .venv/bin/activate` to check it exists |
| Environment feels broken | Something's genuinely tangled | Delete and rebuild: `rm -rf .venv`, then recreate. You lose nothing. |

### The debugging habit

When anything package-related misbehaves, ask **"which Python am I actually running?"**

```bash
which python        # which Python will run
which pip           # which pip will install
pip list            # what's installed in it
```

Nearly every virtual environment problem is one of those three not being what
you assumed.

---

## Quick Reference

| Task | Command |
|---|---|
| Create an environment | `python3 -m venv .venv` |
| Activate (macOS/Linux) | `source .venv/bin/activate` |
| Activate (Windows) | `.venv\Scripts\activate` |
| Deactivate | `deactivate` |
| Install a package | `pip install flask` |
| Install an exact version | `pip install flask==3.1.3` |
| List installed packages | `pip list` |
| Save the package list | `pip freeze > requirements.txt` |
| Install from the list | `pip install -r requirements.txt` |
| Check which Python is active | `which python` |
| Delete an environment | `rm -rf .venv` |

### The normal workflow

```bash
# --- once per project ---
python3 -m venv .venv
source .venv/bin/activate
pip install flask
pip freeze > requirements.txt

# --- every time you sit down to work ---
source .venv/bin/activate
python app.py
# ... work ...
deactivate          # or just close the terminal
```

---

## Concepts Map — What You Already Know → Virtual Environments

| You Already Know | How It Applies Here |
|---|---|
| **Folders and paths** | A venv is literally just a folder you can look inside |
| **`import`** | Python searches this environment's `site-packages/` for modules |
| **Modules** → your own `.py` files | Packages are the same idea, written by other people |
| **`>` redirection** | `pip freeze > requirements.txt` writes output to a file |
| **Reading a text file** | `requirements.txt` is plain text — open it, it's just a list |
| **Scope** → local vs global variables | Same idea for packages: a venv is *local* scope, system Python is *global* |

That last one is the clearest way to think about it. A local variable exists only
inside its function and doesn't disturb anything outside. A virtual environment's
packages exist only inside that project and don't disturb anything outside.
