from collections import namedtuple
from potential_func import inert_repel, decided_path
from moves import adjacent_linear, bc19_9_radius

class Unit:

    def __init__(self, cur_pos, poten_func, next_moves, move_cost_func, sight_range):
        self.cur_pos = cur_pos
        self.poten_func = poten_func
        self.next_moves = next_moves
        self.move_cost_func = move_cost_func
        self.sight_range = sight_range

    def copy(self, cur_pos):
        if not cur_pos:
            cur_pos = self.cur_pos
        return Unit(cur_pos, self.poten_func, self.next_moves, self.move_cost_func, self.sight_range)

    def next_pos(self):
        return [self.cur_pos + move for move in self.next_moves]

    def cur_sight(self):
        return [self.cur_pos + move for move in self.sight_range]

    def visible_from(self, other):
        return self.cur_pos in other.cur_sight()

    def can_see_point(self, other_point):
        return other_point in self.cur_sight()

    def can_see(self, other):
        return other.cur_pos in self.cur_sight()

    def poten_at(self, point):
        return self.poten_func(self.cur_pos, point)

# Sample units
SCOUT = Unit(None, inert_repel, adjacent_linear(), None, bc19_9_radius())

