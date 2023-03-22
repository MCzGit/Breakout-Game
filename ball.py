#Import the Modules
from turtle import Turtle

#Set the distance the ball will travel
BALL_DISTANCE = 10

#Create a class for the ball, inherit the Turtle class, & determine its shape, color, speed, and movement.
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#F6F1F1")
        self.penup()
        self.x_ball_distance = BALL_DISTANCE
        self.y_ball_distance = BALL_DISTANCE
        self.move_speed = 0.05
        self.reset()

    def move_ball(self):
        #Set the ball to move vertically and horizontally, both only 10 steps ahead.
        new_y = self.ycor() + self.y_ball_distance
        new_x = self.xcor() + self.x_ball_distance
        self.goto(x=new_x, y=new_y)

    def bounce_ball(self, x_bounce, y_bounce):
        if x_bounce:
            #Set the ball's direction to reverse horizontally
            self.x_ball_distance *= -1
            self.move_speed *= 1
            
        if y_bounce:
            #Set the ball's direction to reverse vertically
            self.y_ball_distance *= -1
            self.move_speed *= 1
            
    def reset(self):
        #The ball should return to the initial position, always moving up.
        self.goto(x=0, y=-240)
        self.move_speed = 0.05
        self.y_ball_distance = 10



