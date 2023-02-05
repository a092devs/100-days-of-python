import time
from turtle import Turtle
from screen_configs import right_score_position, left_score_position

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = {"right": 0, "left": 0}
        self.hideturtle()
        self.penup()
        self.inform_score()

    def inform_score(self) -> None:

        self.color("white")
        self.clear()
        self.goto(right_score_position)
        self.write(arg=self.score["right"], move=False, align="center", font=("Courier", 80, "normal"))
        self.goto(left_score_position)
        self.write(arg=self.score["left"], move=False, align="center", font=("Courier", 80, "normal"))

    def count_point(self, ball: Turtle) -> None:
        if ball.xcor() < 0:
            self.score["right"] += 1
        else:
            self.score["left"] += 1
        self.home()
        self.color("blue")
        self.write(arg="Point!", move=False, align="center", font=("Courier", 80, "normal"))
        time.sleep(0.3)
        self.clear()

    def final_score(self):
        self.home()
        self.color("red")
        self.write(arg="Game Over", move=False, align="center", font=("Courier", 80, "normal"))
        time.sleep(0.3)