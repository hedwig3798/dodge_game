import random
from pico2d import *
import json

import game_framework
import game_world
import layer

import print_word
from background import Background

import main_state
import high_score_state

from player import Player



def load_score():
    global scores
    
    file = open('./high_score.json', 'r')
    
    scores = json.load(file)

    file.close

def save_score(scores):
    
    file = open('./high_score.json', 'w')
    
    scores = json.dump(scores,file)
    
    file.close


def enter():

    global scores

    if_high = 0

    game_world.init(layer.count)
    SDL_ShowCursor(SDL_ENABLE)

    bg = Background('./image/background.png')
    game_world.add(bg, layer.bg)
    

    game_over = print_word.word('GAME OVER', './font/Pixel.ttf', 220,400, (255,255,255), 50)
    game_world.add(game_over, layer.obstacle)

    restart = print_word.word('PRESS R TO RESTART', './font/Pixel.ttf', 30,300, (255,255,255), 50)
    game_world.add(restart, layer.obstacle)

    text_score = 'SCORE: {:4.1f}'.format(Player.score)

    score = print_word.word(text_score, './font/Pixel.ttf', 30,200, (255,255,255), 50)
    game_world.add(score, layer.obstacle)

    load_score()

    score_date = json.dumps(Player.score)

    

    name = high_score_state.get_name()
    

    now_score = {"name": name, "score": Player.score}

    for i in range(5):
        if now_score["score"] > scores[i]["score"]:
            
            temp = scores[i]
            scores[i] = now_score
            now_score = temp

    save_score(scores)



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

    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                game_framework.pop_state()
            if e.key == SDLK_r:
                game_framework.change_state(main_state)

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
