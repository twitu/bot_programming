from collections import namedtuple

import math

class Point(namedtuple('Point', ['x', 'y'])):
    __slots__ = ()

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __le__(self, other):
        if self.x - other.x <= 0:
            return True
        elif self.y - other.y <= 0:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.x - other.y < 0:
            return True
        elif self.x - other.y > 0:
            return False
        elif self.y - other. y < 0:
            return True
        else:
            return False

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def dist(self, other, squared=True):
        dist_squared = (self.x - other.x)**2 + (self.y - other.y)**2
        if squared:
            return dist_squared
        else:
            return math.sqrt(dist_squared)

