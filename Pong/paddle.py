from turtle import Turtle, Screen

screen = Screen()
PLAYER_INITIAL_COR = (280, 20)
MACHINE_INITIAL_COR = (-280, 20)
MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("gray")
        self.goto(PLAYER_INITIAL_COR)
        self.setheading(UP)

    def move(self):
        screen.onkeypress(self.go_up, "Up")
        screen.onkeypress(self.go_down, "Down")

    # IF THE PADDLE IS GOING UP IT'S NOT ALLOWED TO GO DOWN
    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        self.backward(MOVE_DISTANCE)


class Machine(Paddle):
    def __init__(self):
        super().__init__()
        self.goto(MACHINE_INITIAL_COR)

    def auto_move(self):

        if self.ycor() > 200:
            self.setheading(DOWN)
            self.forward(MOVE_DISTANCE / 4)
            getting_down = True
        elif self.ycor() < -180:
            self.setheading(UP)
            self.forward(MOVE_DISTANCE / 4)
            getting_up = True
        else:
            self.forward(MOVE_DISTANCE / 4)
