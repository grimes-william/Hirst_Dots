# import colorgram

# colors = colorgram.extract('image.jpg', 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rbg = (r, b, g)
#     rgb_colors.append(rbg)
#
# print(rgb_colors)

from turtle import Turtle, Screen
import random

rgb_colors = [(215, 102, 153), (15, 74, 19), (235, 101, 225), (49, 146, 85), (111, 213, 172), (170, 46, 80),
              (48, 20, 30), (212, 63, 85), (194, 124, 89), (27, 130, 43), (111, 64, 37), (54, 49, 117), (23, 28, 45),
              (157, 87, 62), (196, 171, 134), (141, 25, 32), (118, 162, 199), (65, 37, 27), (152, 196, 211),
              (98, 194, 112), (31, 46, 89), (84, 32, 80), (64, 115, 161), (149, 220, 212), (165, 225, 186),
              (226, 163, 174)]

screen = Screen()
screen.colormode(255)

hirst = Turtle()
hirst.hideturtle()
y_cor = 0.0

# Grid of 100 dots
for _ in range(10):
    # new line above previous
    hirst.setpos(0.0, y_cor)
    for x in range(10):
        circle_color = random.choice(rgb_colors)

        hirst.pendown()
        hirst.speed(0)
        hirst.color(random.choice(rgb_colors))
        hirst.begin_fill()
        hirst.circle(15)
        hirst.end_fill()
        hirst.penup()
        hirst.forward(50)
    y_cor += 50.0


screen.exitonclick()
