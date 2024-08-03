from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        x = self.xcor()
        y = self.ycor()
        y += 20
        if self.ycor() < 240:
            self.goto(x, y)

    def down(self):
        x = self.xcor()
        y = self.ycor()
        y -= 20
        if self.ycor() > -240:
            self.goto(x, y)
