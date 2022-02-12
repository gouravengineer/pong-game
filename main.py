from turtle import Turtle,Screen
from pong import Paddle,Ball
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.tracer(0)

paddle=Paddle()
ball=Ball()
screen.listen()
screen.onkey(paddle.run_w,"w")
screen.onkey(paddle.run_s,"s")
screen.onkey(paddle.run_up,"Up")
screen.onkey(paddle.run_down,"Down")
    
is_game_on=True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    #bounce when collision with wall 
    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce_y()
    #counce when colission with paddle
    if paddle.paddle[1].xcor() > 360 and ball.distance(paddle.paddle[1]) < 30 or paddle.paddle[0].xcor() < -340 and ball.distance(paddle.paddle[0]) < 30:
        ball.bounce_x()    
    
"""li=[]
position=[(-380,0),(-380,-20),(-380,20),(-380,40)]
for i in range(4):
    tim=Turtle()
    tim.speed("fastest")
    tim.penup()
    tim.penup()
    tim.shape("square")
    tim.color("white")
    tim.goto(position[i])
    li.append(tim)

"""














screen.exitonclick()

