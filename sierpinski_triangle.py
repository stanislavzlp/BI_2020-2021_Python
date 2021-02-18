import random
import turtle

def sierpinski_triangle(num=500):

    turtle.shape("circle")
    turtle.penup()
    x1, y1 = random.randint(-100, 200), random.randint(350, 450)
    x2, y2 = random.randint(250, 350), random.randint(-450, -50)
    x3, y3 = random.randint(-450, -350), random.randint(-450, 0)
    start_x, start_y = random.randint(-150, 150), random.randint(-150, 150)
    turtle.shape("circle")
    turtle.speed(0.1)
    turtle.shapesize(0.01, 0.01, 0.01)
    turtle.goto(start_x, start_y)
    turtle.stamp()
    turtle.goto(x1, y1)
    turtle.stamp()
    turtle.goto(x2, y2)
    turtle.stamp()
    turtle.goto(x3, y3)
    turtle.stamp()
    current_position_x, current_position_y = start_x, start_y
    for i in range(num):
        new_position = random.randint(1, 3)
        if new_position == 1:
            go_to_x = (current_position_x + x1)/2
            go_to_y = (current_position_y + y1) / 2
            turtle.goto(go_to_x, go_to_y)
            turtle.stamp()
            current_position_x, current_position_y = go_to_x, go_to_y
        elif new_position == 2:
            go_to_x = (current_position_x + x2)/2
            go_to_y = (current_position_y + y2) / 2
            turtle.goto(go_to_x, go_to_y)
            turtle.stamp()
            current_position_x, current_position_y = go_to_x, go_to_y
        elif new_position == 3:
            go_to_x = (current_position_x + x3)/2
            go_to_y = (current_position_y + y3) / 2
            turtle.goto(go_to_x, go_to_y)
            turtle.stamp()
            current_position_x, current_position_y = go_to_x, go_to_y
    turtle.done()


sierpinski_triangle(1000)


