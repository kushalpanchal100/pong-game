import turtle

wn = turtle.Screen()
wn.title("pong by @kushal panchal")
wn.bgcolor("purple")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a. speed(0)
paddle_a.shape("square")
paddle_a. color("Red")
paddle_a. shapesize(stretch_wid=5, stretch_len=1)
paddle_a. penup()
paddle_a. goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b. speed(0)
paddle_b.shape("square")
paddle_b. color("Blue")
paddle_b. shapesize(stretch_wid=5, stretch_len=1)
paddle_b. penup()
paddle_b. goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(10)
ball.shape("circle")
ball.color("GREEN")
ball.penup()
ball.goto(0,0)
ball.dy = 0.3
ball.dx = -0.3

# Pen
pen_a = turtle.Turtle()
pen_a.speed(0)
pen_a.color("black")
pen_a.penup()
pen_a.hideturtle()
pen_a.goto(0,260)
pen_a.write("Player A: 0 Player B: 0", align="center", font=("Algerian",20,"normal"))

pen_b = turtle.Turtle()
pen_b.speed(0)
pen_b.color("grey")
pen_b.penup()
pen_b.hideturtle()
pen_b.goto(0,-230)
pen_b.write("MADE BY KUSHAL PANCHAl", align="center", font=("Segoe Script",18,"bold"))

pen_c = turtle.Turtle()
pen_c.speed(0)
pen_c.color("grey")
pen_c.penup()
pen_c.hideturtle()
pen_c.goto(0,-260)
pen_c.write("copyright2021 I TECHWARE .LTD", align="center", font=("courier",12,"bold"))


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 10
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 10
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 10
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 10
    paddle_b.sety(y)

# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"v")
wn.onkeypress(paddle_a_down,"c")
wn.onkeypress(paddle_b_up,"Right")
wn.onkeypress(paddle_b_down,"Left")

# main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
       ball.sety(290)
       ball.dy *=-1
    
    if ball.ycor() < -290:
       ball.sety(-290)
       ball.dy *=-1
       
    if ball.xcor() > 390:
       ball.goto(0,0)
       ball.dx *=-1
       score_a += 1
       pen_a.clear()
       pen_a.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Algerian",20,"normal"))
    
    if ball.xcor() < -390:
       ball.goto(0,0)
       ball.dx *=-1
       score_b += 1
       pen_a.clear()
       pen_a.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Algerian",20,"normal"))


    # Paddle and Ball collision
    if (ball.xcor() > 340 and ball.xcor() < 390) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
     ball.setx(360)
     ball.dx *=-1

    if (ball.xcor() < -340 and ball.xcor() > -390) and (ball.ycor() < paddle_a.ycor() +40 and ball.ycor() > paddle_a.ycor() -40):
     ball.setx(-360)
     ball.dx *=-1