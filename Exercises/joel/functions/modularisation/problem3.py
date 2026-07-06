# input

# passwords = ["hello", "Hello123", "H3llo!", "Ab1!xyzw"]

# for pw in passwords:
#     is_valid, failures = validate_password(pw)
#     if is_valid:
#         print(f"'{pw}' -> STRONG")
#     else:
#         print(f"'{pw}' -> WEAK: {', '.join(failures)}")


# Build a password strength checker by writing these functions:

# has_minimum_length(password, min_length=8) — returns True if the password is at least min_length characters long.
# has_uppercase(password) — returns True if the password contains at least one uppercase letter.
# has_digit(password) — returns True if the password contains at least one digit.
# has_special_char(password) — returns True if the password contains at least one special character from !@#$%^&*.
# validate_password(password) — uses all four functions above to check the password. Returns a tuple: (is_valid, list_of_failures) where is_valid is True only if all checks pass, and list_of_failures contains messages for each failed check.

def has_minimum_length(password, min_length):
    if len(password) < min_length:
        return False
    return True



def has_uppercase(password):
    for char in password:
        if ord(char) >= 65 and ord(char) <= 90:
            return True
    else:
        return False


# print(has_uppercase("1"))

def has_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False

# print(has_digit("A1"))

def has_special_characters(password):
    for char in password:
        if ord(char) >= 32 and ord(char) <= 47:
            return True
    else:
        return False
    
# print(has_special_characters("a "))

def validate_password(password):
    has_m = has_minimum_length(password, 8)
    has_d = has_digit(password)
    has_sc = has_special_characters(password)
    has_up = has_uppercase(password)

    return has_m and has_d and has_sc and has_up

passwords = ["hello", "Hello123", "H3llo!", "Ab1!xyzw"]

for pw in passwords:
    is_valid = validate_password(pw)
    if is_valid:
        print(f"'{pw}' -> STRONG")
    else:
        print(f"'{pw}' -> WEAK")


