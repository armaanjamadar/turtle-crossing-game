from car import Car
import time

END_LINE = -420

class CarManager:
    def __init__(self):
        self.last_spawn_time = time.monotonic()
        self.spawn_gap = 0.3
        self.cars = []

    def spawn_cars(self):
        if time.monotonic() - self.last_spawn_time < self.spawn_gap:
            return
        car = Car()
        self.cars.append(car)
        self.last_spawn_time = time.monotonic()

    def move_cars(self):
        for car in self.cars[:]:
            if car.xcor() < END_LINE:
                car.destroy()
                self.cars.remove(car)
            else:
                car.move()

    def increase_speed(self):
        Car.increase_speed()
        if self.spawn_gap > 0.1:
            self.spawn_gap -= 0.02