
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? s, m or l?\n")
pepperoni = input("Do you want pepperoni? y/n\n")
cheese = input("Do you want extra cheese? y/n\n")
bill = 0

if size == "s":
    bill += 25
    print("Your large pizza will cost $15.")
elif size == "m":
    bill += 20
    print("Your medium pizza will cost $20.")
else:
    bill += 25
    print("Your small pizza will cost $25.")
    if pepperoni != "n" and size == "s":
        bill += 1
    elif pepperoni == "y":
        bill += 3
if cheese == "y":
    bill += 1
print(f"Your total bill is: ${bill}")
