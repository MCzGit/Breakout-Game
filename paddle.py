#Import the Modules
from turtle import Turtle

#Determine the distance the paddle will move.
PAD_DISTANCE = 70

#Create a class for the paddle, inherit the Turtle class, & determine the shape, size, and color of the paddle.
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("#19A7CE")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=10)
        #Place the paddle at the lowest part of the window and in the center using the goto function.
        self.goto(x=0, y=-280)

    #Set the paddle to move left and right. 
    #Since the paddle is facing the right direction by default, it will only need to move forward and backward.
    def slide_left(self):
        self.backward(PAD_DISTANCE)

    def slide_right(self):
        self.forward(PAD_DISTANCE)

        

