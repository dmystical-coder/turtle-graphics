import turtle
from turtle import Turtle
from turtle import Screen
import random

turtle.colormode(255)
turtle_taido = Turtle()
turtle_taido.speed("fastest")


def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_circle(gap_size):
    for i in range(int(360/gap_size)):
        turtle_taido.color(get_random_color())
        turtle_taido.circle(100)
        turtle_taido.setheading(turtle_taido.heading() + gap_size)


draw_circle(gap_size=5)


my_screen = Screen()
my_screen.exitonclick()
