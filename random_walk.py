import turtle
from turtle import Turtle
from turtle import Screen
import random

turtle.colormode(255)
turtle_taido = Turtle()
turtle_taido.shape('turtle')
turtle_taido.color('blue')
turtle_taido.pensize(15)
turtle_taido.speed("fastest")


def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
for i in range(200):
    turtle_taido.color(get_random_color())
    turtle_taido.forward(30)
    turtle_taido.setheading(random.choice(directions))


my_screen = Screen()
my_screen.exitonclick()
