import turtle as t
import random

tom = t.Turtle()
screen = t.Screen()
t.colormode(255)

tom.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


for index in range(0, 361, 3):
    tom.color(random_color())
    tom.setheading(index)
    tom.circle(100)

screen.exitonclick()
