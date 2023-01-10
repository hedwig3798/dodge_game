from pico2d import *

import game_framework
import game_world
import layer

import print_word
from background import Background

import gameover_state

name = [65,65,65]

def get_name():
    global name

    return chr(name[0]) + chr(name[1]) + chr(name[2])

def click(mouse, button):

    button_box = button.get_hitbox()

    L, R, B, T = range(4)

    if button_box[L] < mouse.x < button_box[R]:
        if button_box[T] -10 < mouse.y < button_box[B] + 15:
            return True

    return False

def enter():
    global first, second, third, name, enter

    

    game_world.init(layer.count)
    SDL_ShowCursor(SDL_ENABLE)

    bg = Background('./image/background.png')
    game_world.add(bg, layer.bg)

    inof = print_word.word("YOU GOT HIGH SCORE", './font/Pixel.ttf', 50,500, (255,255,255), 50)
    game_world.add(inof, layer.obstacle)

    inof2 = print_word.word("ENTER YOUR NAME", './font/Pixel.ttf', 80,400, (255,255,255), 50)
    game_world.add(inof2, layer.obstacle)
    

    first = print_word.word(chr(name[0]), './font/Pixel.ttf', 140,200, (255,255,255), 150)
    game_world.add(first, layer.obstacle)
    first.hitbox = (140,260,430,310)

    second = print_word.word(chr(name[1]), './font/Pixel.ttf', 340,200, (255,255,255), 150)
    game_world.add(second, layer.obstacle)
    second.hitbox = (340,460,430,310)

    third = print_word.word(chr(name[2]), 'font/Pixel.ttf', 540,200, (255,255,255), 150)
    game_world.add(third, layer.obstacle)
    third.hitbox = (540,660,430,310)

    enter = print_word.word("ENTER", './font/Pixel.ttf', 280,100, (255,255,255), 50)
    game_world.add(enter, layer.obstacle)
    enter.hitbox = (280,500,500,470)


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

    global first, second, third, name, enter
    

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
            if click(e, first):
                if e.type == SDL_MOUSEBUTTONDOWN:
                    game_world.remove(first)
                    
                    name[0] += 1

                    if name[0] > 90:
                        name[0] = 65

                    first = print_word.word(chr(name[0]), './font/Pixel.ttf', 140,200, (255,255,255), 150)
                    game_world.add(first, layer.obstacle)
                    first.hitbox = (140,260,430,310)
                    

            if click(e, second):
                if e.type == SDL_MOUSEBUTTONDOWN:
                    game_world.remove(second)
                    
                    name[1] += 1

                    if name[1] > 90:
                        name[1] = 65

                    second = print_word.word(chr(name[1]), './font/Pixel.ttf', 340,200, (255,255,255), 150)
                    game_world.add(second, layer.obstacle)
                    second.hitbox = (340,460,430,310)

    
            if click(e, third):
                if e.type == SDL_MOUSEBUTTONDOWN:
                    game_world.remove(third)
                    
                    name[2] += 1

                    if name[2] > 90:
                        name[2] = 65

                    third = print_word.word(chr(name[2]), './font/Pixel.ttf', 540,200, (255,255,255), 150)
                    game_world.add(third, layer.obstacle)
                    third.hitbox = (540,660,430,310)


            if click(e, enter):
                if e.type == SDL_MOUSEBUTTONDOWN:
                    game_framework.change_state(gameover_state)


            



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

