from ScoreBoard import ScoreBoard
from turtle import Screen
from MyTurtle import MyTurtle
from Car import Car
import random
import time

cars = []

def create_random_cars():
    for _ in range(10):
        cars.append(Car((random.randint(-250,250),random.randint(-240,240))))
    for _ in range(1):
        cars.append(Car((300,random.randint(-240,240))))
        #cars.append(Car((300,-245)))

    

screen = Screen()
screen.setup(600,600)
screen.bgcolor("white")
screen.title("Car Crossing Game")
screen.listen()
screen.tracer(0)

myTurtle = MyTurtle()
scoreBoard = ScoreBoard()

create_random_cars()

#screen.update()

screen.onkeypress(myTurtle.up, "Up")
screen.onkeypress(myTurtle.down, "Down")

#screen.tracer(1)

game_is_on = True    

while game_is_on:
    screen.update()
    for i in range(len(cars)):
        cars[i].move_random()
        
        #Move the cars back to initial position if they cross the screen left end.
        if cars[i].xcor() < -300:
            cars[i].goto(300,random.randint(-240,240))   
               
        #check if the turtle has collided with the cars
        if (cars[i].xcor() >= -40 and myTurtle.distance(cars[i]) <= 20)  or (cars[i].xcor() <= 40 and myTurtle.distance(cars[i]) <= 20):
                print("Game over")
                scoreBoard.lose()
                game_is_on = False
                
    # check if the turtle has crossed all the cars
    if myTurtle.ycor() > 260 :
        scoreBoard.increase_score();
        myTurtle.reset_position()
        
        for i in range(len(cars)):
            cars[i].increase_speed()
                
    time.sleep(0.01)


screen.exitonclick()