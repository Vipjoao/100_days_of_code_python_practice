import random
import art
from cards_list import cards as c

def deal_cards():
    return random.choice(list(c))

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare_cards(player_score, computer_score):
    if player_score == computer_score:
        return "It's a draw"
    elif computer_score == 0:
        return "You lost, computer have a Blackjack"
    elif player_score == 0:
        return "You won, you have a Blackjack"
    elif player_score > 21:
        return "You went over 21, you lose."
    elif computer_score > 21:
        return "Computer went over 21, you won!"
    elif player_score > computer_score:
        return f"You win! He had {computer_score} and you have {player_score}!"
    else:
        return f"You lose. He had {computer_score} and you have {player_score}."
        

def play_blackjack():
    print(art.logo)
    player_score = -1
    computer_score = -1
    player_hand = []
    computer_hand = []
    game_over = False

    for _ in range(2):
        player_hand.append(deal_cards())
        computer_hand.append(deal_cards())

    while not game_over:
        player_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)
        print(f"Your cards: {player_hand}. Your current score is {player_score}.")
        print(f"Computer's first card is {computer_hand[0]}.")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, or 'n' to reject: \n")
            if user_should_deal == "y":
                player_hand.append(deal_cards())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_cards())
        computer_score = calculate_score(computer_hand)

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
    print(compare_cards(player_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': \n") == "y":
    print("\n" * 20)
    play_blackjack()