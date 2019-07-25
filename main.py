import map_generator
import potential
import numpy as np
from movement_cost import linear_cost, randomized_cost
from path_finding import PathFinder
from terrain_analysis import TerrainAnalyzer
from next_moves import adjacent_linear
from timeit import default_timer as timer

map_data = None


def is_valid_pos(cur_pos):
    x, y = cur_pos
    return 0 <= x < 100 and 0 <= y < 100 and map_data[y][x]


if __name__ == "__main__":
    map_data = map_generator.generate_map(100, 100, seed=25, obstacle_density=0.35)
    start = (59, 45)
    mid = (0, 0)
    end = (86, 40)
    waypoints = [start, mid, end]
    moves = adjacent_linear()
    cost_func = linear_cost()
    start = timer()
    path_finder = PathFinder(linear_cost(), linear_cost(), is_valid_pos)
    path, store = path_finder.find_path_waypoints(moves, waypoints, return_store=True)
    print(timer() - start)
    map_generator.view_path(map_data, path, store)
    start = timer()
    potn = potential.manhattan(map_data)
    print(timer() - start)
    potential.view_potential(potn)
    start = timer()
    terrainer = TerrainAnalyzer(map_data)
    print(timer() - start)
    terrainer.view_terrain(True)
