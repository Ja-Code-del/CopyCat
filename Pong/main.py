from turtle import Screen
from paddle import Paddle, Machine
from ball import Ball


window = Screen()
window.title("Pong")
window.setup(640, 480)
window.colormode(255)
window.bgcolor(33, 33, 33)

window.tracer(0)
#initialize the objects
player = Paddle()
machine = Machine()
ball = Ball()
#the screen is now listening
window.listen()
#the variable to check if the game is running
game_is_on = True

while game_is_on:
    #Try the collide_with method
    window.update()
    player.move()
    machine.auto_move()
    ball.move()
    player.collide_with(ball)
    machine.collide_with(ball)


window.exitonclick()
