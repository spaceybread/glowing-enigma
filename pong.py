import turtle
import random

wn = turtle.Screen()
wn.title("sad and tired but at least i can type")
wn.bgcolor("black")
wn.setup(width=800, height=800)
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 360)
pen.write("Player A: 0 // Player B: 0", align="center", font=("Roboto", 24, "normal"))

paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.color("white")
paddleA.penup()
paddleA.goto(-380,0)

paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.color("white")
paddleB.penup()
paddleB.goto(375,0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = random.random() * 2 + 0.1
ball.dy = random.random() * 2 + 0.1

def paddleA_up():
    y = paddleA.ycor()
    y = y + 10
    paddleA.sety(y)

def paddleA_down():
    y = paddleA.ycor()
    y = y - 10
    paddleA.sety(y)

def paddleB_up():
    y = paddleB.ycor()
    y = y + 10
    paddleB.sety(y)

def paddleB_down():
    y = paddleB.ycor()
    y = y - 10
    paddleB.sety(y)

scA = 0
scB = 0

wn.listen()
wn.onkeypress(paddleA_up, "q")
wn.onkeypress(paddleA_down, "a")
wn.onkeypress(paddleB_up, "p")
wn.onkeypress(paddleB_down, "l")

while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 390:
        ball.sety(390)
        ball.dy = ball.dy * -1

    if ball.ycor() < -390:
        ball.sety(-390)
        ball.dy = ball.dy * -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = random.random() * 2 + 0.1
        ball.dy = random.random() * 2 + 0.1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = random.random() * 2 + 0.1
        ball.dy = random.random() * 2 + 0.1

    if (ball.ycor() < paddleA.ycor() + 50) and (ball.ycor() > paddleA.ycor() - 50) and (ball.xcor() < paddleA.xcor() + 10):
        ball.dx = ball.dx * -1
        scA = scA + 1
        pen.clear()
        pen.write("Player A: {} // Player B: {}".format(scA, scB), align="center", font=("Roboto", 24, "normal"))

    if (ball.ycor() < paddleB.ycor() + 50) and (ball.ycor() > paddleB.ycor() - 50) and (ball.xcor() > paddleB.xcor() - 10):
        ball.dx = ball.dx * -1
        scB = scB + 1
        pen.clear()
        pen.write("Player A: {} // Player B: {}".format(scA, scB), align="center", font=("Roboto", 24, "normal"))

    paddleA.goto(-380, ball.ycor())
    paddleB.goto(375, ball.ycor())
