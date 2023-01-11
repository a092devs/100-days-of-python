import turtle as t
import random

tom = t.Turtle()

for i in range(3, 11):
    tom.color(random.random(), random.random(), random.random())
    for _ in range(i):
        tom.forward(100)
        tom.right(360/i)