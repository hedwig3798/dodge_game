import random
from pico2d import *
import game_framework
import game_world

class Player:

    life = 5
    score = 54.0

    def __init__(self, image):
        self.P_image = load_image(image)
        self.px , self.py = 0 , 0

        self.font = load_font('./font/LAB_digit.ttf', 20)
        self.color = (255,255,255)

        

    def update(self):
        Player.score += game_framework.frame_time
        pass

    def draw(self):
        self.P_image.draw(self.px, self.py)
        
        text_life = 'life: {:d}'.format(Player.life)
        self.font.draw(50,550, text_life, self.color)

        text_score = 'score: {:4.1f}'.format(Player.score)
        self.font.draw(50,500, text_score, self.color)
        
    def player_event(self, e):
        self.px , self.py = e.x, get_canvas_height() - e.y

    def other_event(self, e):
        self.px , self.py = get_canvas_width() - e.x, e.y
 
    def get_hitbox(self):
        return (self.px - 2.5, self.px + 2.5 , self.py - 2.5 , self.py + 2.5)
    
