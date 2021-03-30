from turtle import Turtle
import random


colors = ["red","green","yellow","blue","cyan","purple","black","brown","orange","pink","grey"]

class Car(Turtle):
    def __init__(self,position):
        super().__init__("square")

        self.penup()
        self.shapesize(1,2)
        self.goto(position)
        self.color(random.choice(colors))
        self.speed = 3
        
    def move_random(self):
        self.backward(self.speed)
        
    def increase_speed(self):
        self.speed += 1