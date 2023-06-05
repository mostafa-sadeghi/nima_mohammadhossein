import turtle
import time
from random import randint

snake_body = []

def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def move_food():
    food_x_position = randint(-240, 240)
    food_y_position = randint(-240, 240)
    food.goto(food_x_position, food_y_position)


def add_new_tail():
    new_tail = turtle.Turtle()
    new_tail.speed("fastest")
    new_tail.shape("square")
    new_tail.color("grey")
    new_tail.penup()
    snake_body.append(new_tail)


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("blue")
win.setup(width=600, height=600)

head = turtle.Turtle()
head.speed("fastest")
head.shape('square')
head.color("black")
head.penup()
head.direction = "none"


food = turtle.Turtle()
food.shape("circle")
food.speed("fastest")
food.color("red")
food.penup()
food.shapesize(0.7, 0.7)
move_food()


win.listen()
win.onkey(go_up, "Up")
win.onkey(go_right, "Right")
win.onkey(go_down, "Down")
win.onkey(go_left, "Left")


while True:
    win.update()

    if head.distance(food) < 17:
        move_food()
        add_new_tail()
        print(snake_body)

    for i in range(len(snake_body) - 1 , 0 , -1):
        x_prev_i = snake_body[i-1].xcor()
        y_prev_i = snake_body[i-1].ycor()
        snake_body[i].goto(x_prev_i,y_prev_i)

    if len(snake_body) > 0:
        head_x_position = head.xcor()
        head_y_position = head.ycor()
        snake_body[0].goto(head_x_position, head_y_position)

    move()
    time.sleep(0.1)
