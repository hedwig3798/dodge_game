from pico2d import *
import game_framework
import game_world


class Background:

    def __init__(self, image):
        self.image = load_image(image)

    def draw(self):
        self.image.draw(get_canvas_width() / 2, get_canvas_height() / 2)

    def update(self):
        pass

    
