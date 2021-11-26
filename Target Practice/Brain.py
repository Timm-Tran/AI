import pyglet
import random as r
import time
import utils
from AI import *

class Brain:

    def __init__(self):
        self.AIs = []
        self.fitnessValues = []
    
    def createAI(self, xpos, ypos):
        a = AI(xpos, ypos)
        a.evaluateFitness(u.l/2, u.w/2)
        self.AIs.append(a)
        self.fitnessValues.append(a.fitness)
        
    
    def generatePop(self, size = 0):
        
        for i in range(size):
            self.AIs.append(AI())
            self.AIs[i].aimRandom()
            self.fitnessValues.append(self.AIs[i].evaluateFitness(utils.l/2, utils.w/2))
    
    def showPop(self, batch):
        if self.AIs is None:   
            return print('No AIs to show.')
        else:
            catch = []
            for v in self.AIs:
                catch.append(v.shoot(batch))
            
            return catch
    
    def showFitness(self):
        if self.AIs is None:
            return print('No AIs to show.')

        if not self.fitnessValues: 
            print (self.fitnessValues)
 
    def selectionFPS(self):
        if self.fitnessValues:
            #print(f'list of fitness values: {self.fitnessValues}')
            parents = []
            for fit in self.fitnessValues:
                parents.append(0)
            
            nextGen = []
            nextGenFitness = []
            
            total = sum(self.fitnessValues)
            current = total
            parentA = None
            parentB = None
            
            for i, AIs in enumerate(self.AIs):
                selA = round(r.uniform(0, total), 2) + .01
                selB = round(r.uniform(0, total), 2) + .01
                for i, aiFit in enumerate(self.fitnessValues):
                    current -= aiFit
                    if selA >= current and parentA is None:
                        parentA = self.AIs[i]
                        parents[i] += 1
                    if selB >= current and parentB is None:
                        parentB = self.AIs[i]
                        parents[i] += 1
                    if parentA and parentB:
                        child = AI()
                        child.crossOver(parentA, parentB)
                        nextGen.append(child)
                        nextGenFitness.append(child.fitness)
                        break
                current = total
                parentA = None
                parentB = None
            
            print(self.fitnessValues)
            self.AIs = nextGen
            self.fitnessValues = nextGenFitness
            nextGen = []
            nextGenFitness = []
        print(parents)    
    
    def mutateAIs(self, rate):
        if rate > 100 or rate < 0:
            return print('Mutation rate out of bounds, failed.')
        
        else:
            for ai in self.AIs:
                ai.mutate(rate)