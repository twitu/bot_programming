from helper import get_x_and_y_from_itr
from itertools import cycle

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm
import matplotlib.colors as colors
import numpy as np
import itertools


def animate_game_state(game_map, frames=10, grid=True):

    fig = plt.figure()
    fig.set_size_inches(12, 12, True)
    ax = plt.axes()
    active_scatter = None
    mock_scatter = None
    turn_queue = cycle(game_map.active)

    # show active units
    unit_points = [game_unit.cur_pos for game_unit in game_map.active]
    x, y = get_x_and_y_from_itr(unit_points)
    colors = np.arange(len(unit_points))
    active_scatter = ax.scatter(x, y, c=colors)

    # show map with static passable and impassable terrain
    map_data = game_map.static
    m, n = map_data.shape
    im = plt.imshow(map_data)
    plt.xticks(np.arange(0.5, n, 1.0), [])
    plt.yticks(np.arange(-0.5, m, 1.0), [])
    plt.grid(grid)
    fig.canvas.draw()

    def update_plot(i):
        # pass cur unit game state information and make turn
        cur_unit = next(turn_queue)
        cur_unit.update_pos()

        # update active units positions
        unit_points = [game_unit.cur_pos for game_unit in game_map.active]
        x, y = get_x_and_y_from_itr(unit_points)
        units_pos = np.c_[x, y]
        active_scatter.set_offsets(units_pos)
        return active_scatter,

    return animation.FuncAnimation(fig, update_plot, frames=frames, blit=True)


def view_game_state(game_map, view_mock=False, grid=True):
    """
    Method shows current game state including static, active and mock points.
    Active points should have cur_pos, Mock objects should have a list of
    points, static is a 2D np array.

    Note: Mock objects have low opacity (alpha=0.3)

    Args:
        game_map (Map object)
        view_mock (Boolean): mock objects are shown if true
        grid (Boolean): True displays grid
    """
    # show active units
    unit_points = [game_unit.cur_pos for game_unit in game_map.active]
    x, y = get_x_and_y_from_itr(unit_points)
    colors = np.arange(len(unit_points))
    plt.scatter(x, y, c=colors)

    # show mock units if specified
    if view_mock:
        mock_objects = [game_mock.points for game_mock in game_map.mock]

        # each mock object is colored different but points for each object
        # are colored same
        colors = [len(obj) for obj in mock_objects]
        colors = [[i]*value for i, value in enumerate(colors)]
        colors = list(itertools.chain.from_iterable(colors))
        colors = np.array(colors)

        mock_objects = itertools.chain.from_iterable(mock_objects)
        x, y = get_x_and_y_from_itr(mock_objects)
        plt.scatter(x, y, c=colors, alpha=0.3)

    # show map with static passable and impassable terrain
    map_data = game_map.static
    m, n = map_data.shape
    plt.imshow(map_data)
    plt.xticks(np.arange(0.5, n, 1.0), [])
    plt.yticks(np.arange(-0.5, m, 1.0), [])
    plt.connect('button_press_event', mouse_move)
    plt.grid(grid)
    plt.show()


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
        paths:       List of paths to be shown.
        stores:      Point stores to be shown.
        points:      Special points to be displayed.
        grid:        Display grid. Defaults to True.

    Notes:
        coordinates: click anywhere on the map to view coordinates
            of that point.
    """

    if stores:
        colors = cm.autumn(np.linspace(0, 1, len(stores)))
        for c, store in zip(colors, stores):
            x, y = get_x_and_y_from_itr(store)
            plt.scatter(x, y, color=c)

    if paths:
        colors = cm.winter(np.linspace(0, 1, len(paths)))
        for c, path in zip(colors, paths):
            start, end = path[0], path[-1]
            x, y = get_x_and_y_from_itr(path)
            plt.scatter(x, y, color=c)
            plt.plot(start.x, start.y, marker='x')
            plt.plot(end.x, end.y, marker='x')

    if points:
        x = [point.x for point in points]
        y = [point.y for point in points]
        plt.scatter(x, y, color='black', marker='o')

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
        x, y = get_x_and_y_from_itr(store)
        plt.scatter(x, y, color='orange')
    # plot all the points in the path
    if path:
        start = path[0]
        end = path[-1]
        x, y = get_x_and_y_from_itr(path)
        plt.plot(x, y, color='blue')
        if markers:
            plt.scatter(x, y, color='green')
        plt.plot(start.x, start.y, 'gx')
        plt.plot(end.x, end.y, 'rx')
        view_map(map_data, grid)
    else:
        print("Empty path")
    return


def view_potential_field(potential, plot_type='colorgraded'):
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


def view_tactical_map(obj, grid=True, gates=True, graph=True):
    """View all zones in the terrain
    a) obj:             Terrain Analyzer type object.
    a) grid:            Boolean Value. Display grid?
    b) gates:           Boolean Value. Do you want to show the gates?
    c) graph:           Boolean Value. Plot connectivity graph?
    """
    plt.imshow(obj.zone_map)
    plt.colorbar()
    plt.xticks(np.arange(0.5, obj.map_size[1], 1.0), [])
    plt.yticks(np.arange(-0.5, obj.map_size[0], 1.0), [])
    plt.gca().set_xlim([-0.5, obj.map_size[1] - 0.5])
    plt.gca().set_ylim([-0.5, obj.map_size[0] - 0.5])
    plt.gca().invert_yaxis()
    plt.grid(grid)
    plt.connect('button_press_event', obj.mouse_move)
    if gates and obj.gate_points:
        x, y = zip(*obj.gate_points)
        plt.scatter(x, y, color='green')
    print(obj.zone_no, "zones found")
    x, y = zip(*[Z.center for Z in obj.zones])
    plt.scatter(x, y, edgecolors='white', color='red')
    if graph:
        for Z in obj.zones:
            p1 = Z.center
            for zone_id in Z.entry_points:
                p2 = obj.zones[zone_id].center
                plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color='white')
    plt.show()
    return


def mouse_move(event):
    """Show coordinates of selected point"""
    if event.xdata is None or event.ydata is None:
        return
    x, y = int(round(event.xdata)), int(round(event.ydata))
    print(x, y)
    return

def saveColorGradedMap(name,map,color='Reds',maxRange=1.0,minRange=0.0,underRange=(0.,0.,0.),overRange=(1.,1.,1.)):
    norm = colors.Normalize(vmin=minRange, vmax=maxRange)
    cmap = cm.get_cmap(color)
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