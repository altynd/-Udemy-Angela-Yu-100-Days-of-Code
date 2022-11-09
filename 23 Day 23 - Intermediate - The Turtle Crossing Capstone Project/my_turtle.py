from turtle import Turtle

class MyTurtle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("turtle")
        self.penup()
        self.goto(position)
        self.setheading(90)

    def move(self):
        self.goto(self.xcor(), self.ycor()+20)

    def restart(self):
        self.goto(self.position)

