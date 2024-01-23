import time
from turtle import Screen
from screen_configs import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    TOP_BORDER,
    BOTTOM_BORDER,
    RIGHT_BORDER,
    LEFT_BORDER,
)
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.colormode(255)
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
l_paddle = Paddle(position="left")
r_paddle = Paddle(position="right")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=r_paddle.up, key="Up")
screen.onkeypress(fun=r_paddle.down, key="Down")
screen.onkeypress(fun=l_paddle.up, key="w")
screen.onkeypress(fun=l_paddle.down, key="s")

game_over = False
while not game_over:
    time.sleep(0.05)
    screen.update()
    ball.fd(ball.difficulty)
    scoreboard.inform_score()

    if ball.ycor() > TOP_BORDER or ball.ycor() < BOTTOM_BORDER:
        ball.bounce()

    if (ball.distance(r_paddle) < 50) and (ball.xcor() > (r_paddle.xcor() - 20)):
        ball.hit(r_paddle)

    if (ball.distance(l_paddle) < 50) and (ball.xcor() < (l_paddle.xcor() + 20)):
        ball.hit(l_paddle)

    if ball.xcor() > RIGHT_BORDER or ball.xcor() < LEFT_BORDER:
        scoreboard.count_point(ball=ball)
        ball.point()

    if scoreboard.score["right"] == 5 or scoreboard.score["left"] == 5:
        scoreboard.final_score()
        game_over = True

screen.exitonclick()
