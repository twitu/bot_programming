from functools import partial

import math

from point import Point

"""
This module defines potential functions that give the potential at a given
destination point (dest). There are a few variations of potential functions
that include:
    - Potential w.r.t to the current point (cur_pos)
    - Potential fields that ignore cur_pos
    - Potential functions that are curried with argument, returning a
        function that only takes dest as argument
    - Potential maps that map offsets from cur_pos to potential values

Potential here is analogous to elelctro-static potential, i.e +ve potential
implies repulsion and -ve potential implies attraction.
"""


def inert_repel(cur_pos, dest):
    """
    Inert potential is analogous to a wall or a bad tile, that cannot be
    stepped on.

    Return:
        potential value

    """
    if dest == cur_pos:
        return math.inf
    return 0


def inert_repel_with(cur_pos):
    """
    Curry inert function with cur_pos.

    Return:
        function(dest): only requires dest argument to give potential value
    """
    return partial(inert_repel, cur_pos)


def linear_cutoff(cur_pos, cutoff, dest):
    """
    Potential degrades linearly from cutoff radius. Analogous to an enemy
    unit with cutoff being attack range for enemy unit

    Return:
        potential value
    """
    dist = cur_pos.dist(dest) - cutoff
    if dist < 0:
        return math.inf
    else:
        return max(4 - dist, 0)


def linear_cutoff_at(cur_pos, cutoff):
    """
    Curry linear cutoff function with cur_pos and cutoff

    Return:
        function(dest): only requires dest argument to give potential value
    """
    return partial(linear_cutoff, cur_pos, cutoff)


def decided_path_point(cur_pos, slope, index, dest):
    """
    Decided points on the path have -ve potential to attract. Potential
    of point on path increases the further it is down the path. Slope
    indicates rate of degrading influence.

    Return:
        potential value
    """
    dist = cur_pos.dist(dest)
    return min(-index - 4 + dist * slope, 0)


def decided_path(path, slope, dest):
    """
    Calculates sum of all points on path at dest. Uses decided_path_point
    to do so.

    Return:
        potential value
    """
    scores = [decided_path_point(point, slope, i, dest) for i, point in enumerate(path)]
    return min(scores)


def decided_path_at(path, slope):
    """
    Curries decided_path arguments

    Return:
        function(dest): gives potential at dest
    """
    return partial(decided_path, path, slope)


if __name__ == "__main__":
    from itertools import combinations

    origin = Point(0, 0)
    cur = Point(0, 0)
    dest = Point(1, 1)
    g = inert_repel_with(origin)
    for a, b in combinations([origin, cur, dest], 2):
        print(a, b)
        print(inert_repel(a, b))
        print(g(b))

    path = [Point(0, 0), Point(0, 1), Point(1, 1)]
    dest = Point(-1, -1)
    print(decided_path(path, -2, dest))
