import colorgram
from random import choice
import turtle as t

def image_color_list(image):
	colors = []
	image_colors = colorgram.extract(image, 35)

	for color in image_colors:
		color_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
		colors.append(color_tuple)

color_list = [(58, 106, 148), (224, 200, 110), (134, 84, 58), (223, 138, 62), (196, 145, 171), (142, 178, 203), (139, 82, 105), (208, 90, 69), (237, 225, 233), (188, 80, 120), (69, 105, 90), (133, 182, 135), (133, 133, 74), (64, 156, 92), (47, 156, 193), (183, 192, 201), (213, 177, 191), (19, 58, 92), (20, 68, 113), (113, 123, 149), (227, 174, 166), (172, 203, 183), (156, 206, 217), (69, 58, 47), (72, 64, 53), (111, 46, 59), (53, 70, 64), (119, 46, 39), (48, 65, 61)]

# 10x10 size -> 20 space -> 50
tim = t.Turtle()
tim.speed(0)
t.colormode(255)
tim.penup()
tim.hideturtle()

x = -200
y = -200
tim.setpos(x, y)

for row in range(10):
	tim.setpos(-200, y)
	for collum in range(10):
		tim.forward(50)
		tim.dot(20,choice(color_list))
	y += 50


screen = t.Screen()
screen.exitonclick()

# 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
