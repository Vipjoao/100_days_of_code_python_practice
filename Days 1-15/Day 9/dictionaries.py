programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])

programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)


programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# For Loops in dictionaries will only return the key
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key]) # But that's easily solvable by calling the dictionary value in the loop