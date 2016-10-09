# Two turtles race

import turtle              # 1.  import the modules
import random
wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('lightblue')
wn.title('Turtle Race')

lance = turtle.Turtle()    # 3.  Create two turtles
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                  # 4.  Move the turtles to their starting point
lance.up()
andy.goto(-300, 40)
lance.goto(-300, -40)

for i in range(100):
    x = random.randrange(1,10)
    andy.fd(x)
    x = random.randrange(1,10)
    lance.fd(x)


wn.exitonclick()
