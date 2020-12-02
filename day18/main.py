from turtle import Turtle, Screen
import random
tim = Turtle()
screen = Screen()

tim.shape("arrow")
tim.color("red")

# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)
# for i in range(150):
#     tim.forward(1)
#     if i % 2 == 0:
#         tim.penup()
#         tim.forward(1)
#     else:
#         tim.pendown()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 10):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)





screen.exitonclick()