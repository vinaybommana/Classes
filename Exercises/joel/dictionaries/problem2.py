# Given this string:

# text = "hello world"
# Write code that creates a dictionary where each character is a key and the count of how many times it appears is the value. Skip spaces.

# Expected output:

# {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

# dictionaries keys are unique


text = "quick brown fox"

dict_count = {}

text = text.replace(" ", "")
print(text)
for c in text:
    # print(c, dict_count)
    if c in dict_count.keys():
        v = dict_count[c] # obtaining the value
        v = v + 1 # incrementing it
        dict_count[c] = v # assigning
    else:
        dict_count[c] = 1

print(dict_count)
