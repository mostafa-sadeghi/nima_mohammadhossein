import turtle
import time


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_right():
    if head.direction != "left":
        head.direction = "right"

# TODO Add go_down and go_left functions


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    # TODO add functionality for moving in left and down direction


win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("blue")
win.setup(width=600, height=600)

head = turtle.Turtle()
head.speed("fastest")
head.shape('square')
head.color("black")
head.penup()
# head.goto(0, 100)
head.direction = "none"

win.listen()
win.onkey(go_up, "Up")
win.onkey(go_right, "Right")
# TODO add onkey for Down and Left

while True:
    win.update()
    move()
    time.sleep(0.1)
