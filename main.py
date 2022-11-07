import random
import time 
import turtle

delay = 0.1

screen = turtle.Screen()
screen.title("zmeika") # nazvaniye
screen.bgcolor("white") # cvet fona
screen.setup(width=600, height=600) # parametri ekrana
screen.tracer(0) # 

zmeika = turtle.Turtle()
zmeika.shape('square')
zmeika.color('green')
zmeika.penup()
zmeika.goto(0, 0)
zmeika.direction = "Stop"




pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0 Snake№2 score: 0 ", align="center",
		font=("candara", 24, "bold"))

food = turtle.Turtle()
color = random.choice(["yellow","red","blue"])
shape = random.choice(['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'])
food.speed(0)
food.color(color)
food.shape("square")
food.penup()
food.goto(0,100)

 
def godown():
	if zmeika.direction != "up":
		zmeika.direction = "down"

def goup():
	if zmeika.direction != "down":
		zmeika.direction = "up"

def goleft():
	if zmeika.direction != "right":
		zmeika.direction = "left"

def goright():
	if zmeika.direction != "left":
		zmeika.direction = "right"

def move():
	if zmeika.direction == "up":
		y = zmeika.ycor()
		zmeika.sety(y+20)
	if zmeika.direction == "down":
		y = zmeika.ycor()
		zmeika.sety(y-20)
	if zmeika.direction == "left":
		x = zmeika.xcor()
		zmeika.setx(x-20)
	if zmeika.direction == "right":
		x = zmeika.xcor()
		zmeika.setx(x+20)
		
screen.listen()
screen.onkeypress(goup, "w")
screen.onkeypress(godown, "s")
screen.onkeypress(goleft, "a")
screen.onkeypress(goright, "d")

# сложности с обработкой нажатий на русские буквы, т.к. _tkinter.TclError: bad event type or keysym "ц"
# screen.onkeypress(goup, "ц")
# screen.onkeypress(godown, "ы")
# screen.onkeypress(goleft, "ф")
# screen.onkeypress(goright, "в")



# Main Gameplay
while True:
	screen.update()
	if zmeika.xcor() > 290 or zmeika.xcor() < -290 or zmeika.ycor() > 290 or zmeika.ycor() < -290:
		# time.sleep(1)
		zmeika.goto(0, 0)
		zmeika.direction = "Stop"
		colors = random.choice(['red', 'blue', 'green'])
		shapes = random.choice(['square', 'circle'])
		# for segment in segments1:
		# 	segment.goto(1000, 1000)
		# segments1.clear()
		# score = 0
		delay = 0.1
		pen.clear()
		# pen.write("Score: {} Snake№2 score: {} ".format(
		# 	score1, score2), align="center", font=("candara", 24, "bold"))

	

	# if zmeika.distance(food) < 20:
	# 	x = random.randint(-270, 270)
	# 	y = random.randint(-270, 270)
	# 	food.goto(x, y)

	# 	# Adding segment
	# 	new_segment = turtle.Turtle()
	# 	new_segment.speed(0)
	# 	new_segment.shape("square")
	# 	new_segment.color("orange") # tail colour
	# 	new_segment.penup()
	# 	segments1.append(new_segment)
	# 	delay -= 0.001
	# 	score1 += 10
	# 	# if score > high_score:
	# 	# 	high_score = score
	# 	pen.clear()
	# 	pen.write("Score: {} Score: {} ".format(
	# 		score1, score2), align="center", font=("candara", 24, "bold"))


	# # Checking for head collisions with body segments
	# for index in range(len(segments1)-1, 0, -1):
	# 	x = segments1[index-1].xcor()
	# 	y = segments1[index-1].ycor()
	# 	segments1[index].goto(x, y)
	# if len(segments1) > 0:
	# 	x = zmeika.xcor()
	# 	y = zmeika.ycor()
	# 	segments1[0].goto(x, y)

	move()

	# for segment in segments1:
	# 	if segment.distance(zmeika) < 20:
	# 		# time.sleep(1)
	# 		zmeika.goto(0, 0)
	# 		zmeika.direction = "stop"
	# 		colors = random.choice(['red', 'blue', 'green'])
	# 		shapes = random.choice(['square', 'circle'])
	# 		for segment in segments1:
	# 			segment.goto(1000, 1000)
	# 		segment.clear()

	# 		score1 = 0
	# 		delay = 0.1
	# 		pen.clear()
	# 		pen.write("Score: {} Snake№2 score:  {} ".format(
	# 			score1, score2), align="center", font=("candara", 24, "bold"))

	
	time.sleep(delay)

screen.mainloop()
