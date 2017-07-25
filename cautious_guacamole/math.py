"""
A tiny set of functions which do math.
"""

# Write a function named add that adds two values


def add(a, b):
    """
    Function to add two values
    """
    c = a + b
    return c


def mult(a1, a2):
    """
    Function to multiply two values
    """
    return a1 * a2


def div(a1, a2):
    """
    Function to divide the first value by the second
    """
    if(a2 == 0):
        raise ZeroDivisionError("Cannot divide by 0! (duh)")
    return a1 / a2


def mod(a1, a2):
    """
    Function to give the remainder
    """
    return a1 % a2

def sum(a):
    """
    Function to sum all the elements of an array
    """
    val = 0
    for i in a:
        val += i
    return val

def pow(a, b):
    """
    Function to raise the first value to the second
    """
    if type(b) is not int:
        raise Exception("Can't do fractional powers!(yet)")
    val = 1
    for i in range(b):
        val = a*pow(a,b-1)
    return val

