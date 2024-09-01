from turtle import Turtle, Screen
import random

COLORS = [
    "LightPink",  # Rose pastel clair
    "LightSalmon",  # Saumon clair
    "LightYellow",  # Jaune clair
    "LightGreen",  # Vert clair
    "LightBlue",  # Bleu clair
    "Lavender",  # Lavande
    "Pink",  # Rose
    "PeachPuff",  # Pêche clair
    "SkyBlue",  # Bleu ciel
    "Thistle",  # Chardon
    "Honeydew",  # Miel
    "MistyRose"  # Rose brumeux
]


class Scenery(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.goto(-320, -205)

    def road_maker(self, colors, space_between_dots, numb_dot_per_line, numb_of_lines, dots_size):
        """Function to draw dots like Hirst painting : self is your turtle name.
        colors is a list of rgb colors"""
        for _ in range(numb_of_lines):
            for _ in range(numb_dot_per_line):
                self.pendown()
                self.color(random.choice(colors))
                self.forward(dots_size)
                self.penup()
                self.forward(dots_size)
            # print(self.pos())
            self.penup()
            self.left(90)
            self.forward(3 * dots_size)
            self.right(90)
            self.backward((dots_size * numb_dot_per_line) + (space_between_dots * numb_dot_per_line))
