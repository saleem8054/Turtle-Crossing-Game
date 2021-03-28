from turtle import Turtle
import random
import time

colors = ["red","green","yellow","blue","cyan","purple","black","brown","orange","pink","grey"]

class Car(Turtle):
    def __init__(self,position):
        super().__init__("square")
        self.speed(0)
        self.penup()
        self.shapesize(1,2)
        self.goto(position)
        self.color(random.choice(colors))
        
    def move_random(self):
        self.backward(random.randint(1,5))  