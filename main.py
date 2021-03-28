from turtle import Screen
from MyTurtle import MyTurtle
from Car import Car
import random
import time

cars = []

def create_random_cars():
    for _ in range(15):
        cars.append(Car((random.randint(0,240),random.randint(-240,240))))
    
    

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
        if cars[i].xcor() < random.randint(-300,-200):
            cars[i].goto(240,random.randint(-240,240))
            
    time.sleep(0.01)


screen.exitonclick()