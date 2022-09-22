from turtle import Turtle, Screen
import random

colors = ["medium blue", "lime", "red", "medium violet red", "dark violet", "indian red", "yellow", "cyan"]
tim = Turtle()


def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for i in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)


for _ in range(3, 11):
    draw_shape(_)
    tim.color(random.choice(colors))


screen = Screen()
screen.exitonclick()
