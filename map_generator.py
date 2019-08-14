from helper import get_x_and_y_from_store
from helper import get_x_and_y_from_path

import matplotlib.pyplot as plt
import numpy as np
import perlin


def view_map(map_data, grid=True):
    """View map
    a) map_data:    Boolean numpy array. True for passable, False for impassable.
    b) grid:        Display grid. Defaults to True.
    c) color code:  yellow for passable(1), purple for impassable(0).
    d) coordinates: click anywhere on the map to view coordinates of that point.
    """
    m, n = map_data.shape
    plt.imshow(map_data)
    plt.xticks(np.arange(0.5, n, 1.0), [])
    plt.yticks(np.arange(-0.5, m, 1.0), [])
    plt.grid(grid)
    plt.connect('button_press_event', mouse_move)
    plt.show()
    return


def view_path(map_data, path, store=None, grid=True, markers=False):
    """View path
    a) map_data:    Boolean numpy array. True for passable, False for impassable.
    b) path:        List[(int, int)]. List of points (x,y) in path from 0(start) to end(stop).
    c) grid:        Display grid. Defaults to True.
    d) markers:     Display bullet markers for points in path. Defaults to True.
    e) store:       Optionally pass store of points to print all points that were checked
                    while finding the correct path
    """
    # plot all the points in the store
    if store:
        x, y = get_x_and_y_from_store(store)
        plt.scatter(x, y, color='orange')
    # plot all the points in the path
    if path:
        start = path[0]
        end = path[-1]
        x, y = get_x_and_y_from_path(path)
        plt.plot(x, y, color='blue')
        if markers:
            plt.scatter(x, y, color='green')
        plt.plot(start.x, start.y, 'gx')
        plt.plot(end.x, end.y, 'rx')
        view_map(map_data, grid)
    else:
        print("Empty path")
    return


# noinspection PyTypeChecker
def generate_map(rows, cols, obstacle_density=0.35, var_index=0.1, seed=0):
    """Generate 2D map
    a) rows, cols:          No. of rows and columns.
    b) obstacle_density:    Percentage of map filled by obstacles. Defaults to 0.35.
    c) var_index:           Variability index. Controls "noisiness" of obstacles. Defaults to 0.1.
    d) seed:                Seed for rng. Use 0 for random seed. Defaults to 0.
    e) return value:        Boolean numpy array. True for passable, False for impassable.
    """
    y = np.linspace(0, cols * var_index, cols, endpoint=False)
    x = np.linspace(0, rows * var_index, rows, endpoint=False)
    x, y = np.meshgrid(x, y)
    map_data = perlin.perlin(x, y, seed=seed) + 0.5
    map_data = np.array(map_data > obstacle_density)
    return map_data


def mouse_move(event):
    """Show coordinates of selected point"""
    if event.xdata is None or event.ydata is None:
        return
    x, y = int(round(event.xdata)), int(round(event.ydata))
    print(x, y)
    return
