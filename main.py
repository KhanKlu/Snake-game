from turtle import Turtle, Screen
import time
import random

screen = Screen()
screen.bgcolor("green")
screen.title("Welcome in Snake Game")
screen.setup(width=600, height=600)
screen.tracer(False)

# Premenné
score = 0
highest_score = 0

# Snake head
head = Turtle("square")
head.color("black")
head.speed(0)
head.penup()
head.goto(0, 0)
head.direction = "stop"

score_sign = Turtle("square")
score_sign.speed(0)
score_sign.color("white")
score_sign.penup()
score_sign.hideturtle()
score_sign.goto(0,265)
score_sign.write(f"Skóre: {score} Najväčšie skóre: {highest_score}" ,align="center", font=("Arial", 18))
# functions

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_left():
    if head.direction != "right":
        head.direction = "left"

def move_right():
    if head.direction != "left":
        head.direction = "right"


# Kliklnutie na klávesi
screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

apple = Turtle("circle")
apple.color("red")
apple.penup()
apple.goto(100, 100)

body_parts = []

# main cycle
while True:
    screen.update()

    # Control of colition with display border
    if head.xcor() > 290 or head.xcor() < - 290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(2)
        head.goto(0, 0)
        head.direction = "stop"
        
        # Hiding part of body
        for one_body_part in body_parts:
            one_body_part.goto(1500,1500)

        # Clearing Body parts
        body_parts.clear()
        score = 0
        score_sign.clear()    
        score_sign.write(f"Skóre: {score} Najväčšie skóre: {highest_score}" ,align="center", font=("Arial", 18))
     
    
    # apple

    if head.distance(apple) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        apple.goto(x,y)
        score += 10

        if score > highest_score:
            highest_score = score

        score_sign.clear()    
        score_sign.write(f"Skóre: {score} Najväčšie skóre: {highest_score}" ,align="center", font=("Arial", 18))

        # pridanie části tela
        new_body_part = Turtle("square")
        new_body_part.speed(0)
        new_body_part.color("grey")
        new_body_part.penup()
        body_parts.append(new_body_part)

    for index in range(len(body_parts) - 1, 0, -1):
       x = body_parts[index - 1].xcor()
       y = body_parts[index - 1].ycor()
       body_parts[index].goto(x, y)


    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x,y)
    move()

    # head colide with body

    for one_body_part in body_parts:
        if one_body_part.distance(head) < 20:
            time.sleep(2)
            head.goto(0, 0)
            head.direction = "stop"
            
                # Hiding part of body
            for one_body_part in body_parts:
                one_body_part.goto(1500,1500)

            # Clearing Body parts
            body_parts.clear()
            score = 0
    time.sleep(0.1)
    


screen.exitonclick()