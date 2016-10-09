import turtle
wn = turtle.Screen()
wn.bgcolor('lightblue')
wn.title("Squares")

lance = turtle.Turtle()

def drawSquare(t, sz=50):

    for i in range(4):
        t.forward(sz)
        t.left(90)

command = turtle.textinput("Input command", "What to draw?")
commands = command.split()
figure = commands[0]
numfigure = int(commands[1])

lance.penup()
lance.goto(-300, -300)
lance.pendown()

if figure == 'square':
    for i in range(numfigure):
        drawSquare(lance)
        lance.penup()
        lance.goto(-300 + (i+1)*100, -300 + (i+1)*100)
        lance.pendown()


wn.exitonclick()