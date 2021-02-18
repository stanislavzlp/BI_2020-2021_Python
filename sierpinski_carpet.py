import turtle


def sierpinski_carpet(level_of_depth, length):
    turtle.tracer(0)
    turtle.color('black')
    turtle.shape('turtle')
    if level_of_depth == 0:
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(length)
            turtle.left(90)
        turtle.end_fill()
    else:
        for i in range(4):
            sierpinski_carpet(level_of_depth - 1, length / 3)
            turtle.forward(length / 3)
            sierpinski_carpet(level_of_depth - 1, length / 3)
            turtle.forward(length / 3)
            turtle.forward(length / 3)
            turtle.left(90)
        turtle.update()


sierpinski_carpet(4, 400)
turtle.done()

