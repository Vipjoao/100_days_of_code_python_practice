from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0,0), (0, -20), (0, -40)]
DIRECTIONS = {
    "up": 90,
    "down": 270,
    "left": 180,
    "right": 0,
}

class Snake:
    def __init__(self):
        self.segment_list = []
        self.create_snake()
        self.head = self.segment_list[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("lime")
        new_segment.penup()
        self.segment_list.append(new_segment)
        new_segment.goto(position)

    def extend(self):
        self.add_segment(self.segment_list[-1].position())

    def move(self):
        for seg_num in range(len(self.segment_list) - 1, 0, -1):
            new_x = self.segment_list[seg_num - 1].xcor()
            new_y = self.segment_list[seg_num - 1].ycor()
            self.segment_list[seg_num].goto(new_x, new_y)
        self.segment_list[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DIRECTIONS["down"]:
            self.head.setheading(DIRECTIONS["up"])

    def down(self):
        if self.head.heading() != DIRECTIONS["up"]:
            self.head.setheading(DIRECTIONS["down"])

    def left(self):
        if self.head.heading() != DIRECTIONS["right"]:
            self.head.setheading(DIRECTIONS["left"])

    def right(self):
        if self.head.heading() != DIRECTIONS["left"]:
            self.head.setheading(DIRECTIONS["right"])
