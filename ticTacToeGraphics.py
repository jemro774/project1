#Jack Robey
#11/1/17
#ticTacToeGraphics.py - Tic-Tac-Toe with graphics

from ggame import *
from random import randint

#allows the user to fill a square with X through clicking
def mouseClick(event):
    if data['Game Over'] == False:
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
        if winner() == True:
            print('X wins!')
            data['Game Over'] = True
            return
        computerTurn()
        if winner() == True:
            print('O wins!')
            data['Game Over'] = True
            return
        fullBoard()

#allows the computer to fill a square with O in response to a user click
def computerTurn():
    if data['Game Over'] == False:
        num = randint(1,9)
        if num == 1 and isEmpty(1):
            Sprite(o,(220,100))
            data['square1'] = 'O'
        elif num == 2 and isEmpty(2):
            Sprite(o,(380,100))
            data['square2'] = 'O'
        elif num == 3 and isEmpty(3):
            Sprite(o,(540,100))
            data['square3'] = 'O'
        elif num == 4 and isEmpty(4):
            Sprite(o,(220,260))
            data['square4'] = 'O'
        elif num == 5 and isEmpty(5):
            Sprite(o,(380,260))
            data['square5'] = 'O'
        elif num == 6 and isEmpty(6):
            Sprite(o,(540,260))
            data['square6'] = 'O'
        elif num == 7 and isEmpty(7):
            Sprite(o,(220,420))
            data['square7'] = 'O'
        elif num == 8 and isEmpty(8):
            Sprite(o,(380,420))
            data['square8'] = 'O'
        elif num == 9 and isEmpty(9):
            Sprite(o,(540,420))
            data['square9'] = 'O'
        else:
            computerTurn()

#determines whether a square is empty or full
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
    else:
        return False

#determines the patterns of X's and O's that lead to a win
def winner():
    if data['square1'] == 'X' and data['square2'] == 'X' and data['square3'] == 'X':
        return True
    elif data['square4'] == 'X' and data['square5'] == 'X' and data['square6'] == 'X':
        return True
    elif data['square7'] == 'X' and data['square8'] == 'X' and data['square9'] == 'X':
        return True
    elif data['square1'] == 'X' and data['square4'] == 'X' and data['square7'] == 'X':
        return True
    elif data['square2'] == 'X' and data['square5'] == 'X' and data['square8'] == 'X':
        return True
    elif data['square3'] == 'X' and data['square6'] == 'X' and data['square9'] == 'X':
        return True
    elif data['square1'] == 'X' and data['square5'] == 'X' and data['square9'] == 'X':
        return True
    elif data['square3'] == 'X' and data['square5'] == 'X' and data['square7'] == 'X':
        return True
    elif data['square1'] == 'O' and data['square2'] == 'O' and data['square3'] == 'O':
        return True
    elif data['square4'] == 'O' and data['square5'] == 'O' and data['square6'] == 'O':
        return True
    elif data['square7'] == 'O' and data['square8'] == 'O' and data['square9'] == 'O':
        return True
    elif data['square1'] == 'O' and data['square4'] == 'O' and data['square7'] == 'O':
        return True
    elif data['square2'] == 'O' and data['square5'] == 'O' and data['square8'] == 'O':
        return True
    elif data['square3'] == 'O' and data['square6'] == 'O' and data['square9'] == 'O':
        return True
    elif data['square1'] == 'O' and data['square5'] == 'O' and data['square9'] == 'O':
        return True
    elif data['square3'] == 'O' and data['square5'] == 'O' and data['square7'] == 'O':
        return True
    else:
        return False

#tells the computer that the board is full
def fullBoard():
    if isEmpty(1) == False and isEmpty(2) == False and isEmpty(3) == False and isEmpty(4) == False and isEmpty(5) == False and isEmpty(6) == False and isEmpty(7) == False and isEmpty(8) == False and isEmpty(9) == False:
        return True
    else:
        return False

#runs the game
if __name__ == '__main__':
    
    #variables for individual squares and a variable for "game over"
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
    data['Game Over'] = False
    
    #colors
    black = Color(0x000000,1)
    white = Color(0xffffff,1)
    
    #outline for graphics
    blackOutline = LineStyle(8,black)
    
    #lines for the board, the X's, and a circle for the O's
    verticalLine = LineAsset(0,480,blackOutline)
    horizontalLine = LineAsset(480,0,blackOutline)
    xpart1 = LineAsset(120,120,blackOutline)
    xpart2 = LineAsset(-120,120,blackOutline)
    o = CircleAsset(60,blackOutline,white)
    
    #the board
    Sprite(verticalLine,(300,24))
    Sprite(verticalLine,(460,24))
    Sprite(horizontalLine,(140,184))
    Sprite(horizontalLine,(140,344))
    
    App().listenMouseEvent('click',mouseClick)
    App().run()