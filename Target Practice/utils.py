import pyglet
from pyglet import *

l, w = 500, 500

def drawTarget(l, w, batch):
    hold = []
    
    hold.append(shapes.Circle(l/2, w/2, 201, color=(0, 0, 0), batch = batch))
    hold.append(shapes.Circle(l/2, w/2, 199, color=(255, 255, 255), batch = batch))
    hold.append(shapes.Circle(l/2, w/2, 161, color=(0, 0, 0), batch = batch))
    hold.append(shapes.Circle(l/2, w/2, 159, color=(0, 255, 0), batch = batch))
    hold.append(shapes.Circle(l/2, w/2, 121, color=(0, 0, 0), batch = batch))
    hold.append(shapes.Circle(l/2, w/2, 119, color=(40, 40, 255), batch = batch))
    hold.append(shapes.Circle(l/2, w/2, 81, color=(0, 0, 0), batch = batch))
    hold.append(shapes.Circle(l/2, w/2, 79, color=(255, 40, 40), batch = batch))
    hold.append(shapes.Circle(l/2, w/2, 41, color=(0, 0, 0), batch = batch))
    hold.append(shapes.Circle(l/2, w/2, 39, color=(255, 255, 0), batch = batch))
    hold.append(shapes.Circle(l/2, w/2, 6, color=(0, 0, 0), batch = batch))
    hold.append(shapes.Circle(l/2, w/2, 5, color=(0, 255, 0), batch = batch))
    hold.append(shapes.Circle(l/2, w/2, 1, color=(0, 0, 0), batch = batch))
    
    return hold