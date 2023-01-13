import turtle
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard

GAME_SPEED = 8
WIDTH = 800
HEIGHT = 600

wait_time = (11 - GAME_SPEED) / 30
x_range = WIDTH // 2 - 10
y_range = HEIGHT // 2 - 10

screen = turtle.Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Finished Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_over = False
while not game_is_over:
    screen.update()
    time.sleep(wait_time)
    snake.move()

    if snake.head.distance(food) < 10:
        scoreboard.add_one()
        snake.extend()
        food.respawn()

    if snake.head.xcor() < -x_range or snake.head.xcor() > x_range \
            or snake.head.ycor() < -y_range or snake.head.ycor() > y_range:
        game_is_over = True

    for i in range(1, snake.length):
        if snake.head.distance(snake.segments[i]) < 10:
            game_is_over = True

scoreboard.game_over()

screen.exitonclick()