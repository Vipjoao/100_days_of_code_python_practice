from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Scoreboard

snake = Snake()
food = Food()
score = Scoreboard()

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Keys setup
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_is_on = False

    # Detect collision with its own tail
    for segment in snake.segment_list[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False

    # Detects when the user loses to trigger GAME OVER
    if not game_is_on:
        score.game_over()

screen.exitonclick()
