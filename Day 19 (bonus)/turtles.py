from colors import colors
from turtle import Turtle
import random

STARTING_X_AXIS = 320
STARTING_Y_AXIS = 75
TURTLE_OFFSET = 30

def create_dashed_lines(tur, x_axis, y_axis):
    for _ in range(2):
        tur.teleport(x_axis, y_axis)
        tur.left(180)
        for _ in range(40):
            tur.pendown()
            tur.forward(10)
            tur.penup()
            tur.forward(10)
        x_axis = x_axis * -1
        y_axis = y_axis * -1

class Turtles(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.turtles_list = []
        self.x_axis = STARTING_X_AXIS
        self.y_axis = STARTING_Y_AXIS
        self.create_track()
        self.create_turtles()

    def create_turtles(self):
        for i in range(len(colors)):
            new_turtle = Turtle(shape="turtle")
            new_turtle.color(colors[i])
            new_turtle.penup()
            new_turtle.goto(-self.x_axis, self.y_axis)
            self.y_axis -= TURTLE_OFFSET
            self.turtles_list.append(new_turtle)

    def create_track(self):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color("black", "white")
        new_turtle.penup()
        new_turtle.goto(-(self.x_axis + TURTLE_OFFSET),self.y_axis + TURTLE_OFFSET / 2)
        new_turtle.pendown()
        new_turtle.goto(self.x_axis + TURTLE_OFFSET,self.y_axis + TURTLE_OFFSET / 2)
        new_turtle.penup()
        new_turtle.left(180)
        new_turtle.goto(self.x_axis + TURTLE_OFFSET, -(self.y_axis + TURTLE_OFFSET / 2))
        new_turtle.pendown()
        new_turtle.goto(-(self.x_axis + TURTLE_OFFSET + 20), -(self.y_axis + TURTLE_OFFSET / 2))
        new_turtle.penup()
        create_dashed_lines(new_turtle, -(self.x_axis + TURTLE_OFFSET + 10), self.y_axis - (TURTLE_OFFSET / 2))
        create_dashed_lines(new_turtle, -(self.x_axis + TURTLE_OFFSET + 10), self.y_axis - (TURTLE_OFFSET * 1.5))
        new_turtle.penup()
        new_turtle.goto(-(self.x_axis + TURTLE_OFFSET + 10), 0)
        new_turtle.left(180)
        for _ in range(40):
            new_turtle.pendown()
            new_turtle.forward(10)
            new_turtle.penup()
            new_turtle.forward(10)

    def turtles_run(self):
        for tur in self.turtles_list:
            random_distance = random.randint(1, 10)
            tur.forward(random_distance)

    def check_win(self, user_bet):
        for tur in self.turtles_list:
            if tur.xcor() >= 340:
                winning_color = tur.pencolor()
                if winning_color == user_bet:
                    print(f"You won! The {winning_color} turtle is best!")
                    return False
                else:
                    print(f"You lost! The {winning_color} won!")
                    return False
        return True