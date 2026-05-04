# Create a file called sample.txt with the following content (copy-paste or write it with code):

# The quick brown fox
# jumps over the lazy dog
# Python is awesome


# f = open("sample.txt", "w")
# ...
# f.close()

with open("sample.txt", "w") as f:
    f.write("""
 The quick brown fox
 jumps over the lazy dog
 Python is awesome
""")
