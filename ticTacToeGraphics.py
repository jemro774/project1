#Jack Robey
#11/1/17
#ticTacToeGraphics.py - Tic-Tac-Toe with graphics

#imports
from ggame import *
from random import randint

def mouseClick(event):
    if event.x < 300 and event.y < 184:
        xpart1 = LineAsset(120,120,blackOutline)
        xpart2 = LineAsset(-120,120,blackOutline)
        Sprite(xpart1,(160,44))
        Sprite(xpart2,(280,44))
    elif event.x < 460 and event.y < 184:
        xpart1 = LineAsset(120,120,blackOutline)
        xpart2 = LineAsset(-120,120,blackOutline)
        Sprite(xpart1,(320,44))
        Sprite(xpart2,(440,44))
    elif event.x < 620 and event.y < 184:
        xpart1 = LineAsset(120,120,blackOutline)
        xpart2 = LineAsset(-120,120,blackOutline)
        Sprite(xpart1,(480,44))
        Sprite(xpart2,(600,44))
    elif event.x < 300 and event.y < 344:
        xpart1 = LineAsset(120,120,blackOutline)
        xpart2 = LineAsset(-120,120,blackOutline)
        Sprite(xpart1,(160,204))
        Sprite(xpart2,(280,204))
    elif event.x < 460 and event.y < 344:
        xpart1 = LineAsset(120,120,blackOutline)
        xpart2 = LineAsset(-120,120,blackOutline)
        Sprite(xpart1,(320,204))
        Sprite(xpart2,(440,204))
    elif event.x < 620 and event.y < 344:
        xpart1 = LineAsset(120,120,blackOutline)
        xpart2 = LineAsset(-120,120,blackOutline)
        Sprite(xpart1,(480,204))
        Sprite(xpart2,(600,204))
    elif event.x < 300 and event.y < 504:
        xpart1 = LineAsset(120,120,blackOutline)
        xpart2 = LineAsset(-120,120,blackOutline)
        Sprite(xpart1,(160,364))
        Sprite(xpart2,(280,364))
    elif event.x < 460 and event.y < 504:
        xpart1 = LineAsset(120,120,blackOutline)
        xpart2 = LineAsset(-120,120,blackOutline)
        Sprite(xpart1,(320,364))
        Sprite(xpart2,(440,364))
    elif event.x < 620 and event.y < 504:
        xpart1 = LineAsset(120,120,blackOutline)
        xpart2 = LineAsset(-120,120,blackOutline)
        Sprite(xpart1,(480,364))
        Sprite(xpart2,(600,364))
    
def computerTurn():
    num = randint(1,9)
    if num == 1:
        Sprite(o,(380,100))
    elif num == 2:
        Sprite(o,(380,260))
    elif num == 3:
        Sprite(o,(380,420))
    elif num == 4:
        Sprite(o,(220,100))
    elif num == 5:
        Sprite(o,(220,260))
    elif num == 6:
        Sprite(o,(220,420))
    elif num == 7:
        Sprite(o,(540,100))
    elif num == 8:
        Sprite(o,(540,260))
    else:
        Sprite(o,(540,420))

if __name__ == '__main__':
    
    black = Color(0x000000,1)
    white = Color(0xffffff,1)
    
    blackOutline = LineStyle(8,black)
    
    verticalLine = LineAsset(0,480,blackOutline)
    horizontalLine = LineAsset(480,0,blackOutline)
    xpart1 = LineAsset(120,120,blackOutline)
    xpart2 = LineAsset(-120,120,blackOutline)
    o = CircleAsset(60,blackOutline,white)
    
    Sprite(verticalLine,(300,24))
    Sprite(verticalLine,(460,24))
    Sprite(horizontalLine,(140,184))
    Sprite(horizontalLine,(140,344))
    
    App().listenMouseEvent('click',mouseClick)
    computerTurn()
    App().run()