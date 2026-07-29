from turtle import Turtle

STARTING_POSITION = (0, -220)
SPEED = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.left(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(SPEED)

    def reset(self):
        self.goto(STARTING_POSITION)