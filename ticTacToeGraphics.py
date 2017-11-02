#Jack Robey
#11/1/17
#ticTacToeGraphics.py - Tic-Tac-Toe with graphics, and possibly AI (with set difficulties)

#imports
from ggame import *
from random import randint

if __name__ == '__main__':
    
    black = Color(0x000000,1)
    
    blackOutline = LineStyle(8,black)
    
    verticalLine1 = LineAsset(0,480,blackOutline)
    verticalLine2 = LineAsset(0,480,blackOutline)
    horizontalLine1 = LineAsset(480,0,blackOutline)
    horizontalLine2 = LineAsset(480,0,blackOutline)
    
    Sprite(verticalLine1,(300,24))
    Sprite(verticalLine2,(460,24))
    Sprite(horizontalLine1,(140,184))
    Sprite(horizontalLine2,(140,344))
    App().run()