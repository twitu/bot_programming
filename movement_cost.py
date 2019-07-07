import random

import math


def linear_cost(start, end, cost=1):
    """
    Manhattan distance, only linear movement is allowed

    Args:
        start (int, int): x and y coordinates of start point
        end   (int, int): x and y coordinates of end point
        cost       (int): cost of one step

    Returns:
        Linear cost between start and end point
    """

    delta_x = abs(start[0] - end[0])
    delta_y = abs(start[1] - end[1])
    return (delta_x + delta_y) * cost


def euclidean_cost(start, end, cost=1):
    """
    Euclidean distance, linear and diagonal movement is allowed,
    cost of diagonal movement is calculated using square root method

    Args:
        start (int, int): x and y coordinates of start point
        end   (int, int): x and y coordinates of end point
        cost  (int): cost of one step

    Returns:
        Euclidean cost between start and end point
    """

    delta_x = abs(start[0] - end[0])
    delta_y = abs(start[1] - end[1])
    return math.sqrt(delta_x * delta_x + delta_y * delta_y) * cost


def diagonal_cost(start, end, lin=1, diag=1):
    """
    Diagonal distance, 8 directions.
    Linear and diagonal movement is allowed at same cost
    For lin = 1 and diag = 1, gives octile distance
    For lin = 1 and diag = root 2, gives triangle distance

    Args:
        start (int, int): x and y coordinates of start point
        end   (int, int): x and y coordinates of end point
        lin          int: cost of one linear step
        diag         int: cost of one diagonal step

    Returns:
        Diagonal cost between start and end point
    """

    delta_x = abs(start[0] - end[0])
    delta_y = abs(start[1] - end[1])
    return (delta_x + delta_y) * lin + min(delta_x, delta_y) * (diag - 2 * lin)


def scaled_cost(h_func, p_scale, *args):
    """
    Scales cost function based on given parameter

    Args:
        h_func: cost function
        p_scale: scales cost function multiple times
        *args: arguments passed to cost function

    Returns:
        Scaled value of cost cost
    """

    return h_func(*args) * p_scale


def randomized_cost(sigma, mu, h_func, *args):
    """
    Generates random number with normal distribution based on given sigma and mu.
    Scales cost function by generated random number. Suggested values are
    mu = 1 and 0.2 < mu < 0.3, for realistic paths.

    Args:
        sigma: standard deviation in normal distribution
        mu: average value in normal distribution
        h_func: cost function
        *args: arguments passed to cost function

    Returns:
        Randomly scaled value of cost cost
    """

    return h_func(*args) * random.normalvariate(mu, sigma)
