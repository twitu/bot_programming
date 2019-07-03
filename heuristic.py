import math

# heuristic functions

def simple_heuristic(start, end):
    delta_x = math.abs(start['x'] - end['x']) 
    delta_y = math.abs(start['y'] - end['y'])
    return delta_x + delta_y 

# Also known as manhattan distance
# linear movement costs one unit
def linear_heuristic(start, end):
    delta_x = math.abs(start['x'] - end['x']) 
    delta_y = math.abs(start['y'] - end['y'])
    return math.sqrt(delta_x*delta_x + delta_y*delta_y)

# Also known as chebyshev heuristic
# all 8 directions have equal costs
def diagonal_heuristic(start, end):
    delta_x = math.abs(start['x'] - end['x']) 
    delta_y = math.abs(start['y'] - end['y'])
    return math.abs(delta_x, delta_y)
