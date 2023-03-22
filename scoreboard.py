#Import the Modules
from turtle import Turtle

#Check if the HighScore.txt file exist. If not, create the file 
#and write to it the single digit of zero to be set as the high score.
#If the file does exist, check if it has any saved data.
#If it does not have any saved data, the score will be set to zero.
#If there are no errors, the highest score will be read and displayed.
try:
    score = int(open("HighScore.txt", "r").read())
except FileNotFoundError:
    score = open("HighScore.txt", "w").write(str(0))
except ValueError:
    score = 0

FONT = ("monaco", 18, 'normal')

#Create a class for the scoreboard, that defines the max number of lives, displays the score, updates the score, 
#and maintains the high score.
class Scoreboard(Turtle):
    def __init__(self, lives):
        super().__init__()
        self.color("#5D9C59")
        self.penup()
        self.hideturtle()
        self.hi_score = score
        self.goto(x=-580, y=260)
        self.lives = lives
        self.score = 0
        self.update_score()

    def update_score(self):
        #Each time the score is updated, the previous text must be cleared.
        self.clear()
        self.write(f"Score: {self.score} | Highest Score: {self.hi_score} | Lives: {self.lives}", 
                   align="left", font=FONT)
        
    def increase_score(self):
        self.score += 1
        if self.score > self.hi_score:
            self.hi_score += 1
        self.update_score()

    #Each time the user misses the ball, decrease the number of lives by 1.
    def decrease_lives(self):
        self.lives -= 1
        self.update_score()

    def reset(self):
        self.clear()
        self.score = 0
        self.update_score()
        open("HighScore.txt", "w").write(str(self.hi_score))

    


