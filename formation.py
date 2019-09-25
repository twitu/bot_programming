from itertools import cycle

from movement_cost import diagonal_cost
from moves import adjacent_octile
from path_finding import PathFinder


class Formation:

    def __init__(self, index, rel_pos, leader_index, units, is_valid_pos):
        self.index = index
        self.leader_index = leader_index
        self.units = units
        self.leader = units[leader_index]
        self.rel_pos = rel_pos
        self.turn_queue = cycle(units)
        self.is_valid_pos = is_valid_pos
        self.path_finder = PathFinder(diagonal_cost(), diagonal_cost(), self.is_valid_pos)
        self.leader_path = None
        self.moves = adjacent_octile()
        self.dest = None

    def update_units(self, units):
        """
        Update formation unit positions. Decentralized formation requires
        each unit to observe its neighbours and perform updates.

        Args:
            units (List[Unit]): List of units
        """
        self.units = units
        self.leader = units[self.leader_index]

    def init_dest(self, dest):
        """
        Initialize destination for formation. Find ideal path from
        leader to destination

        Args:
            dest (Point): destination point
        """
        self.dest = dest
        self.leader_path = self.path_finder.find_path(self.moves, self.leader, dest)

    def find_path(self, src, dest):
        """
        Use formation object find path to have similar configuration in all
        units

        Args:
            src (Point): source point
            dest (Point): destination point
        """
        return self.path_finder.find_path(self.moves, src, dest)

    def predict_pos_from(self, pos):
        """
        Predict position of unit from given point. Takes into account
        obstacles and impassable terrains and returns point closest to ideal
        position.

        Args:
            pos (Point): destination point
        """
        possible_pos = pos + self.rel_pos[self.index]
        store = self.path_finder.generic_a_star(self.moves, pos, possible_pos, 30)
        score_points = [(possible_pos.dist(pos), pos) for pos in store.keys()]
        return min(score_points)
