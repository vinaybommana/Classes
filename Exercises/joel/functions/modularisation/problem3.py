# Build a password strength checker by writing these functions:

# has_minimum_length(password, min_length=8) — returns True if the password is at least min_length characters long.
# has_uppercase(password) — returns True if the password contains at least one uppercase letter.
# has_digit(password) — returns True if the password contains at least one digit.
# has_special_char(password) — returns True if the password contains at least one special character from !@#$%^&*.
# validate_password(password) — uses all four functions above to check the password. Returns a tuple: (is_valid, list_of_failures) where is_valid is True only if all checks pass, and list_of_failures contains messages for each failed check.


def has_minimum_length(password, min_length=8):
    if len(password) < min_length:
        return False
    else:
        return True


def has_uppercase(password):
    for c in password:
        if ord(c) >= 65 and ord(c) <= 90:
            return True

    return False

def has_digit(password):
    for c in password:
        if c.isdigit():
            return True
    
    return False

def has_special_char(password):
    for c in password:
        if ord(c) >= 32 and ord(c) <= 47:
            return True
        elif ord(c) >= 58 and ord(c) <= 64:
            return True
        elif ord(c) >= 91 and ord(c) <= 96:
            return True
        elif ord(c) >= 123 and ord(c) <= 126:
            return True
    else:
        return False
    

# print(has_minimum_length("abcdefgh"))
# print(has_uppercase("abc"))
# print(has_digit("a"))
# print(has_special_char("a!b"))


def validate_password(password):
    # print(has_minimum_length(password))
    # print(has_uppercase(password))
    # print(has_digit(password))
    # print(has_special_char(password))
    return has_minimum_length(password) and \
           has_uppercase(password) and \
           has_digit(password) and has_special_char(password)


print(validate_password("Ab1!xyzw"))
