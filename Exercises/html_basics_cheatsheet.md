# HTML Basics Cheatsheet

Every page you have ever looked at in a browser — Google, Wikipedia, your bank
— arrived as a plain text file written in HTML. Not a picture, not an app. Text.

```
 server ──────────────►  browser
         <h1>Hello</h1>
                              the browser reads the text
                              and DRAWS it
```

You have already sent HTML from Flask (`return "<h1>Hello</h1>"`). This
cheatsheet is the step backwards we skipped: **what that text is actually made
of**, before we worry about making it pretty or interactive.

---

## 1. What HTML Is — and Isn't

**HTML** = **H**yper**T**ext **M**arkup **L**anguage.

*Markup* means: take plain text, and **mark it up** with notes saying what each
bit *is*. A browser then knows how to draw it.

```
 Plain text                   Marked-up text              What you see
 ──────────                   ──────────────              ────────────
 Shopping list        →   <h1>Shopping list</h1>     →    Shopping list   (big, bold)
 Milk                 →   <li>Milk</li>              →      • Milk
```

### HTML is not a programming language

This trips up everybody coming from Python. There is **no logic in HTML**.

| HTML has | HTML does **not** have |
|---|---|
| tags that describe content | variables |
| attributes that configure them | `if` / `else` |
| nesting | loops |
| | functions |
| | arithmetic |

You cannot write "show this only on Tuesdays" in HTML. HTML is a **description
of a document** — the nouns, not the verbs. Logic lives in your Python (Flask)
before the HTML is sent, or in JavaScript after it arrives.

> **The three languages of a web page, and the one question each answers:**
>
> | Language | Question | Example |
> |---|---|---|
> | **HTML** | *What is it?* | "this is a heading, this is a button" |
> | **CSS** | *What does it look like?* | "headings are blue, buttons are rounded" |
> | **JavaScript** | *What does it do?* | "when the button is clicked, show a menu" |

Today is entirely the first row.

### Key Points

- HTML describes **structure and meaning**, never appearance or behaviour.
- A browser is extremely forgiving — broken HTML still renders *something*,
  which is exactly why bugs are hard to spot. No error messages here.

---

## 2. Anatomy of a Tag

This is the whole syntax of HTML. There is genuinely not much more to it.

```
      opening tag                     closing tag
      ───────────                     ───────────
          <a href="https://wikipedia.org">Wiki</a>
           │  └──────────┬───────────┘  └─┬┘    │
           │             │                │     └── the slash marks the end
           │             │                └──────── content (what the user sees)
           │             └───────────────────────── attribute: name="value"
           └─────────────────────────────────────── tag name
```

Opening tag + content + closing tag = an **element**.

| Part | Rule |
|---|---|
| Tag name | lowercase by convention (`<p>`, not `<P>`) |
| Attribute | always `name="value"`, quotes around the value |
| Multiple attributes | separated by spaces: `<input type="text" name="user">` |
| Closing tag | same name with a `/` in front |

### Empty (self-closing) elements

A few tags have no content, so they have no closing tag:

```html
<br>                                  <!-- a line break           -->
<hr>                                  <!-- a horizontal rule      -->
<img src="cat.jpg" alt="A cat">       <!-- an image               -->
<input name="username">               <!-- a form field           -->
<meta charset="UTF-8">                <!-- page metadata          -->
<link rel="stylesheet" href="s.css">  <!-- attaches a stylesheet  -->
```

You will also see `<br />` with a trailing slash. That is old XHTML style —
harmless, still works, no longer required.

### Nesting — the one rule that actually matters

Tags must close in the **reverse order** they were opened, like brackets in
Python.

```html
<p>This is <strong>very</strong> important.</p>     <!-- ✅ correct     -->
<p>This is <strong>very</p></strong>                <!-- ❌ overlapping -->
```

```
 ✅  <p> ... <strong> ... </strong> ... </p>
      └───────────────────────────────────┘
              └──────────────────┘            inner closes first

 ❌  <p> ... <strong> ... </p> ... </strong>
      └──────────────────────┘
              └───────────────────────┘       they cross — invalid
```

Think of it exactly like `([)]` in Python — that is a syntax error, and this is
the same mistake. Indent your HTML and the nesting becomes visible.

### Key Points

- Element = opening tag + content + closing tag.
- Attributes go in the **opening tag only**, never the closing one.
- Nest, never overlap. Indentation is how you see it.

---

## 3. The Skeleton of Every Page

Every HTML file you ever write starts the same way. This is `Exercises/basic.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <p>Hello world</p>
</body>
</html>
```

Line by line:

| Line | Job | What if you leave it out |
|---|---|---|
| `<!DOCTYPE html>` | "this is modern HTML5" | browser enters *quirks mode* and mimics 1998 bugs |
| `<html lang="en">` | wraps everything; declares the language | screen readers mispronounce; translation offers break |
| `<head>` | information **about** the page | — |
| `<meta charset="UTF-8">` | how to decode the bytes | accents and emoji turn into `â€™` garbage |
| `<meta name="viewport" ...>` | "respect the real phone width" | phones render a tiny zoomed-out desktop page |
| `<title>` | the browser tab / bookmark name | tab shows the raw file path |
| `<link rel="stylesheet">` | attach the CSS | page renders unstyled |
| `<body>` | everything the user actually sees | nothing visible |

### head vs body — the split that confuses everyone

```
 ┌──────────────────────────────────────────────┐
 │ <head>   INFORMATION ABOUT THE PAGE          │   invisible
 │          title, charset, stylesheets,        │   (except the tab title)
 │          description for Google              │
 ├──────────────────────────────────────────────┤
 │ <body>   THE PAGE ITSELF                     │   visible
 │          headings, text, images, links,      │
 │          forms, buttons                      │
 └──────────────────────────────────────────────┘
```

> Content the user reads → `<body>`. Settings for the browser → `<head>`.

Putting a `<h1>` in the `<head>` is the classic beginner bug: nothing appears,
no error. (Browsers quietly "fix" it by moving the tag into the body — which is
why it *sometimes* works and teaches you the wrong lesson.)

### Other things that live in `<head>`

```html
<meta name="description" content="A short summary Google shows in results.">
<meta name="author" content="Joel">
<link rel="icon" href="favicon.ico">        <!-- the little tab icon -->
<script src="script.js" defer></script>     <!-- JavaScript          -->
```

### Key Points

- Memorise this skeleton. In VS Code, typing `!` then `Tab` generates it for
  you (the Emmet shortcut) — but know what each line does.
- `<html>`, `<head>`, `<body>` — exactly one of each, in that order.

---

## 4. Text — Headings and Paragraphs

```html
<h1>Biggest heading — the page title</h1>
<h2>A major section</h2>
<h3>A sub-section</h3>
<h4>…</h4>  <h5>…</h5>  <h6>Smallest heading</h6>

<p>A paragraph. The browser adds space above and below automatically.</p>
```

### Headings are an outline, not a font size

`<h1>`–`<h6>` are the page's **table of contents**. They happen to get smaller,
but that is a side effect, not the purpose.

```
 <h1>  Python Course              ← one per page, what the page IS
   <h2>  Week 1: Basics           ← major sections
     <h3>  Variables
     <h3>  Loops
   <h2>  Week 2: Functions
```

| Rule | Why |
|---|---|
| **One `<h1>` per page** | it is the page's name |
| **Don't skip levels** (`h2` → `h4`) | it breaks the outline |
| **Never pick a heading for its size** | use CSS for size; use the level for meaning |

Screen readers let blind users jump heading to heading — a skipped level is a
missing rung on the ladder. Google reads the same outline to understand your page.

### Whitespace is collapsed — the surprise

HTML ignores how *you* format the file. Any run of spaces, tabs, or newlines
becomes **one single space**.

```html
<p>Hello


                  world</p>
```

renders as:

```
Hello world
```

This is the opposite of Python, where whitespace is everything. Here it is
almost nothing — so indent your HTML freely for readability; it costs nothing.

To force a break, use a tag:

```html
Line one<br>Line two        <!-- a line break inside a paragraph -->
<hr>                        <!-- a horizontal divider line       -->
```

| Tag | Use it for | Don't use it for |
|---|---|---|
| `<br>` | addresses, poetry, song lyrics | spacing between paragraphs — use `<p>` and CSS `margin` |
| `<hr>` | a real topic change | drawing decorative lines — use CSS `border` |

### Inline text tags

```html
<strong>Important</strong>      <!-- bold   AND means "this matters"     -->
<em>Emphasis</em>               <!-- italic AND means "stress this word" -->
<b>Bold</b>                     <!-- bold,   no meaning                  -->
<i>Italic</i>                   <!-- italic, no meaning                  -->
<mark>Highlighted</mark>
<small>Fine print</small>
<del>Deleted</del>  <ins>Inserted</ins>
<code>request.form</code>       <!-- inline code, monospace font         -->
<pre>  keeps    your
       spacing  exactly</pre>   <!-- the ONE tag where whitespace counts -->
<blockquote>A quoted passage.</blockquote>
```

**`<strong>` vs `<b>`** (and `<em>` vs `<i>`) look identical on screen. The
difference is meaning: `<strong>` tells a screen reader to *say it more firmly*;
`<b>` just makes pixels darker. Prefer `<strong>` and `<em>`.

**`<pre>`** is the exception to whitespace collapsing — it preserves spacing and
newlines exactly. Combine with `<code>` for code blocks:

```html
<pre><code>def hello():
    print("hi")</code></pre>
```

---

## 5. Lists

Three kinds. You will use the first two constantly.

```html
<!-- Unordered: bullets. Order doesn't matter. -->
<ul>
  <li>Milk</li>
  <li>Eggs</li>
</ul>

<!-- Ordered: numbers. Order DOES matter. -->
<ol>
  <li>Install Python</li>
  <li>Create a virtualenv</li>
  <li>pip install flask</li>
</ol>

<!-- Description: term + definition pairs. -->
<dl>
  <dt>HTML</dt>
  <dd>The structure of a page.</dd>
  <dt>CSS</dt>
  <dd>The appearance of a page.</dd>
</dl>
```

| Tag | Stands for | Gives you |
|---|---|---|
| `<ul>` | unordered list | • bullets |
| `<ol>` | ordered list | 1. 2. 3. numbering |
| `<li>` | list item | one entry (used by both) |
| `<dl>` / `<dt>` / `<dd>` | description list / term / definition | a glossary |

### Key Points

- **Only `<li>` may be a direct child of `<ul>`/`<ol>`.** Loose text between
  items is invalid.
- Lists **nest** — put a whole `<ul>` *inside* an `<li>`, not between items:

```html
<ul>
  <li>Backend
    <ul>
      <li>Flask</li>
      <li>Django</li>
    </ul>
  </li>
  <li>Frontend</li>
</ul>
```

- Navigation menus are lists of links — that is the standard, and why
  `<nav><ul><li><a>` is such a common sight.
- The numbers in `<ol>` are generated by the browser. Never type "1." yourself.

---

## 6. Links — the "Hyper" in HyperText

A link is what makes the web a *web* rather than a pile of documents.

```html
<a href="https://wikipedia.org">Visit Wikipedia</a>
   └┬─┘  └──────────┬─────────┘ └──────┬──────┘
    │               │                  └── the clickable text
    │               └───────────────────── where it goes
    └───────────────────────────────────── "anchor"
```

`href` = **h**ypertext **ref**erence. No `href`, no link.

### Four kinds of destination

```html
<a href="https://wikipedia.org/wiki/Main_Page">Another site</a>   <!-- absolute -->
<a href="/about">Another page on this site</a>                    <!-- root-relative -->
<a href="contact.html">A file next to this one</a>                <!-- relative -->
<a href="#section-3">Further down this page</a>                   <!-- fragment -->
<a href="mailto:joel@example.com">Email me</a>                    <!-- bonus -->
```

| Form | Starts with | Means |
|---|---|---|
| **Absolute** | `https://` | a full address — use for other websites |
| **Root-relative** | `/` | from the top of *this* site — `/about`, `/login` |
| **Relative** | a filename | relative to the current file — `contact.html`, `../index.html` |
| **Fragment** | `#` | jump to `id="section-3"` on this page |

In Flask you will almost always write root-relative links (`/login`) because
they match your routes — and later `url_for('login')`, which generates them for
you so a renamed route can't break your links.

### Opening in a new tab

```html
<a href="https://wikipedia.org" target="_blank" rel="noopener">Wikipedia</a>
```

`target="_blank"` opens a new tab. Add `rel="noopener"` — without it the new
page gets a JavaScript handle back to yours, which is a real security hole.
Use it sparingly; hijacking the back button annoys people.

### Key Points

- Link text should make sense **read on its own**. "Click here" tells a screen
  reader user nothing; "the Flask cheatsheet" tells them everything.
- Anything can go inside `<a>` — wrap an `<img>` to make a clickable image.
- A broken `href` gives you a `404`, which is Flask saying *"no route matches
  that path"*.

---

## 7. Images and Media

```html
<img src="cat.jpg" alt="A ginger cat asleep on a keyboard" width="400">
```

| Attribute | Purpose | Required? |
|---|---|---|
| `src` | the image file's path or URL | **yes** |
| `alt` | text shown if the image fails, read aloud by screen readers | **yes** |
| `width` / `height` | size in pixels | no, but see below |

### `alt` is not optional

Three audiences need it, and only one of them is unusual:

1. Blind users — the screen reader reads the `alt` instead of the picture.
2. Anyone on a bad connection — the image fails, the text explains what was lost.
3. Google — it cannot see pictures either.

```html
<img src="chart.png" alt="Sales doubled between 2024 and 2025">   <!-- ✅ describes it -->
<img src="chart.png" alt="chart">                                 <!-- ❌ useless       -->
<img src="divider.png" alt="">                                    <!-- ✅ purely decorative -->
```

An empty `alt=""` is the correct, deliberate way to say *"this is decoration,
skip it"*. Omitting `alt` entirely reads the filename aloud — worst of both.

### Set width and height

Give the real pixel dimensions and the browser reserves the space before the
image loads, so your text doesn't jump around as the page fills in.

### Formats

| Format | Best for |
|---|---|
| `.jpg` | photographs |
| `.png` | screenshots, logos, anything needing transparency |
| `.svg` | icons and diagrams — vector, scales to any size, tiny |
| `.webp` | modern replacement for jpg/png, smaller files |
| `.gif` | simple animations (largely replaced by video) |

### Audio and video

```html
<video src="demo.mp4" controls width="600"></video>
<audio src="song.mp3" controls></audio>
```

Without `controls` there are no play buttons and nothing appears to happen.

### In Flask

Images are **static files**, so they live in `static/` and get linked with
`url_for` — the same pattern as your stylesheet:

```html
<img src="{{ url_for('static', filename='cat.jpg') }}" alt="A cat">
```

---

## 8. Tables — for Data, Not Layout

```html
<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Joel</td>
      <td>92</td>
    </tr>
    <tr>
      <td>Asha</td>
      <td>88</td>
    </tr>
  </tbody>
</table>
```

| Tag | Stands for | Is |
|---|---|---|
| `<table>` | table | the whole grid |
| `<tr>` | table row | one horizontal row |
| `<th>` | table header | a heading cell — bold and centred by default |
| `<td>` | table data | an ordinary cell |
| `<thead>` / `<tbody>` / `<tfoot>` | — | optional grouping; helps styling and printing |
| `<caption>` | — | a title for the table (put it first, inside `<table>`) |

### The mental model

A table is built **row by row**, not column by column. There is no "column"
tag — a column is just "the third `<td>` in every row". Get this and tables
stop being confusing.

```
<tr>  →   ┌────────┬────────┐
          │  <th>  │  <th>  │
<tr>  →   ├────────┼────────┤
          │  <td>  │  <td>  │
<tr>  →   ├────────┼────────┤
          │  <td>  │  <td>  │
          └────────┴────────┘
```

Every row needs the **same number of cells**, or the grid goes ragged.

### Spanning cells

```html
<td colspan="2">Spans two columns</td>
<td rowspan="3">Spans three rows</td>
```

### Key Points

- Use tables for **tabular data** — things with rows and columns: results,
  prices, schedules.
- **Never use a table to lay out a page.** That was the 1990s workaround before
  CSS existed. It is unreadable to screen readers and breaks on phones. Layout
  is CSS's job (`flexbox`, `grid`).
- This is the structure you will generate with a Jinja `{% for %}` loop over a
  database query — a very common pattern.

---

## 9. Block vs Inline — Why Things Sit Where They Do

Every element is one of two kinds, and this single distinction explains most
"why is it on the wrong line?" confusion.

```
 BLOCK                              INLINE
 ┌──────────────────────────────┐   ┌──────┐┌──────┐┌────────┐
 │ takes the FULL width         │   │ only ││ as   ││ wide as│
 └──────────────────────────────┘   └──────┘└──────┘└────────┘
 ┌──────────────────────────────┐    its content needs, and
 │ next one starts a NEW LINE   │    they sit side by side
 └──────────────────────────────┘    like words in a sentence
```

| | Block | Inline |
|---|---|---|
| Width | fills its container | only as wide as its content |
| Line breaks | starts on a new line | flows within the line |
| Can contain | block *and* inline elements | only text and other inline elements |
| `width` / `height` in CSS | respected | ignored |
| Examples | `<p>` `<div>` `<h1>`–`<h6>` `<ul>` `<li>` `<table>` `<form>` `<section>` | `<a>` `<span>` `<strong>` `<em>` `<img>` `<input>` `<code>` |

This is why, in the CSS cheatsheet, `display: block` on a `<label>` was needed
to stack form fields — labels and inputs are inline by default, so they line up
side by side like words.

CSS can override the default with `display: block`, `display: inline`, or
`display: inline-block`. But knowing the **default** is what lets you predict
the page before you write any CSS.

### `<div>` and `<span>` — the two meaningless tags

```html
<div>A generic block-level box.</div>
<span>A generic inline piece of text.</span>
```

They have **no meaning at all**. They exist purely as hooks to hang CSS and
JavaScript on, for when no meaningful tag fits.

| Tag | Kind | Use when |
|---|---|---|
| `<div>` | block | you need to group a chunk of the page to style or position it |
| `<span>` | inline | you need to style a few words inside a sentence |

```html
<p>Your balance is <span class="danger">-₹500</span> today.</p>
```

> **Rule of thumb:** reach for `<div>` only after checking that no real tag
> fits. If the chunk is the navigation, use `<nav>`. If it's an article, use
> `<article>`. Which brings us to…

---

## 10. Semantic HTML — Tags That Mean Something

Compare these. They look **identical** in a browser:

```html
<!-- "div soup" — technically works, says nothing -->
<div id="top">
  <div id="menu">…</div>
</div>
<div id="content">
  <div class="post">…</div>
</div>
<div id="bottom">…</div>
```

```html
<!-- semantic — same layout, now it has meaning -->
<header>
  <nav>…</nav>
</header>
<main>
  <article>…</article>
</main>
<footer>…</footer>
```

A **semantic** tag describes *what the content is*, not just that it's a box.

| Tag | Means |
|---|---|
| `<header>` | introductory content — logo, site title (can appear more than once) |
| `<nav>` | a block of navigation links |
| `<main>` | the main content — **exactly one per page**, and no repeated stuff like nav or footer |
| `<article>` | a self-contained item that would make sense alone — a blog post, a comment, a product card |
| `<section>` | a thematic grouping, normally with its own heading |
| `<aside>` | tangential content — a sidebar, a pull quote, related links |
| `<footer>` | closing content — copyright, contact, small print |
| `<figure>` / `<figcaption>` | an image/diagram **with its caption attached** |

### Why bother, if it looks the same?

| Audience | What semantics buys them |
|---|---|
| **Screen readers** | users can jump straight to `<main>`, skipping the nav — every page, every site |
| **Search engines** | Google tells your article apart from your sidebar and ranks accordingly |
| **Other developers** | `</section>` tells you what just ended; `</div>` tells you nothing |
| **Browser features** | Reader Mode and "Print this page" find the real content |
| **You, in six months** | 40 nested `<div>`s are genuinely hard to debug |

It is the same argument as naming a Python variable `total_price` instead of
`x`. The computer does not care. Everyone else does — including you, later.

### A typical page skeleton

```html
<body>
  <header>
    <h1>My Blog</h1>
    <nav>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <article>
      <h2>My First Post</h2>
      <p>Hello world.</p>
    </article>
  </main>

  <footer>
    <p>&copy; 2026 Joel</p>
  </footer>
</body>
```

### `<section>` vs `<div>`, briefly

If the chunk has (or could have) its own heading, it's a `<section>`. If you
are only wrapping it to push it around with CSS, it's a `<div>`.

---

## 11. Attributes You Meet Everywhere

Some attributes work on **any** tag ("global attributes"):

```html
<p id="intro" class="lead highlight" title="Hover text">Hello</p>
```

| Attribute | Purpose | Notes |
|---|---|---|
| `id` | a **unique** name for one element | one per page, each used once |
| `class` | a **reusable** label for styling | one tag may have several, space-separated |
| `style` | inline CSS | avoid — use a stylesheet |
| `title` | tooltip on hover | invisible on touchscreens; don't hide anything important here |
| `hidden` | don't display this at all | |
| `data-*` | your own custom data | `data-user-id="42"` — read by JavaScript |

### `id` vs `class` — the distinction to get right now

```html
<div id="login-form" class="card shadow">
     └──── one only ───┘ └── reusable, many allowed ──┘
```

| | `id` | `class` |
|---|---|---|
| How many elements may have it | exactly one | as many as you like |
| How many may one element have | one | several, space-separated |
| CSS selector | `#login-form` | `.card` |
| Used by | `<label for>`, `#fragment` links, JavaScript | styling |

**Use classes for styling.** Reserve `id` for things that must be addressable
individually: a `<label for>`, a `#jump-link`, a JavaScript hook.

> And remember the trap from the forms cheatsheet: `id` is for the **browser**,
> `name` is for the **server**. Only `name` is ever sent over the network.

---

## 12. Comments and Entities

### Comments

```html
<!-- This is a comment. The browser ignores it. -->
```

Python's `#` means nothing in HTML. And note: comments are **visible in View
Source**. Never put a password, a note about a security hole, or anything rude
about a colleague in one.

### Entities — escaping characters that mean something

How do you write `<` in your text when `<` starts a tag? You escape it.

| You want | You type | Why |
|---|---|---|
| `<` | `&lt;` | otherwise it starts a tag |
| `>` | `&gt;` | pairs with the above |
| `&` | `&amp;` | otherwise it starts an entity |
| `"` | `&quot;` | inside an attribute value |
| a space that won't collapse | `&nbsp;` | non-breaking space |
| `©` | `&copy;` | |
| `₹` | `&#8377;` | any character by number |

Every entity is `&name;` — the semicolon is required.

```html
<p>Use &lt;p&gt; for paragraphs.</p>     <!-- displays: Use <p> for paragraphs. -->
```

### This is a security issue, not just typing

If a user types `<script>…</script>` into your Flask form and you print it
straight back onto a page, the browser **runs it**. That attack is called
**XSS** (cross-site scripting).

The good news: Jinja already escapes `{{ variable }}` for you automatically —
this is why `{{ }}` is safe by default and why you should be very suspicious of
the `|safe` filter.

---

## 13. Forms — the Interactive Part

Forms are how the browser sends data **back** to your Python. They are a large
enough topic to have their own cheatsheet, but in outline:

```html
<form action="/login" method="POST">
  <label for="username">Username</label>
  <input id="username" name="username" type="text" required>
  <button type="submit">Log in</button>
</form>
```

| Tag | Job |
|---|---|
| `<form>` | the envelope — `action` (where) and `method` (how) |
| `<input>` | a field — `type=` changes it from text to password, date, checkbox… |
| `<label>` | the question, tied to a field by `for` / `id` |
| `<select>` / `<option>` | a dropdown |
| `<textarea>` | multi-line text |
| `<button>` | sends it |

**→ Full detail in `html_forms_css_cheatsheet.md`**: `name=` vs `id`, GET vs
POST, the input zoo, validation, and reading it all in Flask with
`request.form`.

---

## 14. The Document Tree

Because elements nest and never overlap, an HTML page is a **tree** — exactly
like nested dictionaries and lists in Python.

```html
<body>
  <h1>Title</h1>
  <p>Some <strong>bold</strong> text.</p>
</body>
```

```
                body
                 │
         ┌───────┴───────┐
        h1               p
         │          ┌────┴────┐
      "Title"    "Some "   strong
                              │
                           "bold"
```

The browser builds this tree in memory and calls it the **DOM** (Document
Object Model). It matters because:

- **CSS** walks the tree: `.card input` means *"an input somewhere inside a
  `.card`"* — a descendant.
- **JavaScript** edits the tree live, which is how pages change without reloading.
- **Parent / child / sibling** is the vocabulary everyone uses for page structure.

| Term | Meaning (in the diagram) |
|---|---|
| **Parent** | `p` is the parent of `strong` |
| **Child** | `h1` and `p` are children of `body` |
| **Sibling** | `h1` and `p` are siblings |
| **Descendant** | `strong` is a descendant of `body` |

You already think this way from nested data: `data["users"][0]["name"]` is
walking a tree. Same idea, different notation.

---

## 15. Seeing It Yourself — Browser Tools

Two shortcuts worth showing in class, because HTML gives you no error messages:

| Tool | How | What it shows |
|---|---|---|
| **View Source** | `Ctrl/Cmd + U` | the **exact text** the server sent — proof that pages are just text |
| **Inspect / DevTools** | `F12`, or right-click → Inspect | the **live tree**, editable; hover a tag to highlight it on the page |

In DevTools you can change any text or style and watch the page update
instantly. Nothing is saved — refresh and it's back — which makes it the safest
possible place to experiment.

Open any site your students know and View Source. Seeing Wikipedia as plain
text with tags, written the same way as `basic.html`, is the moment the whole
thing clicks.

> **The validator:** paste your page into
> [validator.w3.org](https://validator.w3.org) and it will list every
> unclosed tag and misplaced element. Closest thing HTML has to a Python
> traceback.

---

## 16. A Complete Page, Everything Together

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Joel's Web App</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <header>
    <h1>Joel's Web App</h1>
    <nav>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/login">Log in</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <article>
      <h2>Week 1 Results</h2>
      <p>We scored <strong>92%</strong> on the first exercise set.</p>

      <table>
        <caption>Scores by student</caption>
        <thead>
          <tr><th>Name</th><th>Score</th></tr>
        </thead>
        <tbody>
          <tr><td>Joel</td><td>92</td></tr>
          <tr><td>Asha</td><td>88</td></tr>
        </tbody>
      </table>
    </article>

    <aside>
      <h2>Useful links</h2>
      <ul>
        <li><a href="https://wikipedia.org">Wikipedia</a></li>
        <li><a href="https://docs.python.org">Python docs</a></li>
      </ul>
    </aside>
  </main>

  <footer>
    <p>&copy; 2026 Joel &mdash; built in class.</p>
  </footer>

</body>
</html>
```

Read it against the checklist:

- [x] `<!DOCTYPE html>` and `lang="en"`
- [x] `charset` and `viewport` in the `<head>`
- [x] exactly one `<h1>`, headings in order
- [x] semantic landmarks: `header`, `nav`, `main`, `article`, `aside`, `footer`
- [x] navigation is a **list** of links
- [x] the table has `<thead>`, `<th>` and a `<caption>`
- [x] `&copy;` escaped as an entity
- [x] not a single `<div>` — nothing needed one

---

## Quick Reference

| Concept | Syntax |
|---|---|
| Page skeleton | `<!DOCTYPE html><html><head>…</head><body>…</body></html>` |
| Comment | `<!-- text -->` |
| Headings | `<h1>` … `<h6>` |
| Paragraph | `<p>text</p>` |
| Line break / divider | `<br>` / `<hr>` |
| Bold / italic (with meaning) | `<strong>` / `<em>` |
| Preformatted text | `<pre>` |
| Bullet list | `<ul><li>item</li></ul>` |
| Numbered list | `<ol><li>item</li></ol>` |
| Link | `<a href="/path">text</a>` |
| New tab | `<a href="…" target="_blank" rel="noopener">` |
| Image | `<img src="x.jpg" alt="description">` |
| Table | `<table><tr><th>…</th></tr><tr><td>…</td></tr></table>` |
| Generic block / inline box | `<div>` / `<span>` |
| Page landmarks | `<header> <nav> <main> <article> <aside> <footer>` |
| Unique name | `id="name"` → CSS `#name` |
| Reusable label | `class="name"` → CSS `.name` |
| Attach CSS | `<link rel="stylesheet" href="style.css">` |
| Attach JS | `<script src="script.js" defer></script>` |
| Escaped `<` `>` `&` | `&lt;` `&gt;` `&amp;` |
| Form | `<form action="/url" method="POST">` |
| Static file in Flask | `{{ url_for('static', filename='x.css') }}` |

---

## Common Problems

| What you see | What's wrong | Fix |
|---|---|---|
| Page renders but looks ancient / spacing is odd | missing `<!DOCTYPE html>` | add it as line 1 |
| Everything after some point is bold or a link | a tag was never closed | find the unclosed `<strong>` / `<a>` |
| Content doesn't appear at all | it's in `<head>` instead of `<body>` | move it into `<body>` |
| Accents or emoji show as `â€™` | missing `<meta charset="UTF-8">` | add it to `<head>` |
| Page is tiny and zoomed out on a phone | missing viewport `<meta>` | add the viewport line |
| My blank lines and spaces vanished | HTML collapses whitespace | use `<p>`, `<br>`, or CSS `margin` |
| Two elements won't sit side by side | they're block-level | CSS `display: inline-block` or flexbox |
| Two elements won't stack | they're inline | CSS `display: block` |
| Image shows a broken icon | wrong `src` path | check the path; in Flask use `url_for('static', …)` |
| Image works locally, breaks on the server | an absolute path like `C:\Users\…` | use a relative or `static/` path |
| CSS rule has no effect | wrong selector, or the browser cached the file | `.` for class, `#` for id; hard refresh `Cmd/Ctrl + Shift + R` |
| Styling one element changed several | you styled a tag or a shared class | use a more specific selector |
| Clicking a link does nothing | missing or empty `href` | add a real `href` |
| Link gives `404` | no Flask route matches that path | match `href` to an `@app.route` |
| Table looks ragged | rows have different cell counts | same number of `<td>` in every `<tr>` |
| Literal `<p>` text appears on the page | you escaped it, or Jinja did | that's `&lt;p&gt;` — correct if intentional |
| Page looks fine, screen readers get lost | `<div>` soup | use semantic landmarks |

---

## Concepts Map — What You Already Know → HTML

| You Already Know | HTML Equivalent |
|---|---|
| **Nested lists / dicts** → `data["users"][0]` | the document tree — elements inside elements |
| **Matching brackets** → `([)]` is an error | tags must close in reverse order |
| **Indentation shows structure** (Python *requires* it) | indentation shows nesting (HTML ignores it, you still need it) |
| **Comments** → `# note` | `<!-- note -->` |
| **Naming variables well** → `total_price` not `x` | semantic tags — `<nav>` not `<div>` |
| **Functions over copy-paste** | one external `.css` file over repeated inline `style=` |
| **Separating logic from output** | HTML (*what*) vs CSS (*how it looks*) vs JS (*what it does*) |
| **Escaping quotes** → `"he said \"hi\""` | entities — `&lt;` for a literal `<` |
| **Validating user input** | never trust what a user typed into HTML either — XSS |
| **`return` sends a value back** | Flask returns HTML text; the browser draws it |
| **A `for` loop building output** | Jinja `{% for %}` generating `<li>` or `<tr>` rows |

---

## Where This Goes Next

You can now describe a page. Three directions open up from here, and you have
already met two of them:

```
            HTML  (you are here — WHAT it is)
              │
    ┌─────────┼─────────────────────┐
    ▼         ▼                     ▼
   CSS      FORMS                 JINJA
 how it    sending data       generating HTML
  looks    back to Python     from Python data
```

| Next topic | Where |
|---|---|
| Making it look good; sending data back | `html_forms_css_cheatsheet.md` |
| Generating HTML from Python data | `examples/flask_templates/` — `{% for %}` over a list builds your `<li>` and `<tr>` rows |
| A real page wired to Python | `examples/flask_login/` |

The key realisation for the next session: **you will rarely write a full HTML
page by hand again.** You will write a *template* — HTML with holes in it — and
let Python fill the holes. But the template is still just the HTML on this
page, so everything here carries over unchanged.

---

## Practice Ideas

Build these by hand in a single `.html` file, opened directly in a browser —
no Flask, no server, just `File → Open`:

1. **A personal profile page** — heading, a paragraph about yourself, a photo
   with real `alt` text, and a list of three links you use often.
2. **A recipe page** — an `<ol>` of steps, a `<ul>` of ingredients, a photo,
   and a `<blockquote>` with a tip.
3. **A class timetable** — a `<table>` with days as columns, with `<thead>`
   and a `<caption>`.
4. **Rebuild #1 semantically** — same content, now with `<header>`, `<nav>`,
   `<main>`, `<footer>`, and zero `<div>`s.
5. **Break it on purpose** — delete a closing `</strong>`, then look at the
   page. Noticing *how* broken HTML fails is the fastest way to learn to read it.
6. **View Source on a real site** and find: the `<title>`, one `<nav>`, and one
   `<img alt="…">`.
