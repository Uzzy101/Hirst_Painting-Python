import random
from turtle import Turtle, Screen
import turtle as t

t.colormode(255)
raphael = Turtle()
raphael.speed("fast")
raphael.shape("turtle")
raphael.color("red")

color_list = [(139, 168, 195), (206, 154, 121), (192, 140, 150), (25, 36, 55), (58, 105, 140), (145, 178, 162),
              (151, 68, 58), (137, 68, 76), (229, 212, 107), (47, 36, 41), (145, 29, 36), (28, 53, 47), (55, 108, 89),
              (228, 167, 173), (189, 99, 107), (139, 33, 28), (194, 92, 79), (49, 40, 36), (228, 173, 166),
              (20, 92, 69), (177, 189, 212), (29, 62, 107), (113, 123, 155), (172, 202, 190), (51, 149, 193),
              (166, 200, 213), (66, 66, 57), (107, 140, 129), (47, 69, 76), (178, 124, 75)]
raphael.hideturtle()

for n in range(10):
    for i in range(10):
        color = random.choice(color_list)
        raphael.dot(15, color)
        raphael.penup()
        raphael.forward(40)
    raphael.setheading(90)
    raphael.forward(40)
    raphael.setheading(180)
    raphael.forward(400)
    raphael.setheading(0)
my_screen = Screen()
my_screen.exitonclick()








