def add(n1, n2): # Math functions from day 10
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# High Order function that calls for the lesser functions
def calculator(number1, number2, calc_func):
    return calc_func(number1, number2)

print(calculator(10, 5, divide))

# An event listener is a function that waits for certain types of events to happen in the code
# to use specific functions determined by the event that was listened.
# Example: We could build a game that keeps going, but its only when the combat triggers
# that we'll call the combat() function.