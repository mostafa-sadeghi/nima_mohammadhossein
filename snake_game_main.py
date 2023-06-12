
import time
from snake_game_utils import make_screen, make_turtle_object, move_food, add_new_tail, move, reset

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


win = make_screen()
win.tracer(0)

head = make_turtle_object("square", "black")
head.direction = "none"


food = make_turtle_object("circle", "red")
food.shapesize(0.7, 0.7)
move_food(food)


win.listen()
win.onkey(go_up, "Up")
win.onkey(go_right, "Right")
win.onkey(go_down, "Down")
win.onkey(go_left, "Left")


while True:
    win.update()

    if head.distance(food) < 17:
        move_food(food)
        add_new_tail(snake_body)

    for i in range(len(snake_body) - 1, 0, -1):
        x_prev_i = snake_body[i-1].xcor()
        y_prev_i = snake_body[i-1].ycor()
        snake_body[i].goto(x_prev_i, y_prev_i)

    if len(snake_body) > 0:
        head_x_position = head.xcor()
        head_y_position = head.ycor()
        snake_body[0].goto(head_x_position, head_y_position)

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        reset(head, snake_body)

    # TODO   add score and high score
    # TODO در لبه های صفحه خط کشیده شود
    # TODO برخورد مار به بدنش 


    move(head)
    time.sleep(0.2)
