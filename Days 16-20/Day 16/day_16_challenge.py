from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import art



def main():
    machine_on = True
    print(art.logo)
    while machine_on:
        menu = Menu()
        cm = CoffeeMaker()
        money_machine = MoneyMachine()
        user_order = str(input(f"What would you like to order? 'Latte', 'Cappuccino' or 'Espresso'?\n")).lower()
        if user_order in menu.get_items():
            if cm.is_resource_sufficient(menu.find_drink(user_order)):
                if money_machine.make_payment(menu.find_drink(user_order).cost):
                    cm.make_coffee(menu.find_drink(user_order))
                else:
                    print(f"Sorry, you don't have enough money! Here's your money back!")
        elif user_order == "report":
            cm.report()
            money_machine.report()
        elif user_order == "off":
            machine_on = False
        else:
            print(f"Sorry, we don't have {user_order} at the menu.")


main()