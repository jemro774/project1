#Jack Robey
#11/1/17
#ticTacToeGraphics.py - Tic-Tac-Toe with graphics

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
    x1part1 = LineAsset(120,120,blackOutline)
    x1part2 = LineAsset(-120,120,blackOutline)
    x2part1 = LineAsset(120,120,blackOutline)
    x2part2 = LineAsset(-120,120,blackOutline)
    x3part1 = LineAsset(120,120,blackOutline)
    x3part2 = LineAsset(-120,120,blackOutline)
    x4part1 = LineAsset(120,120,blackOutline)
    x4part2 = LineAsset(-120,120,blackOutline)
    x5part1 = LineAsset(120,120,blackOutline)
    x5part2 = LineAsset(-120,120,blackOutline)
    x6part1 = LineAsset(120,120,blackOutline)
    x6part2 = LineAsset(-120,120,blackOutline)
    x7part1 = LineAsset(120,120,blackOutline)
    x7part2 = LineAsset(-120,120,blackOutline)
    x8part1 = LineAsset(120,120,blackOutline)
    x8part2 = LineAsset(-120,120,blackOutline)
    x9part1 = LineAsset(120,120,blackOutline)
    x9part2 = LineAsset(-120,120,blackOutline)
    
    Sprite(verticalLine1,(300,24))
    Sprite(verticalLine2,(460,24))
    Sprite(horizontalLine1,(140,184))
    Sprite(horizontalLine2,(140,344))
    Sprite(x1part1,(320,44))
    Sprite(x1part2,(440,44))
    Sprite(x2part1,(320,204))
    Sprite(x2part2,(440,204))
    Sprite(x3part1,(320,364))
    Sprite(x3part2,(440,364))
    Sprite(x4part1,(160,44))
    Sprite(x4part2,(280,44))
    Sprite(x5part1,(160,204))
    Sprite(x5part2,(280,204))
    Sprite(x6part1,(160,364))
    Sprite(x6part2,(280,364))
    Sprite(x7part1,(480,44))
    Sprite(x7part2,(600,44))
    Sprite(x8part1,(480,204))
    Sprite(x8part2,(600,204))
    Sprite(x9part1,(480,364))
    Sprite(x9part2,(600,364))
    App().run()