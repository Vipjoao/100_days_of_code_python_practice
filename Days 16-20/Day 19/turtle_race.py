import turtle as t
import random

screen = t.Screen()
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race?\n"
                                                "Red, Orange, Yellow, Green, Blue or Purple").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

def race(turtle_colors):
    is_race_on = False
    tutle_list = []
    x_axis = 320
    y_axis = 75
    for i in range(len(turtle_colors)):
        new_turtle = t.Turtle()
        new_turtle.shape("turtle")
        new_turtle.color(turtle_colors[i])
        new_turtle.penup()
        new_turtle.goto(-x_axis, y_axis)
        y_axis -= 30
        tutle_list.append(new_turtle)

    if user_bet:
        is_race_on = True

    while is_race_on:
        for tur in tutle_list:
            random_distance = random.randint(0, 10)
            tur.forward(random_distance)
            if tur.xcor() >= 340:
                is_race_on = False
                winning_color = tur.pencolor()
                if winning_color == user_bet:
                    print(f"You won! The {winning_color} turtle is best!")
                else:
                    print(f"You lost! The {winning_color} won!")

if user_bet in colors:
    race(colors)
else:
    print("That's not a valid color!")
    screen.bye()