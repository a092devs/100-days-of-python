import turtle

FONT = ("Arial", 20, "normal")

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("silver")
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.setpos(0, int(self.getscreen().window_height() / 2 - 30))
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def add_one(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER", align="center", font=FONT)