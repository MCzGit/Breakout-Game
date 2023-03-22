#Import the Modules
from turtle import Turtle
import random
import time

FONT = ("Lucida Grande", 52, "normal")
FONT2 = ("Lucida Grande", 32, "normal")
ALIGNMENT = "center"
COLOR = "#ffffff"
LIST_OF_COLORS = ["#864000", "#D44000", "#FF7A00", "#FFEFCF",
                "#F1E3CB", "#F9B384", "#CA5116", "#581C0C",
                "#7C0A02", "#B22222", "#E25822", "#F1BC31",
                "#16A596", "#898B8A"]

#Create a class for the User Interface to display a message and alter the color of the message.
class UI(Turtle):
    def __init__(self):
        super().__init__()
        #Hide the turtle without providing a shape, as only a message to be displayed is needed.
        self.hideturtle()
        self.penup()
        #Randomly select a color from the list of colors.
        self.color(random.choice(LIST_OF_COLORS))
        self.header()

    def header(self):
        self.clear()
        self.goto(x=0, y=-150)
        self.write("Breakout 2023", align=ALIGNMENT, font=FONT)
        self.goto(x=0, y=-180)
        self.write("Press Space to PAUSE or RESUME the Game", align=ALIGNMENT, font=("Helvetica", 14, "normal"))

    def change_color(self):
        self.clear()
        self.color(random.choice(LIST_OF_COLORS))
        self.header()
    
    #When the game is paused, change the color and delay the application 
    #granting the user some time before resuming the game after pressing the spacebar again.
    def paused_status(self):
        #Whenever writing or changing the color, the previous text must be cleared.
        self.clear()
        self.change_color()
        time.sleep(0.5)
    
    def game_is_over(self, win):
        self.clear()
        if win == True:
            self.goto(x=0, y=-150)
            self.write("Congratulations! You've Cleared the Wall!", align=ALIGNMENT, font=FONT)
            
        else:
            self.goto(x=0, y=-150)
            self.write("Game Over! Try Again!", align=ALIGNMENT, font=FONT)
            
            
            


