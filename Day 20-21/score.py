from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.teleport(0, 220)
        self.penup()
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Your score: {self.score}", align="center", font=("Arial", 12, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 12, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

