import random
import turtle


def drunkTurtle(length=500):
    turtle.shape("turtle")
    turtle.left(90)
    turtle.speed(2)
    x, y = 0, 0
    for i in range(length):
        move = random.randint(1, 4)
        if move == 1:
            y += 10
            turtle.goto(x, y)
        elif move == 2:
            x += 10
            turtle.goto(x, y)
        elif move == 3:
            y -= 10
            turtle.goto(x, y)
        elif move == 4:
            x -= 10
            turtle.goto(x, y)
    turtle.done()


drunkTurtle()



