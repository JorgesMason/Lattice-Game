#Points Scoring
#1/23/23

import turtle

score = turtle.Turtle()

score1 = 0
    

def up(): 
    global score1
    score.clear()
    score.write(score1, align="center", font=("Candara", "24", "bold")) 
    score1 = score1 + 1
    

score.penup()
score.goto(0,350)

screen = turtle.Screen() 

screen.listen()
screen.onkeypress(up, "Up")
score.write(score1, align="center", font=("Candara", "24", "bold"))

turtle.done()