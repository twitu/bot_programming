import heapq

def path_from_start_to_end(start, end):
    """
    Takes start and end point and returns a list of points indicating path in the forward direction

    Args:
        start {x, y}: dictionary contains x and y coordinates of start point
        end   {x, y}: dictionary contains x and y coordinates of end point

    Return:
        List[int]: List of points to take to reach end in the forward direction
    """
    
