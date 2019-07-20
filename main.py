import map_generator
import potential
from movement_cost import linear_cost, randomized_cost
from path_finding import PathFinder

map_data = None


def is_valid_pos(cur_pos):
    x, y = cur_pos
    return 0 <= x < 100 and 0 <= y < 100 and map_data[y][x]


if __name__ == "__main__":
    map_data = map_generator.generate_map(100, 100, seed=25)
    start = (59, 45)
    end = (86, 40)
    moves = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]
    cost_func = linear_cost()
    path_finder = PathFinder(linear_cost(), randomized_cost(1, 0.2, cost_func), is_valid_pos)
    path, store = path_finder.find_path_return_store(moves, start, end)
    map_generator.view_path(map_data, path, store)
    potential.view_potential(potential.obstacle(map_data))
