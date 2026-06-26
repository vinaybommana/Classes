# Write a function called min_max that takes a list of numbers and returns both the minimum and maximum values as a tuple.

import math

def min_max(*numbers):
    return min(numbers), max(numbers)

minimum_number, maximum_number = min_max(1, 2, 3, 4)