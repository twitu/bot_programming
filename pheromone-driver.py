from pheromone import pheromone
import numpy as np
import moves
import random
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

# make sure directory exists

for turn in range(10):
    if(turn%1 == 0):
        # print("\n\n\n")
        # print(ph.map)
        addEnemy()
        ph.save_map("pheromone-sample/{}".format(turn))
    ph.propogate()
    

ph.save_map("pheromone-sample/{}".format(turn))