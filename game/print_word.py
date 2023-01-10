from pico2d import *
import game_framework

class word:

    def __init__ (self, word2, font, x, y, color, size):

        self.x, self.y = x, y
        
        self.word2 = word2
        self.font = load_font(font, size)
        self.color = color
        self.hitbox = None
        

    def update(self):
        pass

    def draw(self):
        self.font.draw(self.x, self.y, self.word2, self.color)

    def get_hitbox(self):
        return self.hitbox
