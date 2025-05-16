# Coffee Machine Project
import art
import menu_data as md
import resources_data as rd

def sufficient_resources(order_ingredients):
    for item in order_ingredients:
        if rd.resources[item] < order_ingredients[item]:
            print(f"Sorry, we're lacking out of {item}")
            return False
    return True

def calculate_money():
    user_cash = 0
    print("Please insert coins into the machine.")
    user_cash += int(input("How many Half Dollars ($0,50) do you have?\n")) * 0.5
    user_cash += int(input("How many Quarters ($0,25) do you have?\n")) * 0.25
    user_cash += int(input("How many Dimes ($0,10) do you have?\n")) * 0.25
    user_cash += int(input("How many Nickels ($0,05) do you have?\n")) * 0.25
    user_cash += int(input("How many Pennies ($0,01) do you have?\n")) * 0.25
    return user_cash

def calculate_transaction(total_received, cost):
    if total_received >= cost:
        print(f"Here is your change: ${total_received - cost}")
        return True
    else:
        print(f"Sorry, you don't have enough money! You paid ${total_received}, and it costed ${cost}.")
        return False

def menu_display():
    print("Here's the menu:")
    for key in md.menu:
        print(f"{key} ----------- ${md.menu[key]['cost']}")
    print("Type 'espresso', 'latte' or 'capuccino' to order!")

def report_display():
    for key in rd.resources:
        print(f"{key} ----------- {rd.resources[key]}")

def process_order(name, ingredients):
    for item in ingredients:
        rd.resources[item] -= ingredients[item]
    print(f"Here's your {name}. Enjoy!")


def main():
    machine_on = True
    print(art.logo)
    while machine_on:
        user_request = input("Type 'menu' or the name of your order to order\n")
        if user_request == "off":
            machine_on = False
        elif user_request == "menu":
            menu_display()
        elif user_request == "report":
            report_display()
        elif user_request == "espresso" or user_request == "latte" or user_request == "capuccino":
            user_choice = md.menu[user_request]
            if sufficient_resources(user_choice['ingredients']):
                user_payment = calculate_money()
                if calculate_transaction(user_payment, user_choice['cost']):
                    process_order(user_request, user_choice['ingredients'])
        else:
            print(f"Sorry, we don't have {user_request}.")

main()