
print("Welcome to the rollercoaster!")
height = int(input("Please enter your height in centimeters:\n"))
age = int(input("Please enter your age:\n"))

if height >= 120:
    print("You can ride the rollercoaster!")
    if age <= 12:
        bill = 14
        print("Your ticket is $14!")
    elif age <= 18 :
        bill = 17
        print("Your ticket is $17!")
    else:
        bill = 10
        print("Your ticket is $10!")

    wants_photo = input("Would you like to see a photo? (y/n):\n")
    if wants_photo == "y":
        bill += 3
        print(f"Your total bill is: ${bill}!")
else:
    print("You can't ride the rollercoaster!")