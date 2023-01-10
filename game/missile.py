from pico2d import *
import game_framework

from player import Player


class Missile:
    image = None
    speed = 200 + int(Player.score)
    
    def __init__(self, x, y ,dx, dy):
        if Missile.image == None:
            Missile.image = load_image('./image/missile.png')

        self.x , self.y = x , y

        self.dx , self.dy = dx, dy

    def draw(self):
        self.image.draw(self.x,self.y)

    def update(self):
        self.x += self.dx * game_framework.frame_time * Missile.speed
        self.y += self.dy * game_framework.frame_time * Missile.speed

    def get_hitbox(self):
        return (self.x - 2.5, self.x + 2.5 , self.y - 2.5 , self.y + 2.5)
