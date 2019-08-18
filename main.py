from timeit import default_timer as timer

import map_generator
from movement_cost import linear_cost
from moves import adjacent_linear
from path_finding import PathFinder
from point import Point
from game_map import Map

map_data = None


def is_valid_pos(cur_pos):
    x, y = cur_pos.x, cur_pos.y
    return 0 <= x < 100 and 0 <= y < 100 and map_data[y][x]


if __name__ == "__main__":
    map_data = map_generator.generate_map(100, 100, seed=25, obstacle_density=0.35)
    start = Point(35, 42)
    block = Point(39, 42)
    end = Point(41, 42)
    moves = adjacent_linear()
    cost_func = linear_cost()
    start = timer()
    path_finder = PathFinder(linear_cost(), linear_cost(), is_valid_pos)
    path, store = path_finder.find_path(moves, start, end, return_store=True)
    game_map = Map(map_data)
    game_map.dynamic = [Unit(TYPES['WALL'], block),]
    taken_path = []
    cur_unit = Unit(TYPES['SCOUT'], start)
    while True:
        next_step = path[0]
        cur_unit.cur_pos = next_step
        del path[0]
        if next_step == block:
            break
        else:
            taken_path.append(next_step)

    while not path:
        best_step = path_finder.best_potential_step(game_map, cur_unit, path)
        taken_path.append(best_step)
        cur_unit.cur_pos = best_step
        del path[0]

    map_generator.view_path(map_data, path)
    # start = timer()
    # potn = potential.manhattan(map_data)
    # print(timer() - start)
    # potential.view_potential(potn)
    # start = timer()
    # terrainer = TerrainAnalyzer(map_data)
    # print(timer() - start)
    # terrainer.view_terrain(True)
