from colors import colors
from turtle import Screen
from turtles import Turtles

screen = Screen()
t = Turtles()

user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race?\n"
                                                "Red, Orange, Yellow, Green, Blue or Purple").lower()
def race():
    is_race_on = False
    if user_bet:
        is_race_on = True
    while is_race_on:
        t.turtles_run()
        if not t.check_win(user_bet):
            is_race_on = False

if user_bet in colors:
    race()
else:
    print("That's not a valid color!")
    screen.bye()