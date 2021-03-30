from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-250,270)
        self.write(f"Score: {self.score}",align="center",font=("Courier", 15, "bold"))
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    def lose(self):
        self.clear()
        self.goto((0,0))
        self.write(f"Game over. Total score was {self.score}",align="center",font=("Courier", 15, "bold"))