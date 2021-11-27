def dashed_line(turtle, width, dash_width):
    turtle_x_coordinate = turtle.xcor()
    while turtle.xcor() - turtle_x_coordinate <= width:
        turtle.forward(dash_width)
        if turtle.isdown():
            turtle.penup()
        else:
            turtle.pendown()



