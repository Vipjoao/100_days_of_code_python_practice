# Nested lists and dictionaries are when you have:
# List inside list
# A dictionary inside list
# A list inside dictionary
# A dictionary inside a dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

print(travel_log["France"][1]) # Lillie

nested_list = ["a", "b", "c", [1, 2, 3]]
print(nested_list[3][1]) # prints 2

travel_log2 = {
    "France": {
        "total_visits": 4,
        "cities_visited": ["Paris", "Dijon", "Madrid"], # Nested list, inside a nested dictionary, inside a dictionary.
    },
    "Germany": {
        "total_visits": 2,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],

    },
}

print(travel_log2["Germany"]["cities_visited"][0]) #Berlin