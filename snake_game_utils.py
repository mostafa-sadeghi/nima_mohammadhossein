from random import randint
import turtle


def make_screen():
    """
    This function is used for making a surface
    """
    win = turtle.Screen()
    win.title("Snake Game")
    win.bgcolor("blue")
    win.setup(width=600, height=600)
    return win


def make_turtle_object(turtle_shape, turtle_color):
    turtle_object = turtle.Turtle()
    turtle_object.speed("fastest")
    turtle_object.shape(turtle_shape)
    turtle_object.color(turtle_color)
    turtle_object.penup()
    return turtle_object


def move_food(food):
    food_x_position = randint(-240, 240)
    food_y_position = randint(-240, 240)
    food.goto(food_x_position, food_y_position)


def add_new_tail(snake_body):
    new_tail = make_turtle_object("square", "grey")
    snake_body.append(new_tail)


def move(head):
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


def reset(head, snake_body):

    head.goto(0, 0)
    head.direction = "none"
    for body in snake_body:
        body.ht()

    snake_body.clear()
