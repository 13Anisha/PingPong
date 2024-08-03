from turtle import Turtle


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.add_score(position)

    def add_score(self, position):
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.color("white")
        self.write(f"{self.score}", align="center", font=("Arial", 20, "normal"))

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align="center", font=("Arial", 20, "normal"))
