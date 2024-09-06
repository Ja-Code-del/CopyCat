from turtle import Screen
from paddle import Paddle, Machine

window = Screen()
window.title("Pong")
window.setup(640, 480)
window.colormode(255)
window.bgcolor(33, 33, 33)

window.tracer(0)

player = Paddle()
machine = Machine()
window.listen()
game_is_on = True

while game_is_on:
    window.update()
    player.move()
    machine.auto_move()

window.exitonclick()
