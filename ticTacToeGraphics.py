#Jack Robey
#11/1/17
#ticTacToeGraphics.py - Tic-Tac-Toe with graphics

from ggame import *
from random import randint

def mouseClick(event):
    if event.x < 300 and event.x > 140 and event.y < 184 and event.y > 24 and isEmpty(1):
        xpart1 = LineAsset(120,120,blackOutline)
        xpart2 = LineAsset(-120,120,blackOutline)
        Sprite(xpart1,(160,44))
        Sprite(xpart2,(280,44))
        data['square1'] = 'X'
    elif event.x < 460 and event.x > 300 and event.y < 184 and event.y > 24 and isEmpty(2):
        xpart1 = LineAsset(120,120,blackOutline)
        xpart2 = LineAsset(-120,120,blackOutline)
        Sprite(xpart1,(320,44))
        Sprite(xpart2,(440,44))
        data['square2'] = 'X'
    elif event.x < 620 and event.x > 460 and event.y < 184 and event.y > 24 and isEmpty(3):
        xpart1 = LineAsset(120,120,blackOutline)
        xpart2 = LineAsset(-120,120,blackOutline)
        Sprite(xpart1,(480,44))
        Sprite(xpart2,(600,44))
        data['square3'] = 'X'
    elif event.x < 300 and event.x > 140 and event.y < 344 and event.y > 184 and isEmpty(4):
        xpart1 = LineAsset(120,120,blackOutline)
        xpart2 = LineAsset(-120,120,blackOutline)
        Sprite(xpart1,(160,204))
        Sprite(xpart2,(280,204))
        data['square4'] = 'X'
    elif event.x < 460 and event.x > 300 and event.y < 344 and event.y > 184 and isEmpty(5):
        xpart1 = LineAsset(120,120,blackOutline)
        xpart2 = LineAsset(-120,120,blackOutline)
        Sprite(xpart1,(320,204))
        Sprite(xpart2,(440,204))
        data['square5'] = 'X'
    elif event.x < 620 and event.x > 460 and event.y < 344 and event.y > 184 and isEmpty(6):
        xpart1 = LineAsset(120,120,blackOutline)
        xpart2 = LineAsset(-120,120,blackOutline)
        Sprite(xpart1,(480,204))
        Sprite(xpart2,(600,204))
        data['square6'] = 'X'
    elif event.x < 300 and event.x > 140 and event.y < 504 and event.y > 344 and isEmpty(7):
        xpart1 = LineAsset(120,120,blackOutline)
        xpart2 = LineAsset(-120,120,blackOutline)
        Sprite(xpart1,(160,364))
        Sprite(xpart2,(280,364))
        data['square7'] = 'X'
    elif event.x < 460 and event.x > 300 and event.y < 504 and event.y > 344 and isEmpty(8):
        xpart1 = LineAsset(120,120,blackOutline)
        xpart2 = LineAsset(-120,120,blackOutline)
        Sprite(xpart1,(320,364))
        Sprite(xpart2,(440,364))
        data['square8'] = 'X'
    elif event.x < 620 and event.x > 460 and event.y < 504 and event.y > 344 and isEmpty(9):
        xpart1 = LineAsset(120,120,blackOutline)
        xpart2 = LineAsset(-120,120,blackOutline)
        Sprite(xpart1,(480,364))
        Sprite(xpart2,(600,364))
        data['square9'] = 'X'
    computerTurn()
    
def computerTurn():
    num = randint(1,9)
    if num == 1 and isEmpty(1):
        Sprite(o,(380,100))
        data['square1'] = 'O'
    elif num == 2 and isEmpty(2):
        Sprite(o,(380,260))
        data['square2'] = 'O'
    elif num == 3 and isEmpty(3):
        Sprite(o,(380,420))
        data['square3'] = 'O'
    elif num == 4 and isEmpty(4):
        Sprite(o,(220,100))
        data['square4'] = 'O'
    elif num == 5 and isEmpty(5):
        Sprite(o,(220,260))
        data['square5'] = 'O'
    elif num == 6 and isEmpty(6):
        Sprite(o,(220,420))
        data['square6'] = 'O'
    elif num == 7 and isEmpty(7):
        Sprite(o,(540,100))
        data['square7'] = 'O'
    elif num == 8 and isEmpty(8):
        Sprite(o,(540,260))
        data['square8'] = 'O'
    else:
        Sprite(o,(540,420))
        data['square9'] = 'O'

def isEmpty(x):
    if x == 1 and data['square1'] == '':
        return True
    elif x == 2 and data['square2'] == '':
        return True
    elif x == 3 and data['square3'] == '':
        return True
    elif x == 4 and data['square4'] == '':
        return True
    elif x == 5 and data['square5'] == '':
        return True
    elif x == 6 and data['square6'] == '':
        return True
    elif x == 7 and data['square7'] == '':
        return True
    elif x == 8 and data['square8'] == '':
        return True
    elif x == 9 and data['square9'] == '':
        return True
    elif x == 1 and data['square1'] == 'X':
        return False
    elif x == 2 and data['square2'] == 'X':
        return False
    elif x == 3 and data['square3'] == 'X':
        return False
    elif x == 4 and data['square4'] == 'X':
        return False
    elif x == 5 and data['square5'] == 'X':
        return False
    elif x == 6 and data['square6'] == 'X':
        return False
    elif x == 7 and data['square7'] == 'X':
        return False
    elif x == 8 and data['square8'] == 'X':
        return False
    elif x == 9 and data['square9'] == 'X':
        return False
    elif x == 1 and data['square1'] == 'O':
        return False
    elif x == 2 and data['square2'] == 'O':
        return False
    elif x == 3 and data['square3'] == 'O':
        return False
    elif x == 4 and data['square4'] == 'O':
        return False
    elif x == 5 and data['square5'] == 'O':
        return False
    elif x == 6 and data['square6'] == 'O':
        return False
    elif x == 7 and data['square7'] == 'O':
        return False
    elif x == 8 and data['square8'] == 'O':
        return False
    elif x == 9 and data['square9'] == 'O':
        return False

if __name__ == '__main__':
    
    data = {}
    data['square1'] = ''
    data['square2'] = ''
    data['square3'] = ''
    data['square4'] = ''
    data['square5'] = ''
    data['square6'] = ''
    data['square7'] = ''
    data['square8'] = ''
    data['square9'] = ''
    
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
    App().run()