from turtle import Turtle,Screen

POSITION=[(-380,0),(380,0)]

class Paddle():
    def __init__(self):
        self.create_paddle()
        left_paddle=self.paddle[0]
        right_paddle=self.paddle[1]
    def create_paddle(self):
        self.paddle=[]
        for i in range(2):
            tim=Turtle()
            tim.penup()
            tim.shape("square")
            tim.shapesize(5,1)
            tim.speed("fastest")
            tim.color("white")
            tim.setposition(POSITION[i])
            self.paddle.append(tim)
    def run_w(self):
        left_paddle=self.paddle[0]
        self.paddle_run_up(left_paddle)

    def run_up(self):
        right_paddle=self.paddle[1]
        self.paddle_run_up(right_paddle)
    
    def paddle_run_up(self,left_paddle):
        x=left_paddle.xcor()
        y=left_paddle.ycor()
        if y+20<260:
            left_paddle.goto(x,y+20)
    def run_s(self):
        left_paddle=self.paddle[0]
        self.paddle_run_down(left_paddle)
        
    def run_down(self):
        right_paddle=self.paddle[1]
        self.paddle_run_down(right_paddle)
    def paddle_run_down(self,left_paddle):
        x=left_paddle.xcor()
        y=left_paddle.ycor()
        if y-20>-260:
            left_paddle.speed("fastest")
            left_paddle.goto(x,y-20)

    

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move=10
        self.y_move=10
    def move(self):
        x=self.xcor()+self.x_move
        y=self.ycor()+self.y_move
        self.goto(x,y)
    def bounce_y(self):
        self.y_move *=-1
    def bounce_x(self):
        self.x_move*=-1


