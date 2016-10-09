import turtle

window = turtle.Screen()
window.title('First Lesson')
window.bgcolor("lightgreen")  # background color
tom = turtle.Turtle()

for angle in range(0, 360, 15):
    tom.seth(angle)
    tom.forward(200)
    tom.left(120)
    tom.forward(200)
    tom.left(120)
    tom.forward(200)

window.exitonclick()  # to exit