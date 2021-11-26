import pyglet
import random as r
import utils as u
from pyglet import *

class AI:
    def __init__(self, x=None, y=None):
        self.x = x 
        self.y = y 
        self.fitness = 0
        self.bullethole = None
   
    def aimRandom(self):
        self.x = r.randint(0, u.l)
        self.y = r.randint(0, u.w)

    def shoot(self, batch):
        if self.x != None and self.y != None:
            self.bullethole = shapes.Circle(self.x, self.y, 3, color=(0, 0, 0), batch = batch)
            #print(f'Shot fired at {self.x}, {self.y}')
            return self.bullethole
    
    def evaluateFitness(self, centerX, centerY):
        worstFitness = centerX + centerY
        difX = abs(centerX - self.x)
        difY = abs(centerY - self.y)
        #self.fitness = 1 - (((difX/centerX) + (difY/centerY)) / 2)
        self.fitness = worstFitness - (difX + difY)
        #print(f'self fitness: {self.fitness}x:{self.x} y:{self.y} max:{worstFitness}')
        #print(f'xdif:{difX} ydif:{difY}')
        return self.fitness

    def crossOver(self, parentA, parentB):
        self.x = (parentA.x + parentB.x)/2
        self.y = (parentA.y + parentB.y)/2
        self.evaluateFitness(u.l/2, u.w/2)

    def mutate(self, rate):
        selector = r.randint(0, 100)
        check = 100 - selector
        if rate > check:
            changeX = r.randint(-50, 50)
            changeY = r.randint(-50, 50)
            self.x += changeX
            self.y += changeY
            self.evaluateFitness(u.l/2, u.w/2)
            