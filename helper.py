def add_tuple_elements(a, b):
    return a[0] + b[0], a[1] + b[1]


def scale_tuple_elements(a, p):
    return a[0] * p, a[1] * p


def get_neighbors(point, map_size):
    m, n = map_size
    nbors = [(point[0] + 1, point[1] + 1),
             (point[0] + 1, point[1]),
             (point[0] + 1, point[1] - 1),
             (point[0], point[1] + 1),
             (point[0], point[1] - 1),
             (point[0] - 1, point[1] + 1),
             (point[0] - 1, point[1]),
             (point[0] - 1, point[1] - 1),]
    i = 0
    while i != len(nbors):
        if nbors[i][0] < 0 or nbors[i][0] >= n or nbors[i][1] < 0 or nbors[i][1] >= m:
            nbors.remove(nbors[i])
        else:
            i += 1
    return nbors
