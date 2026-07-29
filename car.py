import random
from turtle import Turtle

COLORS = ["purple", "red", "blue", "green", "yellow", "orange", "grey"]

class Car(Turtle):

    speed = 10

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(420, random.randint(-180, 180))

    def move(self):
        self.forward(self.speed)

    def destroy(self):
        self.hideturtle()
        self.clear()

    @classmethod
    def increase_speed(cls):
        cls.speed += 2