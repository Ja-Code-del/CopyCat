from turtle import Screen
from crosser import Crosser

screen = Screen()
screen.colormode(255)
screen.screensize(640, 480)
screen.bgcolor(33, 33, 33)
screen.tracer(0)
pitt = Crosser()
screen.update()




screen.exitonclick()
