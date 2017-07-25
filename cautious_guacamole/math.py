"""
A tiny set of functions which do math.
"""

# Write a function named add that adds two values


def add(a, b):
    c = a + b
    return c
"""
Function to multiply two values
"""
def mult(a1, a2):
    return a1 * a2
"""
Function to divide the first value by the second
"""
def div(a1, a2):
    if(a2 == 0):
        raise ZeroDivisionError("Cannot divide by 0! (duh)")
    return a1 / a2
"""
Function to give the remainder
"""
def mod(a1, a2):
    return a1 % a2
