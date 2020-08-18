import turtle


screen = turtle.Screen()
screen.setup(width= 800, height = 600)
screen.bgcolor("black")

# Paddle 1 
p1 = turtle.Turtle()
p1.speed(0)
p1.penup()
p1.goto(-350,-50)


p1.begin_fill()
for i in range(0,2):
	p1.color("white", "white")
	p1.forward(20)
	p1.left(90)
	p1.forward(100)
	p1.left(90)
p1.end_fill()

def p1_up():
	

# Paddle 2
# p2 = turtle.Turtle()
#p2.shape()
#p2.color("white")