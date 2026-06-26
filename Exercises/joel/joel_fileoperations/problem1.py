# Problem 1: Write a Greeting
# Write a program that creates a file called greeting.txt and writes the following three lines to it:

# Hello, World!
# Welcome to Python.
# File operations are fun!

with open("greeting.txt", "w") as f:
    f.write("""
Hello, World!
Welcome to Python.
File operations are fun!
""")