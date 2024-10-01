import keyboard
import Gridbase

#white circle:9675
#black square code:9632
#white square code:9633

class entity:
    def __init__(self):
        self.x = 3
        self.y = 3
        self.c = chr(9675)

    def spawn(self):
        charChange(x, y ,c)

    def moveX(self, num):
        if (num == 1 or -1):
            tempX = x
            x += num
            charChange(x, y, c)
            charChange(tempX, y, chr(9633))
    def moveY(self, num):
        if (num == 1 or -1):
            tempY = y
            y += num
            charChange(x, y, c)
            charChange(x, tempY, chr(9633))

    def setX(self, num):
        x = num
    def setY(self, num):
        y = num


class snake(entity):
    def __init__(self):
        self.x = 3
        self.y = 3
        self.c = chr(9632)
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.c = chr(9632)