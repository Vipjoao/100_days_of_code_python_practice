import random
import art

def choose_difficulty():
    difficulty = str(input("Choose a difficulty level:\n'easy' or 'hard'\n"))
    number_of_turns = 0
    if difficulty == "easy":
        number_of_turns = 10
        print("You'll have 10 tries to guess the number!")
    elif difficulty == "hard":
        number_of_turns = 5
        print("You'll have 5 tries to guess the number!")

    return number_of_turns

def guessing_game():
    game_over = False
    number_to_guess = random.randint(1, 100)
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    player_turns = choose_difficulty()

    while not game_over:
        guessed_number = int(input("Try to guess the number i'm thinking (Between 1 and 100)!\n"))
        if guessed_number == number_to_guess:
            game_over = True
            print(f"You guessed the number! It was the number {number_to_guess}.\nAnd you had {player_turns} turns left!")
        else:
            player_turns -= 1
            if guessed_number > number_to_guess:
                print("Too high!")
            else:
                print("Too low!")
            print(f"You guessed the wrong number!\nAnd now you have {player_turns} turns left")
        if player_turns == 0:
            game_over = True
            print("You ran out of turns!")

guessing_game()