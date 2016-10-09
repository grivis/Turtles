import turtle

def drawSquare(t, sz=50, sqcolor='orange'):
    """Make turtle t draw a square of with side sz."""

    t.color(sqcolor)

    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()          # Set up the window and its attributes
wn.bgcolor("lightgreen")

alex = turtle.Turtle()        # create alex
drawSquare(alex)          # Call the function to draw the square

alex.penup()
alex.goto(100,100)
alex.pendown()

drawSquare(alex,75)           # Draw another square

wn.exitonclick()