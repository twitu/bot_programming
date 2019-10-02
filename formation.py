from itertools import cycle

from movement_cost import diagonal_cost
from moves import adjacent_octile
from path_finding import PathFinder


class Formation:
    """
    Formation represents a group of units that move together. The leader position
    can be any unit and does not need to be centered on any particular unit. All
    units move relative to the leader position which advances one step towards
    destination on each turn.
    """

    def __init__(self, index, rel_pos, leader_pos, units, is_valid_pos):
        """
        Formation object is unique to each unit.

        Args:
            index (int): index of unit in position list
            rel_pos (List[Point]): relative position of other units to leader_pos
            leader_pos (Point): leader position
            units (List[Point]): unit positions
            is_valid_pos (func): function to determine if postion is valid
        """
        self.index = index
        self.units = units
        self.leader = leader_pos
        self.rel_pos = rel_pos
        self.is_valid_pos = is_valid_pos
        self.path_finder = PathFinder(diagonal_cost(), diagonal_cost(), self.is_valid_pos)
        self.moves = adjacent_octile()
        self.dest = None

    def update_units(self, units, leader_pos):
        """
        Update formation unit positions. Decentralized formation requires
        each unit to observe its neighbours and perform updates.

        Note: Should only be called when leader_path is not empty

        Args:
            units (List[Unit]): List of units
            leader_pos (Point): Leader position
        """
        self.units = units
        self.leader = leader_pos

    def init_dest(self, dest):
        """
        Initialize destination for formation. Find ideal path from
        leader to destination

        Args:
            dest (Point): destination point
        """
        self.dest = dest
        return self.path_finder.find_path(self.moves, self.leader, dest)

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
        if score_points:
            return min(score_points)[1]
        else:
            return None