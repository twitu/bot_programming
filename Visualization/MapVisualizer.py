import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib as mpl
import numpy as np


def saveColorGradedMap(name,map,color='Reds',maxRange=1.0,minRange=0.0,underRange=(0.,0.,0.),overRange=(1.,1.,1.)):
    norm = mpl.colors.Normalize(vmin=minRange, vmax=maxRange)
    cmap = mpl.cm.get_cmap(color)
    cmap.set_under(underRange)
    cmap.set_over(overRange)

    fig, ax = plt.subplots()
    ax.imshow(map, cmap=cmap, norm=norm)
    # draw gridlines
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
    ax.set_xticks(np.arange(-0.5, map.shape[0], 1))
    ax.set_yticks(np.arange(-0.5, map.shape[1], 1))
    plt.savefig(name + ".png")
    plt.close(fig)