from random import randint

# dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) # Original code
# print(dice_images[dice_num])


"""In order to fix the code, we simply have to read that the original
code's error was 'Index out of range'.
 And with that error we can remember that the range inside a list
 starts on the index 0 and not 1.
 So for we to have an index 6, we need to have 7 items in our list"""
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5) # Fixed code
print(dice_images[dice_num])
