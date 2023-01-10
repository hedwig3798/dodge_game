import random
from pico2d import *
import json


import game_framework
import game_world
import layer



from player import Player
from background import Background
from missile import Missile
from start_botton import startbotton


import gameover_state
import high_score_state

# import font as font_mod

p = None
bg = None


m_count = 50


STATE_GAMEOVER, STATE_INGAME, STATE_PAUSED, STATE_START = range(4)

state = STATE_START

start = 0


def paused():
    global state
    state = STATE_PAUSED


def create_missile():
    w = get_canvas_width()
    h = get_canvas_height()
    
    side = random.randint(1,4)

    dx = random.random()
    dy = 1- dx
    

    if side == 1: # top
        x, y = random.randint(0,w), h
        dy *= -1
        
    elif side == 2: # right
        x, y = w, random.randint(0,h)
        dx *= -1
        
    elif side == 3: # bottom
        x, y = random.randint(0,w), 0
        
    elif side == 4: # left
        x, y = 0, random.randint(0,h)

    game_world.add(Missile(x,y,dx,dy), layer.obstacle)




def crash(player, missile):
    p_box = player.get_hitbox()
    m_box = missile.get_hitbox()

    L, R, B, T = range(4)
    
    if p_box[L] < m_box[L] < p_box[R] or p_box[L] < m_box[R] < p_box[R]:
        if p_box[B] < m_box[T] < p_box[T] or p_box[B] < m_box[B] < p_box[T]:
            return True

    return False

def click(mouse, button):

    button_box = button.get_hitbox()

    L, R, B, T = range(4)

    if button_box[L] < mouse.x < button_box[R]:
        if button_box[B] < mouse.y < button_box[T]:
            return True

    return False

    
   
    
def enter():
    
    
    global p, bg, m, m_count, botton, o, center_missile
    game_world.init(layer.count)

    Player.life = 5
    Player.score = 0

    p = Player('./image/player.png')
    game_world.add(p,layer.player)

    o = Player('./image/other.png')
    game_world.add(o,layer.player)

    bg = Background('./image/background.png')
    game_world.add(bg, layer.bg)

    
    botton = startbotton(600,300)
    game_world.add(botton, layer.obstacle)

    center_missile = Missile(get_canvas_width()/2, get_canvas_height()/2,0,0)
    game_world.add(center_missile, layer.obstacle)

    


    paused()

def load_score():
    global scores
    
    file = open('./high_score.json', 'r')
    
    scores = json.load(file)

    file.close

    for s in scores:
        if Player.score > s["score"]:
            return 1
            break
    return 0


def exit():
    pass

def update():
    global p, state, center_missile, start, m_count

    m_count = 50 + Player.score // 5

    if state == STATE_INGAME:
    
        game_world.update()
        
        if game_world.get_layer_count(layer.obstacle) < m_count:
            create_missile()

        if game_world.get_layer_count(layer.obstacle) < m_count:
            create_missile()
        
        for i in game_world.objects[layer.obstacle]:
            if i.x > get_canvas_width() or i.x < 0:
                game_world.remove(i)
            if i.y > get_canvas_height() or i.y < 0:
                game_world.remove(i)
            
        for i in game_world.objects[layer.obstacle]:
            if crash(p, i) or crash(o, i):
                if i == center_missile:
                    center_missile = None
                Player.life -= 1
                
                game_world.remove(i)

        if Player.life <= 0:
            state = STATE_GAMEOVER
            if load_score() == 1:
                game_framework.change_state(high_score_state)
            else:
                game_framework.change_state(gameover_state)
      

        if center_missile == None:
            if start > 3:
                
                center_missile = Missile(get_canvas_width()/2, get_canvas_height()/2,0,0)
                game_world.add(center_missile, layer.obstacle)
                start = 0
            else:
                start += game_framework.frame_time
        


        
    
def draw():
    clear_canvas()
    game_world.draw()
    update_canvas()
    pass

def handle_events():
    global p, o, state, botton, state
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                game_framework.pop_state()
        if state == STATE_INGAME:
            if e.type == SDL_MOUSEMOTION:
                p.player_event(e)
                o.other_event(e)
                SDL_ShowCursor(SDL_DISABLE)
            
        if state == STATE_PAUSED:
            if e.type == SDL_MOUSEBUTTONDOWN:
                if click(e, botton):
                    state = STATE_INGAME
                    game_world.remove(botton)
                    p.player_event(e)
                    o.other_event(e)
                    SDL_ShowCursor(SDL_DISABLE)


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
