import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib as mpl
from point import Point
class pheromone(object):
    def __init__(self,obstacleData,possible_moves,decayRate = 0.7,dropOff = 0.1):
        # initialize map size of obstacles and set obstacles position as -1
        self.map = np.zeros(shape = obstacleData.shape, dtype = np.float32) - obstacleData
        self.obstacleData = obstacleData
        self.dropOff = dropOff
        self.moves = possible_moves
        self.moves.append(Point(0,0))
        self.multiplier = (1 - decayRate) #normalize
        self.temp = np.zeros(shape = self.map.shape,dtype = np.float32)
        self.cmap = mpl.cm.Reds
        self.cmap.set_under((0.,0.,1.))
        self.norm = mpl.colors.Normalize(vmin=0, vmax=1)
        return

    def addEnemy(self,x,y):
        self.map[x][y] = 1.0
        

    def decay(self):
        self.map = self.map*self.multiplier

    def propogate(self):
        for i,rows in enumerate(self.map):
            for j,value in enumerate(rows):
                if value > self.dropOff:
                    self.propogate_point(value,i,j)
                
        self.map = self.temp - self.obstacleData
        self.temp = np.zeros(shape = self.map.shape,dtype = float)


    def propogate_point(self,value,x,y):
        delta = 0
        changes = []
        for move in self.moves:
            finalx = x + move.x
            finaly = y + move.y
            if(finalx >= 0 and finalx < self.map.shape[0]):
                if(finaly >= 0 and finaly < self.map.shape[1]):
                    if(self.obstacleData[finalx][finaly] == False):
                        changes.append((finalx,finaly))

        delta = (value * self.multiplier)/len(changes)
        for pos in changes:
            self.temp[pos[0]][pos[1]] +=delta


    def save_map(self,name):
        fig, ax = plt.subplots()
        ax.imshow(self.map, cmap=self.cmap, norm=self.norm)
        # draw gridlines
        ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
        ax.set_xticks(np.arange(-0.5, self.map.shape[0], 1));
        ax.set_yticks(np.arange(-0.5, self.map.shape[1], 1));
        plt.savefig(name + ".png")
        plt.close(fig)
