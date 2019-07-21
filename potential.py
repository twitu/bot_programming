import scipy.ndimage
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


def view_potential(potential, plot_type='colorgraded'):
    """View colorplot of potential field.
    a) potential:   Potential field.
    b) plot_type:   'colorgraded', '3d_surface' or 'contour'.
    """
    if plot_type == 'colorgraded':
        plt.imshow(potential)
        plt.colorbar()
        plt.show()
    elif plot_type == '3d_surface':
        plt.figure()
        ax = plt.axes(projection="3d")
        y, x = potential.shape
        x = range(0, x)
        y = range(0, y)
        x, y = np.meshgrid(x, y)
        ax.plot_surface(x, y, potential, rstride=1, cstride=1, cmap='winter', edgecolor='none')
        plt.gca().invert_yaxis()
        plt.show()
    elif plot_type == 'contour':
        y, x = potential.shape
        x = range(0, x)
        y = range(0, y)
        x, y = np.meshgrid(x, y)
        plt.contour(x, y, potential)
        plt.gca().invert_yaxis()
        plt.show()
    return


def obstacle(map_data, d0=2, nu=800, scale=100):
    """Generate obstacle field.
    a) map_data:        Boolean numpy array. True for passable, False for impassable.
    b) d0:              Parameter 1. Fall off.
    c) nu:              Parameter 2. Potential height.
    d) scale:           Parameter 3. Scale. Similar to fall off.
    e) return value:    Numpy ndarray for potential height.
    """
    d = scipy.ndimage.distance_transform_edt(map_data)
    d2 = d / scale + 1
    potn = nu * np.square(np.divide(1, d2) - 1 / d0)
    return potn


def goalpost(map_size, goal, xi=1 / 700):
    """Generate attractive field.
    a) map_size:        Size of map in (m, n). Use map_data.shape
    b) goal:            Target destination (int, int).
    c) xi:              Parameter. Attractive force.
    e) return value:    Numpy ndarray for potential height.
    """
    potn = np.zeros(map_size)
    m, n = map_size
    for y in range(0, m):
        for x in range(0, n):
            potn[y][x] = xi * ((x - goal[0]) * (x - goal[0]) + (y - goal[1]) * (y - goal[1]))
    return potn
