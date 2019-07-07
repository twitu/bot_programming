import random

import math


def linear_cost(scale=1):
    """
    Manhattan distance, only linear movement is allowed

    Args:
        start (int, int): x and y coordinates of start point
        end   (int, int): x and y coordinates of end point
        scale       (int): scale of one step

    Returns:
        Returns linear cost function between start and end point
    """

    def cost(start, end):
        delta_x = abs(start[0] - end[0])
        delta_y = abs(start[1] - end[1])
        return (delta_x + delta_y) * scale

    return cost


def euclidean_cost(scale=1):
    """
    Euclidean distance, linear and diagonal movement is allowed,
    cost of diagonal movement is calculated using square root method

    Args:
        start (int, int): x and y coordinates of start point
        end   (int, int): x and y coordinates of end point
        scale  (int): scale of one step

    Returns:
        Returns euclidean cost fuction between start and end point
    """

    def cost(start, end):
        delta_x = abs(start[0] - end[0])
        delta_y = abs(start[1] - end[1])
        return math.sqrt(delta_x * delta_x + delta_y * delta_y) * scale

    return cost


def diagonal_cost(lin=1, diag=1):
    """
    Diagonal distance, 8 directions.
    Linear and diagonal movement is allowed at same cost
    For lin = 1 and diag = 1, gives octile distance
    For lin = 1 and diag = root 2, gives triangle distance

    Args:
        start (int, int): x and y coordinates of start point
        end   (int, int): x and y coordinates of end point
        lin          int: scale of one linear step
        diag         int: scale of one diagonal step

    Returns:
        Returns diagonal cost function between start and end point
    """

    def cost(start, end):
        delta_x = abs(start[0] - end[0])
        delta_y = abs(start[1] - end[1])
        return (delta_x + delta_y) * lin + min(delta_x, delta_y) * (diag - 2 * lin)

    return cost


def scaled_cost(h_func, p_scale):
    """
    Scales cost function based on given parameter

    Args:
        h_func: cost function
        p_scale: scales cost function multiple times

    Returns:
        Scaled cost function
    """

    def cost(start, end):
        return h_func(start, end) * p_scale

    return cost


def randomized_cost(sigma, mu, h_func):
    """
    Generates random number with normal distribution based on given sigma and mu.
    Scales cost function by generated random number. Suggested values are
    mu = 1 and 0.2 < mu < 0.3, for realistic paths.

    Args:
        sigma: standard deviation in normal distribution
        mu: average value in normal distribution
        h_func: cost function

    Returns:
        Randomly scaled cost function
    """

    def cost(start, end):
        return h_func(start, end) * random.normalvariate(mu, sigma)

    return cost
