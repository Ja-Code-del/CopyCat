from turtle import Screen
from crosser import Crosser
from scoreboard import ScoreBoard
#scree setup
screen = Screen()
screen.colormode(255)
screen.setup(640, 480)
screen.bgcolor(33, 33, 33)

#display the crosser named pitt
screen.tracer(0)
pitt = Crosser()

board = ScoreBoard()
#scree listen to events
screen.listen()

game_is_on = True
#pitt can move

while game_is_on:
    pitt.move()
    screen.update()
#TODO : create the scenery

#TODO : car exists and can move

#TODO : collisions

screen.exitonclick()
