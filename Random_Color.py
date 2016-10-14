import turtle
import random


def circle(turtle):
    for i in range(30):
        turtle.forward(10)
        turtle.left(25)


def spiral(turtle):
    # small loop
    for i in range(100):
        turtle.forward(10)
        turtle.left(i)


def random_color(my_turtle):
    r = random.random()
    g = random.random()
    b = random.random()
    my_turtle.color(r, g, b)


def random_spirals(turtle):
    r = random.randint(1, 10)
    if r < 5:
        # small loop
        for i in range(100):
            turtle.forward(10)
            turtle.left(i)
    else:
        # big loop
        for i in range(50):
            turtle.forward(i)
            turtle.left(15)


def make_spirals(my_turtle):
    my_turtle.forward(10)
    for i in range(13):
        size = random.randint(1, 10)
        random_color(my_turtle)
        my_turtle.pensize(size)
        random_spirals(alex)


def make_flower(t, func):
    # Makes a flower by drawing circles
    loops = 7
    for i in range(loops):
        random_color(t)
        t.home()
        t.left(360/loops * i)
        t.forward(15)
        func(t)


## Set up our turtle
alex = turtle.Turtle()
alex.shape('turtle')
alex.speed(0)
alex.hideturtle()

# ## Make a starter circle
# circle(alex)
# alex.forward(10)

## Make some random spirals
#make_spirals(alex)

# ## Make a flower
make_flower(alex, spiral)
# make_flower(alex, circle)

alex.showturtle()
alex.home()
#print('Thanks for watching!')
alex.goto(-200, -200)
alex.write('Thanks for watching!', font = ("Arial", 16, "bold") )
turtle.exitonclick()
