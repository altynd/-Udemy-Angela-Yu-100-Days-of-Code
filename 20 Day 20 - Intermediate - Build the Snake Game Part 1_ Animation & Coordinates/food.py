from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        coordinate_list = []
        for coordinate in range(-280, 280, 20):
            coordinate_list.append(coordinate)

        random_x = random.choice(coordinate_list)
        random_y = random.choice(coordinate_list)
        self.goto(random_x, random_y)
