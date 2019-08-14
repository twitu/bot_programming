from point import Point

import random


def adjacent_linear(randomize=False):
    """
    Return x and y offsets for adjacent moves in
    linear directions

                         #
                        #x#
                         #

    Args:
        randomize (boolean): randomize order of moves
            or not

    Returns:
        List (Point): List of point offsets from
        current position
    """
    moves = [
        Point(0, 1),
        Point(1, 0),
        Point(0, -1),
        Point(-1, 0)
    ]

    if randomize:
        return random.shuffle(moves)
    else:
        return moves


def adjacent_octile(randomize=False):
    """
    Return x and y offsets for adjacent moves in
    octile directions

                        ###
                        #x#
                        ###

    Args:
        randomize (boolean): randomize order of moves
            or not

    Returns:
        List (Point): List of point offsets from
        current position
    """
    moves = [
        Point(0, 1),
        Point(1, 0),
        Point(0, -1),
        Point(-1, 0),
        Point(1, 1),
        Point(1, -1),
        Point(-1, 1),
        Point(-1, -1)
    ]

    if randomize:
        return random.shuffle(moves)
    else:
        return moves


def bc19_4_radius(randomize=False):
    """
    Return x and y offsets for adjacent moves in
    four unit distance of the current position.

                         #
                        ###
                       ##x##
                        ###
                         #

    Args:
        randomize (boolean): randomize order of moves
            or not

    Returns:
        List (Point): List of point offsets from
        current position
    """
    moves = [
        Point(0, 1),
        Point(1, 0),
        Point(0, -1),
        Point(-1, 0),
        Point(1, 1),
        Point(1, -1),
        Point(-1, 1),
        Point(-1, -1),
        Point(2, 0),
        Point(0, 2),
        Point(0, -2),
        Point(-2, 0)
    ]

    if randomize:
        return random.shuffle(moves)
    else:
        return moves


def bc19_9_radius(randomize=False):
    """
    Return x and y offsets for adjacent moves in
    nine unit distance of the current position.

                         #
                        ###
                       #####
                      ###x###
                       #####
                        ###
                         #

    Args:
        randomize (boolean): randomize order of moves
            or not

    Returns:
        List (Point): List of point offsets from
        current position
    """
    moves = [
        Point(0, 1),
        Point(1, 0),
        Point(0, -1),
        Point(-1, 0),
        Point(1, 1),
        Point(1, -1),
        Point(-1, 1),
        Point(-1, -1),
        Point(2, 0),
        Point(0, 2),
        Point(0, -2),
        Point(-2, 0),
        Point(0, 3),
        Point(1, 2),
        Point(2, 1),
        Point(3, 0),
        Point(2, -1),
        Point(1, -2),
        Point(0, -3),
        Point(-1, -2),
        Point(-2, -1),
        Point(-3, 0),
        Point(-2, 1),
        Point(-1, 2),
        Point(2, 2),
        Point(2, -2),
        Point(-2, 2),
        Point(-2, -2)
    ]

    if randomize:
        return random.shuffle(moves)
    else:
        return moves


def adjacent_linear_directional(up_down=True):
    """
    Return x and y offsets for adjacent moves in
    one of the linear directions

                         o
                        #x#
                         o

    Args:
        up_down (boolean): returns moves for up down movement
            or left right movement

    Returns:
        List (Point): List of point offsets from
        current position
    """

    if up_down:
        return [Point(0, 1), Point(0, -1)]
    else:
        return [Point(1, 0), Point(-1, 0)]

