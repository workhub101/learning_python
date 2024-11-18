import turtle
side1=int(input("enter the number of sides in your shape"))
my_turtle= turtle.Turtle()
my_turtle.screen.bgcolor("aqua")
my_turtle.color("red")
my_turtle.shape(("turtle"))
my_turtle.fillcolor("red")
my_turtle.begin_fill()
angle1=360/side1
for i in range(side1):
    my_turtle.forward(150)
    my_turtle.left(angle1)
my_turtle.end_fill()


turtle.done()
