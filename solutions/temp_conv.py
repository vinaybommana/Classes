# temperature conversion


cel = input("Enter celsius value: ")
cel = float(cel) # type conversion

# fahrenheit
fahrenheit = (cel * 9/5) + 32
# kelvin
kelvin = cel + 273.15

print("fahrenheit: %f" % fahrenheit) ## format python2
print("fahrenheit: {}".format(fahrenheit)) # latest
print(fahrenheit)

print("kelvin: ")
print(kelvin)

print("fahrenheit is: %f, kelvin is: %f"  (fahrenheit, kelvin))
print("fahrenheit is: {0}, kelvin is: {1}".format(fahrenheit, kelvin))

print(f"fahrenheit: {fahrenheit}") # f-strings
print(f"kelvin: {kelvin}")

print(f"celsius: {cel}") # fstrings

# format specifiers
# 1. .format() %s, {}
# 2. f-strings