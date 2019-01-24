from game2d import *
from constants import *
from pieces import *
from game import *

class Chess(GameApp):

    def start(self):
        self._state = HOMESCREEN
        self.lastkeys = 0
        self._game = None
        if (self._state == HOMESCREEN):
            self._text = GLabel(text = "Press 'Q' to Play", font_size = 100, bold = True, x = GAME_WIDTH/2, y = GAME_HEIGHT/2)
        else:
            self._text = None

    def update(self, dt):
        current = self.input.key_count
        if (current > 0 and self.lastkeys == 0):
            if (self.input.is_key_down('q') == True and self._state == HOMESCREEN):
                self._text = None
                self._game = Game()
                self._state = GAMESCREEN
        self.lastkeys = current

        if self._state == GAMESCREEN:
            self._game.update(self.input)

    def draw(self):

        if (self._state == HOMESCREEN):
            self._text.draw(self.view)

        if (self._state == GAMESCREEN):
            self._game.draw(self.view)
