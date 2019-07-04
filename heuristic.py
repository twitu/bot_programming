import math

# heuristic functions

def linear_heuristic(start, end):
    """
    Manhattan distance, only linear movement is allowed

    Args:
        start {x, y}: dictionary contains x and y coordinates of start point
        end   {x, y}: dictionary contains x and y coordinates of end point

    Returns:
        (int): Returns Manhattan (linear) distance between start and end point
    """
    delta_x = math.abs(start['y'] - end['y'])
    delta_y = math.abs(start['y'] - end['y'])
    return delta_x + delta_y 

def euclidean_heuristic(start, end):
    """
    Euclidean distance, linear and diagonal movement is allowed,
    cost of diagonal movement is calculated using square root method

    Args:
        start {x, y}: dictionary contains x and y coordinates of start point
        end   {x, y}: dictionary containing x and y coordinates of end point

    Returns:
        (int): Returns euclidean distance between start and end point
    """
    delta_x = math.abs(start['x'] - end['x']) 
    delta_y = math.abs(start['y'] - end['y'])
    return math.sqrt(delta_x*delta_x + delta_y*delta_y)

def diagonal_heuristic(start, end):
    """
    Diagonal distance, 8 directions.
    Linear and diagonal movement is allowed at same cost 

    Args:
        start {x, y}: dictionary contains x and y coordinates of start point
        end   {x, y}: dictionary containing x and y coordinates of end point

    Returns:
        (int): Returns diagonal distance between start and end point
    """
    delta_x = math.abs(start['x'] - end['x']) 
    delta_y = math.abs(start['y'] - end['y'])
    return delta_x + delta_y - min(delta_x, delta_y)

