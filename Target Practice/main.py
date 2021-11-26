from pyglet.window import *
from pyglet.gl import *
from pyglet import shapes
from AI import *
from Brain import *
import utils
import time


def main():

    #init the game window/batch, set background to white, draw target
    window = pyglet.window.Window(utils.l, utils.w, caption='Target Practice AI')
    batch = pyglet.graphics.Batch()
    target = utils.drawTarget(utils.l, utils.w, batch)
    glClearColor(255, 255, 255, 1)   
    
    brain = Brain()
    brain.generatePop(100)
    
    @window.event
    def on_draw():
        aiShots = brain.showPop(batch)
        window.clear()
        batch.draw()


    @window.event
    def on_key_press(button, modifiers):
        if button == key.F:
            brain.selectionFPS()
            brain.mutateAIs(5)


    pyglet.app.run()

if __name__ == '__main__':
    main()