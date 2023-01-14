from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color(65, 255, 0)
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.setheading(50)
        self.difficulty = 10

    def bounce(self):
        new_angle = self.heading() * -1
        self.setheading(new_angle)

    def hit(self, against: Turtle) -> None:
        new_angle = against.towards(self) * -1
        self.setheading(new_angle)
        self.difficulty += 1

    def point(self) -> None:
        self.difficulty = 10
        self.goto(0, 0)
        self.setheading(self.heading() + 180)