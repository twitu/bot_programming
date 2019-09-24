from pheromone import pheromone
import numpy as np
import moves
import random
from Visualization.MapVisualizer import saveColorGradedMap

np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

def getObstacleData(size,prob):
    return np.random.choice(a=[False, True], size=(size,size), p=[1-prob, prob])

def addEnemy():
    x = random.randint(0,19)
    y = random.randint(0,19)
    print("Enemy added:" ,x, y)
    ph.addEnemy(x,y)

obstacles = getObstacleData(20,0.1)
ph = pheromone(obstacles,moves.adjacent_octile(),decayRate=0,dropOff=0.0)

for i in range(40):
        addEnemy()



for turn in range(10):
    if(turn%1 == 0):
        addEnemy()
        # TODO: make sure directory exists
        saveColorGradedMap("pheromone-sample/{}".format(turn),ph.map,underRange=(0.,0.,1.))
    ph.propogate()
    

