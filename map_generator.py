import perlin
import numpy as np
import matplotlib.pyplot as plt

def view_map(map_data, grid = True):

    """View map
    a) map_data:    Boolean numpy array. True for passable, False for impassable.
    b) grid:        Display grid. Defaults to True.
    c) color code:  yellow for passable(1), purple for impassable(0).
    d) coordinates: click anywhere on the map to view coordinates of that point.
    """

    m, n = map_data.shape
    plt.imshow(map_data)
    plt.xticks(np.arange(0.5, n, 1.0), [])
    plt.yticks(np.arange(0.5, m, 1.0), [])
    plt.grid(grid)
    plt.connect('button_press_event', mouse_move)
    plt.show()
    return

def view_path(map_data, path, grid = True, markers = True):

    """View path
    a) map_data:    Boolean numpy array. True for passable, False for impassable.
    b) path:        List[(int, int)]. List of points (x,y) in path from 0(start) to end(stop).
    c) grid:        Display grid. Defaults to True.
    d) markers:     Display bullet markers for points in path. Defaults to True.
    e) color code:  As in view_map; plus green cross for start and red cross for destination.
    """

    x, y = zip(*path)
    plt.plot(x, y)
    plt.plot(x[0], y[0], 'gx')
    plt.plot(x[-1], y[-1], 'rx')
    if markers:
        plt.scatter(x, y)
    view_map(map_data, grid)
    return

def generate_map(rows, cols, obstacle_density = 0.35, var_index = 0.1, seed = 0):

    """Generate 2D map
    a) rows, cols:          No. of rows and columns.
    b) obstacle_density:    Percentage of map filled by obstacles. Defaults to 0.35.
    c) var_index:           Variability index. Controls "noisiness" of obstacles. Defaults to 0.1.
    d) seed:                Seed for rng.
    e) return value:        Boolean numpy array. True for passable, False for impassable.
    """

    y = np.linspace(0, cols*var_index, cols, endpoint = False)
    x = np.linspace(0, rows*var_index, rows, endpoint = False)
    x, y = np.meshgrid(x, y)
    map_data = perlin.perlin(x, y, seed = seed) + 0.5
    map_data = np.array(map_data > obstacle_density)
    return map_data

def mouse_move(event):
    """Show coordinates of selected point"""
    if event.xdata is None or event.ydata is None:
        return
    x, y = int(event.xdata), int(event.ydata)
    print(x, y)
    return
