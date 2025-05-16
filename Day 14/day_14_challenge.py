# Higher or lower
import random
import art
import game_data

# {
#     'name': 'Instagram',
#     'follower_count': 346,
#     'description': 'Social media platform',
#     'country': 'United States'
# },

def higher_lower():
    game_over = False
    player_score = 0
    choice_1 = random.choice(game_data.data)
    while not game_over:
        choice_2 = random.choice(game_data.data)
        if choice_1 == choice_2:
            choice_2 = random.choice(game_data.data)
        print(art.logo)
        print(f"Current score: {player_score}")
        print(f"Compare: {choice_1['name']}, a {choice_1['description']}, from {choice_1['country']}")
        print(art.vs)
        print(f"Compare: {choice_2['name']}, a {choice_2['description']}, from {choice_2['country']}")

        player_choice = input("Who has more followers? Type 'a' or 'b'\n")

        if player_choice == 'a' and choice_1['follower_count'] > choice_2['follower_count']:
            player_score += 1
            choice_1 = choice_2
        elif player_choice == 'b' and choice_1['follower_count'] < choice_2['follower_count']:
            player_score += 1
            choice_1 = choice_2
        else:
            game_over = True
            print(art.logo)
            print(f"You lost, your final score was: {player_score} ")

higher_lower()