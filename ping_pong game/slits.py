from turtle import Turtle

class Slits(Turtle):
    def __init__(self, coo):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.penup()
        self.goto(coo)

    def up(self):
        self.forward(40)

    def down(self):
        self.back(40)
