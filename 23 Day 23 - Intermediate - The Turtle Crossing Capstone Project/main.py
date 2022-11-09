import random
import time
from turtle import Screen
from my_turtle import MyTurtle
from scoreboard import Scoreboard
from car import Car

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

#add screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("white")
screen.title("Monkin Turtle")
screen.tracer(0)

wall_down_ycor = -screen.window_height()/2
wall_up_ycor = screen.window_height()/2
wall_left_xcor = screen.window_width()/2
wall_right_xcor = screen.window_width()/2

#adding elements on main screen
game_turtle = MyTurtle((0, wall_down_ycor+20))
scoreboard = Scoreboard((100,260))

screen.listen()
screen.onkey(game_turtle.move,"Up")

cars = []
speed = 0.1
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(speed)

    if game_turtle.ycor() > wall_up_ycor-20:
        print("Win")
        game_turtle.restart()
        scoreboard.increase_score()
        speed = speed*0.9


    #car appends in 1/chance times
    chanse = 5
    i = random.randint(0,chanse)
    if i == 0:
        car = Car()
        cars.append(car)
    for car in cars:
        car.move()
        if car.distance(game_turtle) < 20:
            print("MONKIN LOSE")
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()