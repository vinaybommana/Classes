# Problem 1: Phone Book Lookup
# Create a dictionary called phone_book with the following contacts:

# Name	Phone Number
# Alice	555-1234
# Bob	555-5678
# Charlie	555-9012
# Then:

# Print Bob's phone number
# Add a new contact: Diana with number 555-3456
# Update Alice's number to 555-0000
# Print the entire phone book


phone_book = dict() # empty dictionary
phone_book = {
    "alice": "555-1234",
    "bob": "555-5678",
    "charlie": "555-9012"
}

# bob's phone number
print(f"Bob's phone number is {phone_book['bob']}")

# Add a new contact: Diana with number 555-3456
# update()
phone_book["diana"] = "555-3456"
# phone_book.update({"diana": "555-3456"})


# Update Alice's number to 555-0000
phone_book["alice"] = "555-0000"

print(phone_book)