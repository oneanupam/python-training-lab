"""
Module: script_05
Description: Demonstrates the use of string formatting in Python.
Example:
- The older method uses the modulo operator (%) for string formatting
- The format() method allows you to create a format string with placeholders
    (curly braces {}) which are then replaced by the arguments passed to the method.
- F-strings provide a concise and readable way to embed expressions inside string literals.
    They are identified by an f or F prefix before the opening quote of the string.
"""

name = "Anupam"
exp_years = 8

# string formatting using modulo operator
print("Name: %s, Experience: %d years" % (name, exp_years))

# string formatting using format method
print("Name: {}, Experience: {} years".format(name, exp_years))

# string formatting using f-strings (Python 3.6+)
print(f"Name: {name}, Experience: {exp_years} years")
