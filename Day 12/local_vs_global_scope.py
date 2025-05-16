

#Local Scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

# print(potion_strength)  wont work because it doesn't exist outside the function drink_potion

enemies = 1


def increase_enemies():
    enemies = 2 # 'enemies' is highlighted in yellow because it's being redeclared
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
