#Devin Avery 
#1/19/23
#Lattice Game

import turtle
import turtle as p1
import winsound

p1 = turtle.Turtle()

p1.penup()
p1.goto(-250,-120)

#-10,120


screen = turtle.Screen()

screen.setup(1152,653)

screen.bgpic("C:/Users/Devin/Desktop/Lattice-Game/Fintech-Lab.png")

screen.addshape("richard-moves.gif")
screen.addshape("richard-moves-2.gif")
screen.addshape("richard-rock-crouch.gif")
screen.addshape("richard-rock-stands.gif")
p1.shape("richard-rock-stands.gif")

#Stands back up from crouching 
def go_up():
    p1.shape("richard-rock-stands.gif")

#Moves left
def go_left():
    winsound.PlaySound('walks.wav', winsound.SND_ASYNC)
    p1.goto(p1.xcor()-30, p1.ycor())
    p1.shape("richard-moves.gif")
    global score1
    if p1.xcor()==-10:
        score.clear()
        score1 = score1 - 250
        score.write(score1, align="center", font=("Candara", "24", "bold")) 

#Moves right
def go_right():
    winsound.PlaySound('walks.wav', winsound.SND_ASYNC)
    p1.goto(p1.xcor()+30, p1.ycor())
    p1.shape("richard-moves-2.gif")
    #Scoring system
    global score1
    if p1.xcor()==-10:
        score.clear()
        score1 = score1 - 250
        score.write(score1, align="center", font=("Candara", "24", "bold")) 
    

#Crouches on down key
def crouch():
    winsound.PlaySound('corouch.wav', winsound.SND_ASYNC)
    p1.shape("richard-rock-crouch.gif")

#Jumps on space key 
def go_jump():
    winsound.PlaySound('jump.wav', winsound.SND_ASYNC)
    p1.goto(p1.xcor(), p1.ycor()+200)
    p1.goto(p1.xcor(), p1.ycor()-200)


#Scoring system
score = turtle.Turtle()
score.penup()
score1 = 0
score.goto(-500,275)
score.write(score1, align="center", font=("Candara", "24", "bold"))
score.hideturtle() 

screen.listen()

#user Input
screen.listen()
screen.onkeypress(go_up,"Up")
screen.onkeypress(go_left,"Left")
screen.onkeypress(go_right,"Right")
screen.onkeypress(go_jump,"space")
screen.onkeypress(crouch,"Down")
screen.listen()

turtle.done() 
