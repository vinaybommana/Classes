# Then write a program that opens sample.txt and prints:

# The number of lines
# The total number of words
# The total number of characters (including spaces and newlines)

with open("sample.txt", "r") as f:
    text = f.readlines() # list

number_of_lines = len(text) # first problem

lines = [] # list text ['The quick brown fox\n', 'jumps over the lazy dog\n', 'Python is awesome\n']

for line in text:
    lines.append(line.strip("\n"))

words = []

for l in lines:
    words = words + l.split(" ") # split function

number_of_words = len(words)

characters = []


# first way
for i in words:
    inner_chars = []
    for c in i:
        inner_chars.append(c)
    characters = characters + inner_chars

# second
number_of_characters_2 = 0
for i in words:
    # print(len(i))
    number_of_characters_2 = number_of_characters_2 + len(i)


number_of_characters = len(characters)

# print(number_of_lines)
# print(number_of_words)
# print(number_of_characters)
print(number_of_characters_2)