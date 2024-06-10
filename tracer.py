# Testing file
from turtle import Turtle, Screen
import time


screen = Screen()
screen.bgcolor("green")
screen.title("Welcome in Snake Game")
screen.setup(width=600, height=600)
screen.tracer(False)

squre1 = Turtle("square")
squre1.penup()
squre1.goto(0, 0)

squre2 = Turtle("square")
squre2.penup()
squre2.goto(-20,0)
screen.update

for _ in range(80):
    squre1.forward(10)
    squre2.forward(10)
    time.sleep(1)
    screen.update()

screen.exitonclick()