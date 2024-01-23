from turtle import Turtle

RIGHT_PADDLE_POSITION = (450, 0)
LEFT_PADDLE_POSITION = (-450, 0)


class Paddle(Turtle):
    def __init__(self, position: str):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        if position == "right":
            self.goto(RIGHT_PADDLE_POSITION)
        elif position == "left":
            self.goto(LEFT_PADDLE_POSITION)

    def up(self) -> None:
        self.goto(x=self.xcor(), y=self.ycor() + 20)

    def down(self) -> None:
        self.goto(x=self.xcor(), y=self.ycor() - 20)
