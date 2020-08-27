import turtle
import time
import random

# Screen
screen = turtle.Screen()
screen.setup(width= 850, height = 650)
screen.bgcolor("black")

# Border
bd = turtle.Turtle()
bd.hideturtle()
bd.shape("turtle")
bd.color("white", "white")
bd.speed(10)
bd.pensize(5)
bd.penup()
bd.goto(-400,-300)
bd.pendown()
for i in range(0,2):
	randcolor = random.choice(["red","blue","green"])
	bd.color(randcolor)
	bd.forward(800)
	bd.left(90)
	randcolor = random.choice(["yellow","pink","purple"])
	bd.color(randcolor)
	bd.forward(600)
	bd.left(90)

# Intro Text
text = turtle.Turtle()
text.color("white")
text.penup()
text.goto(0,0)
text.hideturtle()
text.write("NameNotDefined Presents...",move=False, align="center", font=("Papyrus", 16, "normal"))
time.sleep(1)
text.clear()
text.write("Pong",move=False, align="center", font=("Papyrus", 24, "normal"))
time.sleep(1)
text.clear()


# Paddle 1 
p1 = turtle.Turtle()
p1.speed(0)
p1.penup()
p1.goto(-350,-50)
p1.hideturtle()

# Paddle 1 Shape 
p1.begin_fill()
for i in range(0,2):
	p1.color("white", "white")
	p1.forward(20)
	p1.left(90)
	p1.forward(100)
	p1.left(90)
p1.end_fill()

# Paddle 2
p2 = turtle.Turtle()
p2.speed(0)
p2.penup()
p2.goto(325,-50)
p2.hideturtle()

# Paddle 2 Shape 
p2.begin_fill()
for i in range(0,2):
	p2.color("white", "white")
	p2.forward(20)
	p2.left(90)
	p2.forward(100)
	p2.left(90)
p2.end_fill()

# Paddle Movement 
def paddle_move(pen, direction,xcoordinate):
	y = pen.ycor()
	y += direction

	pen.sety(y)
	pen.setx(xcoordinate)
	pen.clear()

	pen.begin_fill()
	for i in range(0,2):
		pen.color("white", "white")
		pen.forward(20)
		pen.left(90)
		pen.forward(100)
		pen.left(90)
	pen.end_fill()

# Paddle 1
def p1_up():
	paddle_move(p1, 35, -350)


def p1_down():
	paddle_move(p1, -35, -350)

# Paddle 2
def p2_up():
	paddle_move(p2, 35, 325)

def p2_down():
	paddle_move(p2, -35, 325)

# Key Binding - Paddle 1
screen.onkey(p1_up, "w")
screen.onkey(p1_down, "s")
screen.listen()

# Key Binding - Paddle 2
screen.onkey(p2_up, "Up")
screen.onkey(p2_down, "Down")


# Player names

p1_name = input("Who is player 1? ")
print("\nHello! You will be playing with the w and s keys!\n\n")
p2_name = input("Who is player 2? ")
print("\nHello! You will be playing with the up and down keys!\n")
time.sleep(2)
# Play by Play Comments 

p1_comments_list = ["You're killing it, ", "Nice Shot, ", "Better luck next time, ", "Good one, ","That one was killer, "]

p2_comments_list = ["You're on a roll, ","Your opponent better watch their back, ", "You're killing it once again, ", "Is it talent or skill? You've got both, ", "You're destroying them, "]

# Ball Creation

ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()

# Score Update Definition
def score_update():
    text.clear()
    text.penup()

    # Score Text - Player 1
    text.goto(-100, 200)
    text.hideturtle()
    text.write(p1_score, False, "center",("Verdana", 30, "normal"))

    # Score Text - Player 2
    text.goto(100, 200)
    text.write(p2_score, False, "center",("Verdana", 30, "normal"))


def game():

	global p1_score
	global p2_score
	p1_score = 0 
	p2_score = 0 

	score_update()
    
	ydir = 1 # random.choice([1,2])
	xdir = 1 # random.choice([1,2])

	# Game continue for 3 rounds
	while p1_score != 3 and p2_score != 3: 

		# Ball Movement

		x = ball.xcor() - 4*xdir
		y = ball.ycor() - 3*ydir
		# print(ball.xcor())
		# print(ball.ycor())
		ball.setx(x)
		ball.sety(y)

		# Ball Boundaries
		if ball.ycor() >= 300.0 or (ball.ycor() <= -300):
      		# print("Here")
        	# ball.sety(299.0)
			ydir *= -1
			# xdir *= -1
		
		# If ball makes it past paddle 2 (Paddle 1 scores)
		if ball.xcor() >= 380:
			ball.hideturtle()
			ball.goto(0,0)
			ball.showturtle()
			p1_score +=1
			trashtalk = random.choice(p1_comments_list)
			print(" ")
			print(trashtalk + p1_name +"!")
			score_update()
			time.sleep(1)
			if p1_score == 2:
				screen.onkey(p1_down, "w")
				screen.onkey(p1_up, "s")
				screen.listen()
			elif p2_score == 2:
				screen.onkey(p2_down, "Up")
				screen.onkey(p2_up, "Down")
				screen.listen()


		# if ball makes it past paddle 1 (Paddle 2 scores)
		elif ball.xcor() <= -360:
			ball.hideturtle()
			ball.goto(0,0)
			ball.showturtle()
			p2_score += 1
			trashtalk = random.choice(p2_comments_list)
			print(" ")
			print(trashtalk + p2_name +"!")
			score_update()
			time.sleep(1)
			if p1_score == 2:
				screen.onkey(p1_down, "w")
				screen.onkey(p1_up, "s")
				screen.listen()
			elif p2_score == 2:
				screen.onkey(p2_down, "Up")
				screen.onkey(p2_up, "Down")
				screen.listen()

		# Paddle Boundaries
		if p1.ycor() > 225:
			p1.goto(-350,300)

		if p1.ycor() < -300:
			p1.goto(-350,-300)

		if p2.ycor() > 300:
			p2.goto(325,300)

		if p2.ycor() < -300:
			p2.goto(325,-300)

		# Bouncing off paddles

		if ball.xcor() <= -310 and ball.ycor() <= p1.ycor() + 100 and ball.ycor() >= p1.ycor():
			inc = random.choice([-1])
			ydir *= inc
			xdir *= inc


		if ball.xcor() >= 330 and ball.ycor() <= p2.ycor() + 100 and ball.ycor() >= p2.ycor():
			inc = random.choice([1,2])
			if inc == 1:
				ydir *= -2
				xdir *= -1
			else: 
				ydir *= -1
				xdir *= -2
		
		# # Additional Rule - After two rounds, switch keys of winner
		# while p1_score == 2 or p2_score == 2:
		# 	if p1_score > p2_score:
		# 		screen.onkey(p1_down, "w")
		# 		screen.onkey(p1_up, "s")
		# 		screen.listen()
		# 	elif p2_score > p1_score:
		# 		screen.onkey(p2_down, "Up")
		# 		screen.onkey(p2_up, "Down")
		# 		screen.listen()

	
game()

# Replay Feature

congrats_1 = p1_name + " wins!" 
congrats_2 = p2_name + " wins!"

text.goto(0, 50)
if p1_score > p2_score:
	text.write(congrats_1, False, "center",("Papyrus", 25, "normal"))
elif p2_score > p1_score:
	text.write(congrats_1, False, "center",("Papyrus", 25, "normal"))
time.sleep(2)
text.clear()
text.write("Press Space to play again",False, "center",("Papyrus", 25, "normal"))
screen.onkey(game, "space")
screen.listen()



# TODO: 
# Set boundaries for the paddles
# Make Ball bounce off paddles 
# Scores - show them on screen, end game after 5 turns, display whatever message