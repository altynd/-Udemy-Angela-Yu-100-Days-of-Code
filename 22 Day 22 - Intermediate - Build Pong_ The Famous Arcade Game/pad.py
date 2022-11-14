# TODO 6 DONE
#add pad.py

from turtle import Turtle


class Pad(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.turtlesize(15,1)
        self.goto(position)
        self.penup()
        self.clear()


    def up(self):
        self.goto(self.xcor(), self.ycor()+40)


    def down(self):
        self.goto(self.xcor(), self.ycor()-40)

