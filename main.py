import time
from turtle import Screen
from player import Player
from levelmanager import LevelManager
from carmanager import CarManager

COLLISION_DISTANCE = 25
FINISH_LINE = 230
SLEEP_TIME = 0.05

screen = Screen()
screen.setup(width=800, height=500)
screen.title("Turtle Crossing Game")
screen.tracer(0)
screen.listen()

player = Player()
level_manager = LevelManager()
car_manager = CarManager()

screen.onkey(player.move, "w")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(SLEEP_TIME)
    car_manager.spawn_cars()
    car_manager.move_cars()

    # Detect collision with traffic
    for car in car_manager.cars:
        if player.distance(car) < COLLISION_DISTANCE:
            game_is_on = False
            level_manager.game_over()

    # Increase level when player reaches the end
    if player.ycor() > FINISH_LINE:
        level_manager.increase_level()
        car_manager.increase_speed()
        player.reset()


screen.mainloop()
