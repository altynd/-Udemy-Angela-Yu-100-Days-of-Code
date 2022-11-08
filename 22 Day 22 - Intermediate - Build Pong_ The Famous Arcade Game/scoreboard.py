#TODO 9 DONE
# add scoreboard.py
from turtle import Turtle

ALIGMENT = "center"
FONT = ("Courier", 50, "normal")

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """add text of scoreboard"""
        self.write(f"{self.score}",align=ALIGMENT,font=FONT)

    def increase_score(self):
        """increase score of scoreboard"""
        self.score += 1
        self.clear()
        self.update_scoreboard()
