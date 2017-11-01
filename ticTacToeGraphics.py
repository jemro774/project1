#Jack Robey
#11/1/17
#ticTacToeGraphics.py - Tic-Tac-Toe with graphics, and possibly AI (with set difficulties)

#imports
from ggame import *
from random import randint

if __name__ == '__main__':
    
    black = Color(0x000000,1)
    
    blackOutline = LineStyle(5,black)
    
    blackLine1 = LineAsset(0,50,blackOutline)
    
    Sprite(blackLine1,(1012,0))
    App().run()