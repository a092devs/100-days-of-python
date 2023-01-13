import turtle
import random

class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.screen_width = self.getscreen().window_width()
        self.screen_height = self.getscreen().window_height()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("violet")
        self.speed("fastest")
        self.penup()
        self.respawn()

    def respawn(self):
        x_range = int((self.screen_width - 10) / 40)
        y_range = int((self.screen_height - 10) / 40)
        self.setpos(random.randint(-x_range, x_range) * 20, random.randint(-y_range, y_range) * 20)