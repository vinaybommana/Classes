# Write a function called build_profile that takes a name (required), and keyword arguments age, city, and job (all with default value "Not provided"). It should return a formatted string with the profile info.

def build_profile(
        name, age="Not Provided", city="Not Provided", job="Not Provided"
    ): # keyword argument
    # global a_global_name
    return f"""
    Name: {name}
    age: {age}
    city: {city}
    job: {job}
    """


print(build_profile("joel", "student", 10, 11))