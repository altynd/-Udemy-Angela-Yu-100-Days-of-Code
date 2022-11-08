#TODO 4 DONE
# add ball.py

from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.direction_x = random.choice([-1, 1])
        self.direction_y = self.direction_x
        self.shape("square")
        self.color("white")
        self.penup() #delete line turtle
        self.speed("fast")
        self.move()

    def move(self):
        """ball moving on diagonale"""
        new_position_x = self.xcor() + 1 * self.direction_x
        new_position_y = self.ycor() + 1 * self.direction_y
        self.goto(new_position_x, new_position_y)


    def reset_position(self):
        self.goto(0,0)
        self.direction_x = random.choice([-1, 1])
        self.direction_y = self.direction_x
        self.move()


