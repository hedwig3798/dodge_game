from pico2d import *

import game_framework
import game_world
import layer

import print_word
from background import Background

import main_state


def click(mouse, button):

    button_box = button.get_hitbox()

    L, R, B, T = range(4)

    if button_box[L] < mouse.x < button_box[R]:
        if button_box[T] -10 < mouse.y < button_box[B] + 15:
            return True

    return False

def enter():
    global ex

    file = open('high_score.json', 'r')
    
    scores = json.load(file)

    file.close
    
    game_world.init(layer.count)
    SDL_ShowCursor(SDL_ENABLE)

    bg = Background('./image/background.png')
    game_world.add(bg, layer.bg)

    x = 100
    y = 500
    
    for s in scores:




        score = '{:4.1f}'.format(s["score"])
        
        first = print_word.word(s["name"] + ": "+ score, './font/Pixel.ttf', x,y, (255,255,255), 50)
        game_world.add(first, layer.obstacle)
        y -= 100


    ex = print_word.word("EXIT", './font/Pixel.ttf', 500,100, (255,255,255), 50)
    game_world.add(ex, layer.obstacle)
    ex.hitbox = (500,645,500,470)


def exit():
    pass

def update():
    pass

      
    
def draw():
    clear_canvas()
    game_world.draw()
    update_canvas()
    pass

def handle_events():

    global ex
    

    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                game_framework.pop_state()
            if e.key == SDLK_r:
                game_framework.change_state(main_state)

        if e.type == SDL_MOUSEMOTION or e.type == SDL_MOUSEBUTTONDOWN:
            if click(e, ex):
                ex.color = (255,255,255)
                if e.type == SDL_MOUSEBUTTONDOWN:
                    game_framework.pop_state()
            else:
                ex.color = (150,150,150)


            



def pause():
    pass

def resume():

    pass


if __name__ == '__main__':
    import sys
    current_module = sys.modules[__name__]
    open_canvas()
    game_framework.run(current_module)
    close_canvas()

