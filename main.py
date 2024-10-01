import keyboard
import time
import Gridbase
from Gridbase import initMatrixPrnt
from Gridbase import matrixPrnt
import Entities

global running
running = True

initMatrixPrnt()
while running:
    if keyboard.is_pressed('escape'):
        running = False
        #print("finished")
    time.sleep(.5)
    matrixPrnt()
