import time
from turtle import Screen
from ball import Ball
from pad import Pad
from scoreboard import Scoreboard

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 640

#TODO 1 DONE
# add screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

wall_left_xcor = -screen.window_width()/2 + 40
wall_right_xcor = screen.window_width()/2 - 40
wall_up_ycor = screen.window_height()/2 - 30
wall_down_ycor = -screen.window_height()/2 + 40

#TODO 2 DONE
# add ball
ball = Ball()

#TODO 5 DONE
# add pads
pad_1 = Pad((wall_left_xcor+30, 0))
pad_2 = Pad((wall_right_xcor-30,0))

#TODO 8 DONE
# add scoreboards
scoreboard_1 = Scoreboard((-50, wall_up_ycor-50))
scoreboard_2 = Scoreboard((50, wall_up_ycor-50))

screen.listen()
screen.onkey(pad_1.up, "w")
screen.onkey(pad_1.down, "s")
screen.onkey(pad_2.up, "Up")
screen.onkey(pad_2.down, "Down")

game_is_on = True
while game_is_on:

    screen.update()
    # time.sleep(0.2)
    ball.move()

    #TODO 7 DONE
    # Detect collision ball with pad
    if ball.xcor() == pad_1.xcor()+20 and ball.ycor()> pad_1.ycor()-40 and ball.ycor()<pad_1.ycor()+40:
        ball.direction_x *= -1
    elif ball.xcor() == pad_2.xcor()-20 and ball.ycor()> pad_2.ycor()-40 and ball.ycor()<pad_2.ycor()+40:
        ball.direction_x *= -1


    #TODO 3 DONE
    # detect collision ball with wall_up and wall_down
    if ball.ycor() > wall_up_ycor or ball.ycor() < wall_down_ycor:
        ball.direction_y *= -1

    #TODO 4 DONE
    # detect collision ball with wall_left an wall_right
    if ball.xcor() < wall_left_xcor-40:
        scoreboard_2.increase_score()
        ball.reset_position()
    elif ball.xcor() > wall_right_xcor+40:
        scoreboard_1.increase_score()
        ball.reset_position()

screen.exitonclick()
