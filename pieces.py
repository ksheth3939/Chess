from constants import *
from game2d import *

class Rook(GImage):
    def __init__(self, x1, y1, color):
        if color == 'black':
            GImage.__init__(self, x = x1, y = y1, width = PAWN_WIDTH, height = PAWN_HEIGHT, source = BlACK_PIECES[1])
            self._color = color
        else:
            GImage.__init__(self, x = x1, y = y1, width = PAWN_WIDTH, height = PAWN_HEIGHT, source = WHITE_PIECES[1])
            self._color = color

    def getColor(self):
        return self._color

class King(GImage):
    def __init__(self, x1, y1, color):
        if color == 'black':
            GImage.__init__(self, x = x1, y = y1, width = PAWN_WIDTH, height = PAWN_HEIGHT, source = BlACK_PIECES[5])
            self._color = color
        else:
            GImage.__init__(self, x = x1, y = y1, width = PAWN_WIDTH, height = PAWN_HEIGHT, source = WHITE_PIECES[5])
            self._color = color

    def getColor(self):
        return self._color

class Queen(GImage):
    def __init__(self, x1, y1, color):
        if color == 'black':
            GImage.__init__(self, x = x1, y = y1, width = PAWN_WIDTH, height = PAWN_HEIGHT, source = BlACK_PIECES[4])
            self._color = color
        else:
            GImage.__init__(self, x = x1, y = y1, width = PAWN_WIDTH, height = PAWN_HEIGHT, source = WHITE_PIECES[4])
            self._color = color

    def getColor(self):
        return self._color

class Pawn(GImage):
    def __init__(self, x1, y1, color):
        if color == 'black':
            GImage.__init__(self, x = x1, y = y1, width = PAWN_WIDTH, height = PAWN_HEIGHT, source = BlACK_PIECES[0])
            self._color = color
        else:
            GImage.__init__(self, x = x1, y = y1, width = PAWN_WIDTH, height = PAWN_HEIGHT, source = WHITE_PIECES[0])
            self._color = color

    def getColor(self):
        return self._color

class Bishop(GImage):
    def __init__(self, x1, y1, color):
        if color == 'black':
            GImage.__init__(self, x = x1, y = y1, width = PAWN_WIDTH, height = PAWN_HEIGHT, source = BlACK_PIECES[3])
            self._color = color
        else:
            GImage.__init__(self, x = x1, y = y1, width = PAWN_WIDTH, height = PAWN_HEIGHT, source = WHITE_PIECES[3])
            self._color = color

    def getColor(self):
        return self._color

class Knight(GImage):
    def __init__(self, x1, y1, color):
        if color == 'black':
            GImage.__init__(self, x = x1, y = y1, width = PAWN_WIDTH, height = PAWN_HEIGHT, source = BlACK_PIECES[2])
            self._color = color
        else:
            GImage.__init__(self, x = x1, y = y1, width = PAWN_WIDTH, height = PAWN_HEIGHT, source = WHITE_PIECES[2])
            self._color = color

    def getColor(self):
        return self._color

class Square(GRectangle):
    def __init__(self, x1, y1, color):
        GRectangle.__init__(self, x = x1, y = y1, width = GAME_WIDTH/8, height = GAME_HEIGHT/8, fillcolor = color)
