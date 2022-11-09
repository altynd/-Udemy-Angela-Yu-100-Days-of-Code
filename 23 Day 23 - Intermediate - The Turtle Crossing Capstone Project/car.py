import random
from turtle import Turtle

colors = ["yellow", "orange", "green", "blue", "black", "pink","red"]


class Car(Turtle):
    def __init__(self):
        self.positions = []
        super().__init__()
        self.shape("square")
        self.color(random.choice(colors))
        self.turtlesize(1,2)
        self.random_positions()
        self.goto(300,random.choice(self.positions))
        self.penup()
        self.clear()#??
        self.speed = random.randint(10,30)

    def random_positions(self):
        for position in range(-240,280,20):
            self.positions.append(position)

    def move(self):
        self.goto(self.xcor()-self.speed, self.ycor())
