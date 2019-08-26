from helper import get_x_and_y_from_store
from helper import get_x_and_y_from_path
from point import Point

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import perlin

def view_map(map_data, stores=None, paths=None, points=None, grid=True):
    """
    View map with entities like paths, stores, and points. Each
    entity argument is a list and the z-order (visibility) increases
    with index in the list. Among entities z-order varies as
    stores < paths < points.

    The map shows passable as yellow and impassable as purple. Each
    entity list cycles through an indepedent color map, i.e. each
    path in paths will have a different color. All points are
    displayed in black color.

    Args:
        map_data:    Boolean numpy array. True for passable, False
            for impassable.
        coordinates: click anywhere on the map to view coordinates
            of that point.
        paths:       List of paths to be shown.
        stores:      Point stores to be shown.
        points:      Special points to be displayed.
        grid:        Display grid. Defaults to True.
    """

    if stores:
        colors = cm.autumn(np.linspace(0, 1, len(stores)))
        for c, store in zip(colors, stores):
            x, y = get_x_and_y_from_store(store)
            plt.scatter(x, y, color=c)

    if paths:
        colors = cm.winter(np.linspace(0, 1, len(paths)))
        for c, path in zip(colors, paths):
            start, end = path[0], path[-1]
            x, y = get_x_and_y_from_path(path)
            plt.scatter(x, y, color=c)
            plt.plot(start.x, start.y, marker='x')
            plt.plot(end.x, end.y, marker='x')

    if points:
        for point in points:
            plt.plot(point.x, point.y, color='black', marker='o')

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


if __name__ == "__main__":
    map_data = generate_map(100, 100, 0.35, 0.1, 25)
    offsets = []
    for i in range(3):
        for j in range(3):
            offsets.append(Point(i, j))

    store_1 = {Point(41, 25) + offset: True for offset in offsets}
    store_2 = {Point(42, 26) + offset: True for offset in offsets}
    path = [Point(41, 25), Point(41, 26), Point(41, 27), Point(42, 27), Point(43, 27)]
    point = Point(42, 37)
    view_map(map_data, [store_1, store_2], [path], [point])

