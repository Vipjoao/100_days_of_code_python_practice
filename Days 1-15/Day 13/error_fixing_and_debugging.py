# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it") # Original function
# my_function()


"""In order to fix the code, we simply have to read that the original
code's error was 'Index out of range'.
 And with that error we can remember that the range inside a list
 starts on the index 0 and not 1.
 So for we to have an index 20, we need to have 21 items in our list"""
def r_function():
    for i in range(1, 21): # Fixed function
        if i == 20:
            print("Got it")
r_function()
