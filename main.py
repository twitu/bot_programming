import map_generator
from movement_cost import linear_cost
from path_finding import PathFinder

map_data = None


def is_valid_pos(cur_pos):
    x, y = cur_pos
    return 0 <= x < 100 and 0 <= y < 100 and map_data[y][x]


if __name__ == "__main__":
    map_data = map_generator.generate_map(100, 100, seed=25)
    start = (0, 0)
    end = (99, 99)
    moves = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]
    path_finder = PathFinder(linear_cost(), linear_cost(), is_valid_pos)
    path = path_finder.find_path(moves, start, end)
    map_generator.view_path(map_data, path)

