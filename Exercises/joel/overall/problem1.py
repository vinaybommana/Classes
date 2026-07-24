text = "the cat sat on the mat the cat ate the rat on the mat"
# {"the": 5}


def count_words(input_text):
    words = input_text.split(" ")
    word_dict = {}
    for w in words:
        # print(f"word is: {w}")
        if w in word_dict:
            count = word_dict[w]
            count = count + 1
            word_dict[w] = count
            # word_dict[w] = word_dict[w] + 1
        else:
            word_dict[w] = 1

        # print(word_dict)
    
    return word_dict

# def top_n(word_dict, n):
#     highest_v = 0
#     highest_k = ""
#     for k, v in word_dict.items():
#         print(k, v)
#         if v > highest_v:
#             highest_v = v
#             highest_k = k
    
#     return highest_v, highest_k

def top_n(word_dict, n):
    items_list = []
    for k, v in word_dict.items():
        items_list.append((k, v))
    
    items_list = sorted(items_list, reverse=True, key=lambda x: x[1])
    
    return items_list[:n]

word_dict = count_words(text)
print(top_n(word_dict, 4))