import turtle

window = turtle.Screen()
window.title('Second Lesson')
window.bgcolor("lightgreen")  # background color
tom = turtle.Turtle()

colors = ['red', 'green', 'blue', 'yellow', 'purple', 'magenta']
i = 0 # number of steps

for angle in range(0, 360, 15):
    tom.begin_fill()
    tom.color(colors[i%6]) # 0, 1, 2, 3, 4, 5, 0, 1, 2, 3 ...
    tom.seth(angle)
    tom.forward(200)
    tom.left(120)
    tom.forward(200)
    tom.left(120)
    tom.forward(200)
    i += 1
    tom.end_fill()

window.exitonclick()  # to exit