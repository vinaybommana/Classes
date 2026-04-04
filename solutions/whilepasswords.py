passwords = ["hello", "p@ssw0rd!", "abc", "securePass123", "hi"]

i = 0
while i < len(passwords):
    # print(passwords[i])
    passw = passwords[i]
    if len(passw) >= 8:
        print(f"{passw} is valid")
    else:
        print(f"{passw} is too short")
    i += 1

# for i in passwords:
#     print(i)
    