piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
# All the methods below work not only with lists, but with tuples as well
print(piano_keys[2:5])
# This will print "c", "d" and "e"
# Because the position 2 is right before the "c" and position 5 is the one right after the "e"

print(piano_keys[:5])
# This will print "a", "b", "c", "d" and "e". Because it's taking everything before the 5th position

print(piano_keys[2:])
# This will print  "c", "d", "e", "f" and "g". Because it's taking everything after the 2nd position

print(piano_keys[2:5:2])
# This will print "c" and "e"
# Because the second '2' will set the offset of the search. Meaning that it'll return every other character

print(piano_keys[::2])
# This will print "a", "c", "e" and "g"
# By doing it this way, we're taking the entire list, but skipping every other item

print(piano_keys[::-1])
# This will print "g", "f", "e", "d", "c", "b" and "a". Because it's returning the list backwards