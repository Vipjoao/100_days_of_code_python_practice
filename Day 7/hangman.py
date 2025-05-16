# Hangman Game!
import random
from hangman_words import *
from hangman_art import *

print(logo)

word_to_guess = random.choice(word_list)
print(word_to_guess)

encrypted_word = ""
for letter in word_to_guess:
    encrypted_word += "_"
print(encrypted_word)

game_over = False
correct_letters = []
lives = 0

print("Welcome to the hangman puzzle!")

while not game_over:
    print(f"You have {6-lives} lives!")
    users_guess = input("Guess a letter:\n").lower()

    display = ""
    for letter in word_to_guess:
        if len(users_guess) > 1:
            print(f"Sorry! But you can only guess one letter at a time.\nYou guessed {len(users_guess)}.")
            break
        if letter == users_guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    if users_guess not in correct_letters:
        lives += 1
    print(display)
    print(stages[lives])
    if "_" not in display:
        print(f"You guessed all the letters and found that the word was: {word_to_guess}!")
        game_over = True
    if lives == len(stages)-1:
        print(f"You guessed too many letters. Game Over!\nThe word was: {word_to_guess}!")
        game_over = True