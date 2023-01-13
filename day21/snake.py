import turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.length = len(self.segments)

    def create_snake(self):
        for i in range(len(START_POSITIONS)):
            self.add_segment(i)
            self.segments[i].setpos(START_POSITIONS[i])

    def add_segment(self, i):
        self.segments.append(turtle.Turtle(shape="square"))
        self.segments[i].color("white")
        self.segments[i].penup()

    def extend(self):
        self.add_segment(self.length)
        self.segments[self.length].setpos(self.segments[self.length - 1].pos())
        self.length += 1

    def move(self):
        for i in range(self.length - 1, 0, -1):
            self.segments[i].setx(self.segments[i - 1].xcor())
            self.segments[i].sety(self.segments[i - 1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)