def sample_function(n):
    return sample_function()


sample_function()


# 5!
# = 5 * 4 * 3 * 2 * 1


def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


# factorial(5)
#.   5 * factorial(4)
#.   5 * 4 * factorial(3)
