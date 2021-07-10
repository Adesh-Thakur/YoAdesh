import turtle

for a in range(1200000000000):
    for cool in ["yellow","green","red"]:
        turtle.bgcolor(cool)
        turtle.pensize(100)
        turtle.speed(0)
    
    for colours in ["red","yellow","green"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)



turtle.hideturtle()
