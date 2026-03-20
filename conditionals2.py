fruit = input("what are you eating today: ")

# apple, orange, grape, strawberry

# if fruit == "apple":
#     print(f"{fruit} is a good one")
# elif fruit == "orange":
#     print(f"{fruit} is a bad one")
# elif fruit == "grape":
#     print(f"{fruit} is a neutral one")
# elif fruit == "strawberry":
#     print(f"{fruit} is a pink one")
# else:
#     print(f"I don't know this: {fruit}")

# match case # switch case
match fruit:
    case "apple":
        print(f"{fruit} is a good one")
    case "orange":
        print(f"{fruit} is a bad one")
    case "grape":
        print(f"{fruit} is neutral one")
    case "strawberry":
        print(f"{fruit} is a pink one")
    # default
    case _:
        print(f"I don't know this one: {fruit}")