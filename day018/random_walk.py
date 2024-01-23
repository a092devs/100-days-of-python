from turtle import Turtle, Screen
import random

tom = Turtle()
screen = Screen()

choice = [0, 90, 180, 270]

tom.pensize(10)
tom.speed("fastest")


def moveRandom(turtle):
    turtle.forward(-20)
    turtle.setheading(random.choice(choice))


for _ in range(1000):
    tom.pencolor(random.random(), random.random(), random.random())
    moveRandom(tom)

screen.exitonclick()
