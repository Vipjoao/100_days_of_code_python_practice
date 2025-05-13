import art

print(art.logo)

print("Welcome to the secret auction program.")
another_bidder = True
bidders = {}

def get_highest_bidder(bidders):
    highest_bid = 0
    winner = ""

    for bidder in bidders:
        bid_amount = bidders[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while another_bidder:
    user_name = input("What is your name?\n")
    bid_value = float(input("What is your bid?\n"))
    bidders[user_name] = bid_value
    print(f"Bidders: {bidders}")
    redo = input("Are there another bidders? 'yes' or 'no'\n")
    if redo != "yes":
        another_bidder = False
        get_highest_bidder(bidders)
    elif redo == "yes":
        print("\n" * 20)