from turtle import Turtle, Screen

screen = Screen()
PLAYER_INITIAL_COR = (280, 20)
MACHINE_INITIAL_COR = (-280, 20)
MOVE_DISTANCE = 20
MACHINE_MOVE_DISTANCE = MOVE_DISTANCE / 4
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

    def check_collision_with(self, ball):
        if self.distance(ball) < 20:
            return True
        else:
            return False

    def collide_with(self, b):
        if self.check_collision_with(ball=b):
            b.setheading(b.angle + 75)
            b.angle = self.heading() + 45


class Machine(Paddle):
    def __init__(self):
        super().__init__()
        self.goto(MACHINE_INITIAL_COR)

    def auto_move(self):

        if self.ycor() > 200:
            self.setheading(DOWN)
            self.forward(MACHINE_MOVE_DISTANCE)
            getting_down = True
        elif self.ycor() < -180:
            self.setheading(UP)
            self.forward(MACHINE_MOVE_DISTANCE)
            getting_up = True
        else:
            self.forward(MACHINE_MOVE_DISTANCE)

    def collide_with(self, b):
        if self.check_collision_with(ball=b):
            b.setheading(b.angle + 75)
            b.angle = self.heading() + 225
