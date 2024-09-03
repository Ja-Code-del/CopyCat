from turtle import Screen
from crosser import Crosser
from scoreboard import ScoreBoard
from scenery import Scenery, COLORS
from cars import Cars
#scree setup
screen = Screen()
screen.colormode(255)
screen.setup(640, 480)
screen.bgcolor(0, 0, 0)

#create the scenery
scene = Scenery()

#Create the crosser named pitt
screen.tracer(0)
scene.road_maker(COLORS, 10, 32, 14, 10)
pitt = Crosser()
car = Cars()
board = ScoreBoard()


#scree listen to events
screen.listen()

game_is_on = True
#pitt can move

while game_is_on:
    pitt.move()
    screen.update()


#TODO : car exists and can move

#TODO : collisions

screen.exitonclick()
