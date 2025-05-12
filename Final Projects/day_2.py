
print("Welcome to the tip calculator!")
total_bill = int(input("What was the total bill?\n"))
total_tip = int(input("How much in % would you like to tip?\n"))
how_many_people = int(input("How many people to split the bill?\n"))

final_price_before_splitting = total_bill + (total_bill * (total_tip / 100))
final_price = final_price_before_splitting / how_many_people

print(f"Each person should pay ${round(final_price, 2)}.")