import random

random_idx = random.randint(0, 5)
friends = ["Jim", "Dwight", "Michael", "Pamela", "Angela", "Holly"]

print(f"Who will pay the bill?\nThe selected number is {random_idx}!\nAnd that refers to {friends[random_idx]}!\n")

# The easier way is:
random_friend = random.choice(friends)
print(f"By printing it the easier way, the person who will pay the bill is {random_friend}!")