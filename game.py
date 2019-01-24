from game2d import *
from constants import *
from pieces import *

class Game(object):

    def __init__(self):
        self.turn = 'white'
        self.chosenPiece = None
        self._board = self.createBoard()
        self.pawnsWhite = self.createWhitePawns()
        self.pawnsBlack = self.createBlackPawns()
        self.rooksWhite = self.createWhiteRooks()
        self.rooksBlack = self.createBlackRooks()
        self.knightsWhite = self.createWhiteKnights()
        self.knightsBlack = self.createBlackKnights()
        self.bishopsWhite = self.createWhiteBishops()
        self.bishopsBlack = self.createBlackBishops()
        self.queenWhite = Queen(GAME_WIDTH/2 - GAME_WIDTH/16, GAME_WIDTH/16, 'white')
        self.queenBlack = Queen(GAME_WIDTH/2 - GAME_WIDTH/16, GAME_WIDTH - GAME_WIDTH/16, 'black')
        self.kingWhite = King(GAME_WIDTH/2 + GAME_WIDTH/16, GAME_WIDTH/16, 'white')
        self.kingBlack = King(GAME_WIDTH/2 + GAME_WIDTH/16, GAME_WIDTH - GAME_WIDTH/16, 'black')

    def createBoard(self):
        board = []
        x = 50
        y = 50
        color = 'tan'
        for a in range(0,9):
            x = 50
            for b in range(0,9):
                board.append(Square(x,y, color))
                if color == "tan":
                    color = 'beige'
                else:
                    color = 'tan'
                x = x + GAME_WIDTH/8
            y = y + GAME_HEIGHT/8

        return board
    def createWhitePawns(self):
        b = []
        x = GAME_WIDTH/16
        y = GAME_HEIGHT/8 + GAME_WIDTH/16
        for a in range(0,8):
            b.append(Pawn(x, y, 'white'))
            x = x + GAME_WIDTH/8
        return b
    def createBlackPawns(self):

        b = []
        x = GAME_WIDTH/16
        y = GAME_HEIGHT - GAME_HEIGHT/16 - GAME_HEIGHT/8
        for a in range(0,8):
            b.append(Pawn(x, y, 'black'))
            x = x + GAME_WIDTH/8
        return b
    def createWhiteRooks(self):
        b = []
        b.append(Rook(GAME_WIDTH/16, GAME_WIDTH/16, 'white'))
        b.append(Rook(GAME_WIDTH - GAME_WIDTH/16, GAME_WIDTH/16, 'white'))
        return b
    def createBlackRooks(self):
        b = []
        b.append(Rook(GAME_WIDTH/16, GAME_WIDTH - GAME_WIDTH/16, 'black'))
        b.append(Rook(GAME_WIDTH - GAME_WIDTH/16, GAME_WIDTH - GAME_WIDTH/16, 'black'))
        return b
    def createWhiteKnights(self):
        b = []
        b.append(Knight(GAME_WIDTH/16 + GAME_WIDTH/8, GAME_WIDTH/16, 'white'))
        b.append(Knight(GAME_WIDTH - GAME_WIDTH/16 - GAME_WIDTH/8, GAME_WIDTH/16, 'white'))
        return b
    def createBlackKnights(self):
        b = []
        b.append(Knight(GAME_WIDTH/16 + GAME_WIDTH/8, GAME_WIDTH - GAME_WIDTH/16, 'black'))
        b.append(Knight(GAME_WIDTH - GAME_WIDTH/16 - GAME_WIDTH/8, GAME_WIDTH - GAME_WIDTH/16, 'black'))
        return b
    def createWhiteBishops(self):
        b = []
        b.append(Bishop(GAME_WIDTH/16 + GAME_WIDTH/4, GAME_WIDTH/16, 'white'))
        b.append(Bishop(GAME_WIDTH - GAME_WIDTH/16 - GAME_WIDTH/4, GAME_WIDTH/16, 'white'))
        return b
    def createBlackBishops(self):
        b = []
        b.append(Bishop(GAME_WIDTH/16 + GAME_WIDTH/4, GAME_WIDTH - GAME_WIDTH/16, 'black'))
        b.append(Bishop(GAME_WIDTH - GAME_WIDTH/16 - GAME_WIDTH/4, GAME_WIDTH - GAME_WIDTH/16, 'black'))
        return b

    def update(self, input):
        self.goTurn(input)

    def goTurn(self, input):
        if (self.chosenPiece == None):
            self.chosenPiece = self.choosePiece(input)
        if (self.chosenPiece != None and self.chosenPiece.getColor() == self.turn):
            self.movePiece(input)

    def movePiece(self, input):
        if (self.chosenPiece.contains(input.touch)):
            pass
        else:
            for a in self._board:
                if a.contains(input.touch):
                    self.chosenPiece.x = a.x
                    self.chosenPiece.y = a.y
                    self.chosenPiece = None
                    return None

    def choosePiece(self, input):
        if input.touch != None:
            for x in self.pawnsBlack:
                if (x.contains(input.touch)):
                    return x
            for x in self.pawnsWhite:
                if (x.contains(input.touch)):
                    return x
            for x in self.rooksBlack:
                if (x.contains(input.touch)):
                    return x
            for x in self.rooksWhite:
                if (x.contains(input.touch)):
                    return x
            for x in self.bishopsBlack:
                if (x.contains(input.touch)):
                    return x
            for x in self.bishopsWhite:
                if (x.contains(input.touch)):
                    return x
            for x in self.knightsBlack:
                if (x.contains(input.touch)):
                    return x
            for x in self.knightsWhite:
                if (x.contains(input.touch)):
                    return x
            if self.queenBlack.contains(input.touch):
                return self.queenBlack
            if self.queenWhite.contains(input.touch):
                return self.queenWhite
            if self.kingBlack.contains(input.touch):
                return self.kingBlack
            if self.kingWhite.contains(input.touch):
                return self.kingWhite

        return None

    def draw(self, view):
        for a in self._board:
            a.draw(view)
        for a in self.pawnsWhite:
            if a != None:
                a.draw(view)
        for a in self.pawnsBlack:
            if a != None:
                a.draw(view)
        for a in self.rooksWhite:
            if a != None:
                a.draw(view)
        for a in self.rooksBlack:
            if a != None:
                a.draw(view)
        for a in self.knightsWhite:
            if a != None:
                a.draw(view)
        for a in self.knightsBlack:
            if a != None:
                a.draw(view)
        for a in self.bishopsWhite:
            if a != None:
                a.draw(view)
        for a in self.bishopsBlack:
            if a != None:
                a.draw(view)
        if self.queenWhite != None:
            self.queenWhite.draw(view)
        if self.queenBlack != None:
            self.queenBlack.draw(view)
        if self.kingWhite != None:
            self.kingWhite.draw(view)
        if self.kingBlack != None:
            self.kingBlack.draw(view)
