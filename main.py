import random

import colorgram
import colorgram as c
import turtle as t


rgb_colors = []
colors = colorgram.extract("image.jpg",10)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

tim = t.Turtle()
t.colormode(255)
tim.color("white")

tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
tim.speed(0)

for dot in range(1,number_of_dots + 1):
    tim.dot(20,random.choice(rgb_colors))
    tim.forward(50)

    if dot % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)













screen = t.Screen()
t.exitonclick()