import map_generator
from game_map import Map
from mock_object import PathObject, WallObject
from movement_cost import linear_cost
from moves import adjacent_linear
from path_finding import PathFinder
from point import Point
from unit import SCOUT

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
    path_finder = PathFinder(linear_cost(), linear_cost(), is_valid_pos)
    path, store = path_finder.find_path(moves, start, end, return_store=True)
    game_map = Map(map_data)
    wall = WallObject([block])
    taken_path = []
    cur_unit = SCOUT.copy(start)
    while True:
        next_step = path[0]
        if next_step == block:
            break
        else:
            cur_unit.cur_pos = next_step
            del path[0]
            taken_path.append(next_step)

    while path:
        vis_path = [pos for pos in path if cur_unit.can_see_point(pos)]
        game_map.mock = [PathObject(vis_path), wall]
        best_step = path_finder.best_potential_step(game_map, cur_unit)
        taken_path.append(best_step)
        cur_unit.cur_pos = best_step
        del path[0]

    map_generator.view_map(map_data, None, [taken_path], [block])
