from turtle import Turtle


class Table(Turtle):
    def __init__(self):
        super().__init__()
        self.make()

    def make(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.pendown()
        self.setheading(270)

        for i in range(14):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()
