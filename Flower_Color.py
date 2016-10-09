import turtle

window = turtle.Screen()
window.title('Second Lesson')
window.bgcolor("lightgreen")  # background color
tom = turtle.Turtle()

colors = ['#e50000', 'green', 'blue', 'yellow', 'purple', 'magenta', '#001146']
i = 0 # number of steps

for angle in range(0, 360, 15):
    tom.color(colors[i%7]) # 0, 1, 2, 3, 4, 5, 0, 1, 2, 3 ...
    tom.seth(angle)
    tom.forward(200)
    tom.left(120)
    tom.forward(200)
    tom.left(120)
    tom.forward(200)
    i+=1

window.exitonclick()  # to exit