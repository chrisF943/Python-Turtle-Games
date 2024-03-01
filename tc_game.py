import time
from turtle import Screen, Turtle
import turtle
from player import Player
from car_manager import Carmanager
from tc_score import Tcscore

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing Game")

player = Player()
car_manager = Carmanager()
scoreboard = Tcscore()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            turtle.write("GAME OVER", align="center", font=("Courier", 24, "normal"))

    if player.is_at_finish_line():
        player.reset()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()