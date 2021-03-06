from turtle import Turtle
class MyTurtle(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.color("Green")
        self.penup()
        self.setheading(90)
        self.goto(0,-270)
        
    def reset_position(self):
        self.goto((0,-270))
        
    def up(self):
        current_y = self.ycor()
        new_y = current_y + 10
        self.sety(new_y)
       
    def down(self):
        current_y = self.ycor()
        new_y = current_y - 10
        self.sety(new_y)
        