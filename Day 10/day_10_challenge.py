import art
import calculator_functions as calc

keep_going = False

ops = {
        "+": calc.add,
        "-": calc.subtract,
        "*": calc.multiply,
        "/": calc.divide,
    }

def calculator():
    print(art.logo)
    should_accumulate = True
    first_number = float(input("Please enter the first number:\n"))

    while should_accumulate:
        for symbol in ops:
            print(symbol)
        operation = input("Pick an operation.\n")
        other_number = float(input("What's the next number?\n"))
        res = ops[operation](first_number, other_number)

        print(f"{first_number} {operation} {other_number} = {res}")

        calculate_again = str(input(f"Would you like to continue calculating with: {res} type 'y'\n"
                         f"or do you want to start over? Type 'n'\n"))
        if calculate_again == "y":
            first_number = res
        elif calculate_again == "n":
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()