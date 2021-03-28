from turtle import Screen
from MyTurtle import MyTurtle
from Car import Car
import random
import time

cars = []

def create_random_cars():
    for _ in range(10):
        cars.append(Car((random.randint(-250,250),random.randint(-240,240))))
    for _ in range(10):
        cars.append(Car((300,random.randint(-240,240))))
    
    

screen = Screen()
screen.setup(600,600)
screen.bgcolor("white")
screen.title("Car Crossing Game")
screen.listen()
screen.tracer(0)

myTurtle = MyTurtle()

create_random_cars()

#screen.update()

screen.onkeypress(myTurtle.up, "Up")
screen.onkeypress(myTurtle.down, "Down")

#screen.tracer(1)
    

while True:
    screen.update()
    for i in range(len(cars)):
        cars[i].move_random()
    
    for i in range(len(cars)):
        if cars[i].xcor() < -300:
            cars[i].goto(300,random.randint(-240,240))
            
    time.sleep(0.01)


screen.exitonclick()