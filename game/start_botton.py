from pico2d import *
import game_framework


class startbotton:
    
    image = None
    
    def __init__(self, x, y):
        if startbotton.image == None:
            startbotton.image = load_image('./image/startbotton.png')

        self.x , self.y = x , y

    def draw(self):
        self.image.draw(self.x,self.y)

    def update(self):
        pass

    def get_hitbox(self):
        return (self.x - 5, self.x + 5 , self.y - 5 , self.y + 5)
