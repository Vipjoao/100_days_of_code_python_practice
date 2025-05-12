
name = input("What is your name?\n")
print(f"Welcome! {name}, to the Treasure Iland.\nYour mission is to find the lost treasure.")

direction = input("You're in the top of a hill, do you want to go left or right?\n")
if direction == "left":
    direction = input("You fell down into a cave, but somehow you survived\ndo you want to swim the lake or go to the dark path?\n")
    if direction == "swim":
        direction = input("You find a river of aligators\nbut somehow you managed to pass through them\nand arrives in a three way split.\nDo you go, left, right or middle?\n")
        if direction == "left" or direction == "right":
            print(f"You were so close! {name}.\nBut you fell on a pit of deadly black mambas and died.")
        else:
            print(f"Congrats! {name}. You have found the hidden treasure!")
    else:
        print(f"{name} decides do try the dark path.\nBut you run into a big troll that swings his giant mace at you and you die.")
else:
    print("You slip and fall down the montain into a painful death.")