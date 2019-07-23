import next_moves

from itertools import tee

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def add_tuple_elements(a, b):
    return a[0] + b[0], a[1] + b[1]

def scale_tuple_elements(a, p):
    return a[0] * p, a[1] * p

def get_next_positions(point, moves):
    return [add_tuple_elements(point, move) for move in moves]

def get_neighbors(point, map_size):
    m, n = map_size
    octile_moves = next_moves.adjacent_octile()
    nbors = get_next_positions(point, octile_moves)

    def is_valid(point):
        x, y = point
        return not (x < 0 or x >= n or y < 0 or y >= m)

    selected_nbors = [point for point in nbors if is_valid(point)]
    return selected_nbors

