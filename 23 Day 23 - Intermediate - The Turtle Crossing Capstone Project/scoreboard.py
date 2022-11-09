
from turtle import Turtle

ALIGMENT = "center"
FONT = ("Courier", 25, "normal")

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """add text of scoreboard"""
        self.write(f"Score: {self.score}",align=ALIGMENT,font=FONT)

    def increase_score(self):
        """increase score of scoreboard"""
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("MONKIN LOSE", align=ALIGMENT, font=FONT)

