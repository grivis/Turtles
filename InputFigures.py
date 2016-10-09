import turtle
wn = turtle.Screen()
wn.bgcolor('lightblue')
wn.title('Many Figures')

lance = turtle.Turtle()

def drawSquare(t, sz=50):
    for i in range(4):
        t.forward(sz)
        t.left(90)


def drawTriangle(t, sz=50):
    for i in range(3):
        t.forward(sz)
        t.left(120)

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
elif figure == 'triangle':
    for i in range(numfigure):
        drawTriangle(lance)
        lance.penup()
        lance.goto(-300 + (i+1)*100, -300 + (i+1)*100)
        lance.pendown()


wn.exitonclick()
