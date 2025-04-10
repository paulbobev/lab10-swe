"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def add(a, b): 
    return a + b
def subtract(a, b): 
    return a - b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):   # raise ZeroDivisionError if a == 0
    return b / a
def logarithm(a, b):     # use math library/raise ValueError
    return math.log(a,b)
def exponent(a, b): 
    return math.pow(a,b)