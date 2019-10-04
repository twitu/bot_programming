import math


class PathObject:
    """
    Path points attract a point with degrading field upto
    a certain cutoff. The field strength increases with
    increasing index along the path.
    """

    def __init__(self, points):
        self.points = points

    def poten_at(self, pos, slope=-2, cutoff=4):
        """
        Calculate potential at point pos

        Args:
            pos: point to calculate potential at
            slope: slope of degrading field
            cutoff: maximum range of affect for field

        Returns:
            value: minimum potential value possible
        """

        def score(path_point, i, pos):
            dist = pos.dist(path_point)
            if dist == 0:
                return -math.inf
            else:
                return (i + 1) * ((1 / dist - 1 / cutoff) * (slope - i))

        scores = [score(path_point, i, pos) for i, path_point in enumerate(self.points)]
        return min(scores)


class WallObject:
    """
    Wall objects behave as inert tiles, not allowing
    any unit to step on them while not affecting any other tile
    """

    def __init__(self, points):
        self.points = points

    def poten_at(self, pos):
        """
        Inert function stepping on wall in not possible. No other
        point is affected.

        Args:
            pos: point to calculate potential at

        Returns:
            value: inf or 0
        """
        if pos in self.points:
            return math.inf
        else:
            return 0

class EnemyObject:
    """
    Enemy objects exert a attraction/repulsion based on the proximity/probability of enemies 
    Enemy objects can be initialized so that they can either attract or repel based on multiplier (default:repel)
    """

    def __init__(self, pheromone, multiplier=1):
        self.pheromone = pheromone
        self.multiplier = multiplier

    def poten_at(self, pos):
        """
        Get enemy proximity 

        Args:
            pos: point to calculate potential at

        Returns:
            value: potential due to enemies
        """
        return (self.pheromone.map[pos.y][pos.x] + self.pheromone.obstacleData[pos.y][pos.x])*self.multiplier
        
