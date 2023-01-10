from pico2d import *

objects = []

def init(layer):
    global objects

    objects = []

    for i in range(layer):
        objects.append([])

def add(obj, layer):
    global objects

    objects[layer].append(obj)

def update():
    global objects

    for i in range(len(objects)):
        for obj in objects[i]:
            obj.update()


def draw():
    global objects

    for i in range(len(objects)):
        for obj in objects[i]:
            obj.draw()

def clear():
    global objects

    for i in range(len(objects)):
        for obj in objects[i]:
            del obj
    objects = []




def get_layer_count(layer):
    global objects

    return len(objects[layer])

def remove(obj):
    global objects
    for i in range(len(objects)):
        if obj in objects[i]:
            objects[i].remove(obj)
            del obj
            break

def get_layer_count(layer):
    return len(objects[layer])



    
