#Import the Modules
import turtle
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import Scoreboard
from user_interface import UI  
import time

#Create screen for program and provide its size, color, and title.
screen = turtle.Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("#000000")
screen.title("Breakout 2023")
screen.tracer(0)

ui = UI()
ui.header()

score = Scoreboard(lives=5)
paddle = Paddle()
ball = Ball()
bricks = Bricks()

game_is_paused = False
game_is_on = True
play_again = False

def pause_game():
    global game_is_paused
    if game_is_paused:
        game_is_paused = False
    else:
        game_is_paused = True


#Allow the application to react to key presses by using the listen() function.
screen.listen()
#Determine the keys which will be listened to using the onkey() function.
screen.onkey(paddle.slide_left, "Left")
screen.onkey(paddle.slide_right, "Right")
screen.onkey(pause_game, "space")


#Create function to determine the ball's collision with the walls.
def detect_wall_collision():
    global ball, score, game_is_on, ui

    #Detect collision with the left and right walls.
    if ball.xcor() < -580 or ball.xcor() > 570:
        ball.bounce_ball(x_bounce=True, y_bounce=False)
        return
    
    #Detect collision with the top wall.
    if ball.ycor() > 270:
        ball.bounce_ball(x_bounce=False, y_bounce=True)
        return
    
    #Detect collision with the bottom wall.
    #This indicates that the user missed the ball and has lost the game, thus the game will be reset.
    if ball.ycor() < -280:
        ball.reset()
        #Decrease the number of lives whenever the ball touches the bottom wall.
        score.decrease_lives()
        #When the number of lives is equal to zero, display the game is over and end the while loop.
        if score.lives == 0:
            score.reset()
            game_is_on = False
            ui.game_is_over(win=False)
            return
        ui.change_color()
        return
    

#Create a function to determine the ball's collision with the paddle.
def detect_paddle_collision():
    global ball, paddle

    #Log the ball and paddle's x-axis coordinates.
    paddle_x = paddle.xcor()
    ball_x = ball.xcor()

    #Determine if the ball's distance (from its center) from the paddle (from its center) is less than the width of the paddle 
    #and the ball is below a certain coordinate to detect their collision.
    if ball.distance(paddle) < 110 and ball.ycor() < -250:
        
        #If the paddle is on the right of the screen:
        if paddle_x > 0:
            if ball_x > paddle_x:
                #If the ball hits the paddle's left side, it should go back to the left.
                ball.bounce_ball(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce_ball(x_bounce=False, y_bounce=True)
                return
            
        #If the paddle is on the left of the screen:
        elif paddle_x < 0:
            if ball_x < paddle_x:
                #If the ball hits the paddle's right side, it should go back to the right.
                ball.bounce_ball(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce_ball(x_bounce=False, y_bounce=True)
                return
        
        #Else, Paddle is in the center horizontally.
        else:
            if ball_x > paddle_x:
                ball.bounce_ball(x_bounce=True, y_bounce=True)
                return
            elif ball_x < paddle_x:
                ball.bounce_ball(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce_ball(x_bounce=False, y_bounce=True)
                return
            

#Create a function to determine the ball'ss collision with the bricks.
def detect_bricks_collision():
    global ball, score, bricks

    #Using the distance() function, determine if the distance between the ball and the brick are within touching range.
    #When a collision between the ball and brick is confirmed, reduce the quantity of the brick, which becomes equal to zero.
    #The brick is then moved from any visibile range, and removed from the list.
    for brick in bricks.bricks:
        if ball.distance(brick) < 40:
            #Whenever the ball strikes a brick, increase the score.
            score.increase_score()
            brick.quantity -= 1
            if brick.quantity == 0:
                brick.clear()
                brick.goto(3000, 3000)
                bricks.bricks.remove(brick)

    #Once it is determined whether the ball and brick have touched or not, confirm the coordinates of the brick 
    #and make the ball bounce accordingly.
    #If the ball collides with a brick sideways, the ball's direction changes horizontally, other vertically.

            #Determine if the collision is from the left.
            if ball.xcor() < brick.left_wall:
                ball.bounce_ball(x_bounce=True, y_bounce=False)
            #Determine if the collision is from the right.
            elif ball.xcor() > brick.right_wall:
                ball.bounce_ball(x_bounce=True, y_bounce=False)
            #Determine if the collision is from the bottom.
            elif ball.ycor() < brick.bottom_wall:
                ball.bounce_ball(x_bounce=False, y_bounce=True)
            #Determine if the collision is from the top.
            elif ball.ycor() > brick.top_wall:
                ball.bounce_ball(x_bounce=False, y_bounce=True)


#Create an infinite loop with the initial step being updating the screen, followed by a delay, and initializing ball movement.
def main():
    while game_is_on:

        if not game_is_paused:

            screen.update()
            time.sleep(ball.move_speed)
            ball.move_ball()

            #Detect the ball's Collision with walls.
            detect_wall_collision()

            #Detect the ball's Collision with the paddle.
            detect_paddle_collision()

            #Detect the ball's Collision with a brick.
            detect_bricks_collision()

            #Detect the user's win.
            if len(bricks.bricks) == 0:
                ui.game_is_over(win=True)
                break

        else:
            ui.paused_status()

main()

turtle.mainloop()
