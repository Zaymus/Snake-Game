import turtle
import time
import random

delay = 0.06
speed = 20
score = 0
high_score = 0

#screen setup
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("green")
window.setup(width = 900, height = 900, startx = None, starty = None)
window.tracer(0)#turns off screen updates

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

#Snake body
body = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 410)
pen.write("Score: 0             High Score: 0", align= "center", font=("Courier", 24, "normal"))
# Functions
def reset():
    time.sleep(1)
    score = 0
    delay = 0.06
    head.goto(0, 0)
    head.direction = "stop"

    for i in body:
        i.goto(1000, 1000)

    body.clear()
    food.goto(random.randint(-440, 440), random.randint(-440, 440))

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + speed)

    if head.direction == "down":
        head.sety(head.ycor() - speed)

    if head.direction == "left":
        head.setx(head.xcor() - speed)

    if head.direction == "right":
        head.setx(head.xcor() + speed)

# Keyboard bindings
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")

#main game loop
while True:
    window.update()

    #Check for border collisions
    if head.xcor() > 440 or head.xcor() < -440 or head.ycor() > 440 or head.ycor() < -440:
        reset()

    #Food collision detection
    if head.distance(food) < speed:
        x = random.randint(-440, 440)
        y = random.randint(-440, 440)
        food.goto(x, y)

        #add a body segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green", "black")
        new_segment.penup()
        body.append(new_segment)

        #increase score
        score += 10

        #shorten delay
        delay -= 0.001

        if score > high_score:
            high_score = score

    #Move the end segments fairts in reverse order
    for i in range(len(body) - 1, 0, -1):
        body[i].goto(body[i - 1].xcor(), body[i - 1].ycor())
    
    #Move segment 0 to head

    if(len(body) > 0):
        body[0].goto(head.xcor(), head.ycor())

    move()

    #Check for body collisions
    for i in body:
        if(i.distance(head) < speed):
            reset

    pen.clear()
    pen.write("Score: {}             High Score: {}".format(score, high_score), align= "center", font=("Courier", 24, "normal"))
    time.sleep(delay)
window.mainloop()