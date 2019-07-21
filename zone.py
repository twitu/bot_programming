import numpy as np
import matplotlib.pyplot as plt


def view_zones(zone_map):
    """View the zone map
    a) zone_map:        Numpy ndarray. Contains zone ids of each point.
    """
    plt.imshow(zone_map)
    plt.colorbar()
    plt.show()


def zone_generate(map_data, dist_function, zone_size=10, seed=None):
    """Generate zones for the map. TODO: (BROKEN).
    a) map_data:        Boolean numpy array. True for passable, False for impassable.
    b) dist_function:   Distance function from movement_cost.py.
    c) zone_size:       Zone size (int).
    d) seed:            Randomization seed (int).
    e) return value:    Numpy ndarray. Contains zone ids of each point.
    """
    # Initialize seed
    if seed is not None:
        np.random.seed(seed)

    # Package all points
    y, x = map_data.shape
    x = range(0, x)
    y = range(0, y)
    [x, y] = np.meshgrid(x, y)
    x = np.ndarray.flatten(x)
    y = np.ndarray.flatten(y)
    points = list(zip(x, y))

    # Remove impassables
    i = 0
    while i != len(points):
        x, y = points[i]
        if not map_data[y][x]:
            del points[i]
        else:
            i += 1

    # Build the zones
    zone_map = np.multiply(-1, map_data)
    zone_id = 0
    while points:
        zone_id += 1
        i = np.random.randint(0, len(points))
        flood_fill(zone_map, map_data, zone_id, points[i], points[i], dist_function, zone_size, points)
    return zone_map


def flood_fill(zone_map, map_data, zone_id, current, center, dist_function, zone_size, points):
    """Recursively flood fill a given region with a given zone id.
    a) zone_map:        Mutable numpy ndarray. Contains zone ids of each point.
    b) map_data:        Boolean numpy array. True for passable, False for impassable.
    c) zone_id:         Id of current zone (int).
    d) current:         Current point being processed (int, int).
    e) center:          Zone center point (int, int).
    f) dist_function:   Distance function from movement_cost.py.
    g) zone_size:       Zone size (int).
    h) points:          List of remaining points to process. (list((int, int))).
    """
    x, y = current
    m, n = map_data.shape
    dist = dist_function(current, center)
    if x < 0 or x >= n or y < 0 or y >= m or not map_data[y][x] or zone_map[y][x] != -1 or dist > zone_size:
        return
    else:
        zone_map[y][x] = zone_id
        points.remove(current)
        flood_fill(zone_map, map_data, zone_id, (current[0], current[1] + 1), center, dist_function, zone_size, points)
        flood_fill(zone_map, map_data, zone_id, (current[0], current[1] - 1), center, dist_function, zone_size, points)
        flood_fill(zone_map, map_data, zone_id, (current[0] + 1, current[1]), center, dist_function, zone_size, points)
        flood_fill(zone_map, map_data, zone_id, (current[0] - 1, current[1]), center, dist_function, zone_size, points)
    return
