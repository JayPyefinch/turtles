# Created by Jay Pyefinch
# on August 14th, 2020

from turtle import *

def main(): # The main function encapsulates all of the functionality of the program to be run at the bottom of the code.
    global t # allows the rest of the program to access this variable
    t = Turtle()
    drawTrack()
    doCourse()
    celebrate()

def drawTrack(): # Here, the program will draw the ground along with the hurdles and end flag. (Also changes pointer to turtle shape and sets speed 1)
    t.speed(1000)
    t.up()
    t.backward(340)
    t.down()
    t.forward(680)
    t.up()
    t.backward(580)
    drawHurdle()
    t.forward(200)
    drawHurdle()
    t.forward(200)
    drawHurdle()
    t.forward(100)
    drawEndFlag()
    t.backward(610)
    t.left(90)
    t.forward(15)
    t.right(90)
    t.shape("turtle")
    t.speed(1)

def drawEndFlag(): # This function draws the end flag when it is called from drawTrack().
    t.down()
    t.left(90)
    t.forward(65)
    t.left(90)
    t.forward(5)
    t.left(90)
    t.forward(5)
    t.right(90)
    t.forward(25)
    t.left(135)
    t.forward(5)
    t.right(90)
    t.forward(5)
    t.left(135)
    t.forward(25)
    t.left(90)
    t.forward(10)
    t.right(180)
    t.forward(64)
    t.left(90)
    t.up()



def drawHurdle(): # The three hurdles are drawn thanks to this function. Since this set of lines is repeated, it is more efficient to place it in a function. (Like the end flag, this is called in drawTrack().)
    t.down()
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.right(180)
    t.forward(10)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.up()

def jump(): # This method allows the turtle to clear the hurdles. It uses a for loop to smooth the tragectory of the turtle as it jumps.
    t.speed(2)
    t.left(80)
    for i in range(55):
        t.setheading(80 - (i*3)) # This 'i*3' is a modifier that steepens the curve of the jump.
        t.forward(3)
    t.setheading(0)
    t.speed(1)

def doCourse(): # Here, the turtle is guided along the track by a 'for' loop that selects which hurdle it is facing, and moving the appropriate distance in order to clear them.
    move = 0
    for i in range(3):
        if i == 0:
            move = 40
        elif i == 1:
            move = 100
        else:
            move = 85
        
        t.forward(move)
        jump()
    t.forward(50)

def celebrate(): # Since the turtle put in the work, it deserves a little celebration.
    t.left(90)
    for i in range(3):
        t.forward(10)
        t.backward(10)
    t.right(90)

main() # The main function is called and the program runs.
done() # This 'done()' ends the program without closing the window.