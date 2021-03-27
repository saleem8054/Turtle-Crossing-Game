from turtle import Screen
from MyTurtle import MyTurtle
from Car import Car
import random

cars = []

def create_random_cars():
    for _ in range(15):
        cars.append(Car((random.randint(0,240),random.randint(-240,270))))
        print(random.randint(-270,250))
    
    

screen = Screen()
screen.setup(600,600)
screen.bgcolor("white")
screen.title("Car Crossing Game")
screen.listen()
screen.tracer(0)

myTurtle = MyTurtle()

create_random_cars()

screen.update()

screen.onkeypress(myTurtle.up, "Up")
screen.onkeypress(myTurtle.down, "Down")

screen.tracer(1)
    

while True:
    for i in range(len(cars)):
        cars[i].move_random()


screen.exitonclick()