from pico2d import *

from print_word import word
from background import Background

import game_framework
import game_world
import layer

import ingame_state
import show_score_state

import os

white = (255, 255, 255)
gray = (150, 150, 150)

state = -1


def click(mouse, button):
    button_box = button.get_hitbox()

    L, R, B, T = range(4)

    if button_box[L] < mouse.x < button_box[R]:
        if button_box[T] - 10 < mouse.y < button_box[B] + 15:
            return True

    return False


def enter():
    global start_button, HS_button, exit_button

    game_world.init(layer.count)
    SDL_ShowCursor(SDL_ENABLE)

    bg = Background(os.path.join(os.path.abspath('image'), 'background.png'))
    game_world.add(bg, layer.bg)

    game_over = word("""ICE""", os.path.join(os.path.abspath('font'), 'Pixel.ttf'), 100, 400, (0, 0, 255), 50)
    game_world.add(game_over, layer.obstacle)

    restart = word('DODGE', os.path.join(os.path.abspath('font'), 'Pixel.ttf'), 100, 300, white, 50)
    game_world.add(restart, layer.obstacle)

    score = word('FIRE', os.path.join(os.path.abspath('font'), 'Pixel.ttf'), 100, 200, (255, 0, 0), 50)
    game_world.add(score, layer.obstacle)

    start_button = word('START', os.path.join(os.path.abspath('font'), 'Pixel.ttf'), 500, 400, gray, 50)
    game_world.add(start_button, layer.obstacle)
    start_button.hitbox = (500, 720, 200, 170)

    HS_button = word('H.S.', os.path.join(os.path.abspath('font'), 'Pixel.ttf'), 500, 300, gray, 50)
    game_world.add(HS_button, layer.obstacle)
    HS_button.hitbox = (500, 620, 300, 270)

    exit_button = word('EXIT', os.path.join(os.path.abspath('font'), 'Pixel.ttf'), 500, 200, gray, 50)
    game_world.add(exit_button, layer.obstacle)
    exit_button.hitbox = (500, 650, 400, 370)

    pass


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
    global p, o, state, botton, state, start_button, HS_button, exit_button, state
    events = get_events()

    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                game_framework.pop_state()
            if e.key == SDLK_r:
                game_framework.change_state(ingame_state)

        if e.type == SDL_MOUSEMOTION or e.type == SDL_MOUSEBUTTONDOWN:
            if click(e, start_button):
                start_button.color = white
                if e.type == SDL_MOUSEBUTTONDOWN:
                    game_framework.change_state(ingame_state)
            else:
                start_button.color = gray

            if click(e, HS_button):
                HS_button.color = white
                if e.type == SDL_MOUSEBUTTONDOWN:
                    game_framework.push_state(show_score_state)

            else:
                HS_button.color = gray

            if click(e, exit_button):
                exit_button.color = white
                if e.type == SDL_MOUSEBUTTONDOWN:
                    game_framework.quit()
            else:
                exit_button.color = gray


def pause():
    pass


def resume():
    enter()
    pass


if __name__ == '__main__':
    import sys

    current_module = sys.modules[__name__]
    open_canvas()
    game_framework.run(current_module)
    close_canvas()
