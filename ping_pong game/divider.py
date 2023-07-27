from turtle import Turtle

class Divider(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, -300)
        self.setheading(90)
        for i in range(30):
            self.forward(10)
            self.pendown()
            self.forward(10)
            self.penup()



