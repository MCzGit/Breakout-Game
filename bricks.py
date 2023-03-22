#Import the Modules
from turtle import Turtle
import random

BRICK_COLORS = ["#864000", "#D44000", "#FF7A00", "#FFEFCF",
                "#F1E3CB", "#F9B384", "#CA5116", "#581C0C",
                "#7C0A02", "#B22222", "#E25822", "#F1BC31",
                "#16A596", "#898B8A"]

weights = [1, 2, 1, 1, 3, 
           2, 1, 4, 1, 3,
           1, 1, 1, 4, 1, 
           3, 2, 2, 1, 2,
           1, 2, 1, 2, 1]

#Create a class for an individual brick, determine its shape, size, and weight.
#The weight determines the number of times the brick needs to be hit in order to disappear.
#The number 1 is the most assigned weight number in order to prevent extreme difficulty.
#To determine when the ball collides with a brick, coordinates of the four edges of the brick are needed.
#x-coordinates for left and right, y-coordinates for top and bottom.
class Brick(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1.5, stretch_len=3)
        self.color(random.choice(BRICK_COLORS))
        self.goto(x=x_cor, y=y_cor)

        self.quantity = random.choice(weights)

        #Defining borders of the brick
        self.left_wall = self.xcor() - 30
        self.right_wall = self.xcor() + 30
        self.top_wall = self.ycor() + 15
        self.bottom_wall = self.ycor() - 15


#Create a class for a list of bricks also known as an array of bricks.
#The initial x-coordinate and ending coordinate for the brick remains the same.
#For each layer or lane of brick, the y axis is the only change.
#A single lane function is called inside another function which passes its y-coordinates for lanes.
class Bricks:
    def __init__(self):
        self.y_begin = 0
        self.y_end = 240
        self.bricks = []
        self.generate_all_lanes()

    def generate_lane(self, y_cor):
        for i in range(-570, 570, 63):
            brick = Brick(i, y_cor)
            self.bricks.append(brick)
    
    def generate_all_lanes(self):
        for i in range(self.y_begin, self.y_end, 32):
            self.generate_lane(i)
        

