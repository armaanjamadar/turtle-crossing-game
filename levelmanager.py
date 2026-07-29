from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class LevelManager(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-310, 200)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)