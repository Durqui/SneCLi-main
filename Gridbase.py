#black square code:9632
#white square code:9633

import keyboard
import time
import os

posX = 3
posY = 3

#This matrix contains each line of the screen, the idea for the future is to navigate by using
matrix = [["-","-","-","-","-"], [chr(9632),chr(9632),chr(9632),chr(9632),chr(9632)], [chr(9632),chr(9632),chr(9632),chr(9632),chr(9632)], [chr(9632),chr(9632),chr(9632),chr(9632),chr(9632)], [chr(9632),chr(9632),chr(9632),chr(9632),chr(9632)]
    , [chr(9632),chr(9632),chr(9632),chr(9632),chr(9632)], ["-","-","-","-","-"]]

global running
running = True


#Will print the inital lines of the matrix
def initMatrixPrnt():
    print(matrix[0])
    print(matrix[1])
    print(matrix[2])
    print(matrix[3])
    print(matrix[3])
    print(matrix[4])
    print(matrix[6])

#This will then rewrite over, idea is so it will properly render when the player is moving
def matrixPrnt():
    print(matrix[0],end='\r')
    print(matrix[1],end='\r')
    print(matrix[2],end='\r')
    print(matrix[3],end='\r')
    print(matrix[3],end='\r')
    print(matrix[4],end='\r')
    print(matrix[6],end='\r')


initMatrixPrnt()
while running == True:
    if (keyboard.is_pressed('escape')):
        running = False
    time.sleep(.5)
    matrixPrnt()
