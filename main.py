from turtle import Turtle, Screen

tim_the_turtle = Turtle()
tim_the_turtle.shape("turtle")

for i in range(4):
    tim_the_turtle.forward(50)
    tim_the_turtle.penup()
    tim_the_turtle.forward(50)
    tim_the_turtle.pendown()
    tim_the_turtle.right(90)

screen = Screen()
screen.exitonclick()
