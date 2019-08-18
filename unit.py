from collections import namedtuple
from potential_func import inert_repel, decided_path
from moves import adjacent_linear, bc19_9_radius

UnitProperty = namedtuple('UnitProperty', "pot_func next_moves move_cost_func sight_range")

TYPES = {
    'WALL': UnitProperty(inert_repel, None, None, None),
    'PATH': UnitProperty(decided_path, None, None, None),
    'SCOUT': UnitProperty(inert_repel, adjacent_linear(), None, bc19_9_radius),
}


class Unit:
    __slots__ = UnitProperty._fields + ('cur_pos',)

    def __init__(self, unit_type, cur_pos):
        self.cur_pos = cur_pos
        self.pot_func, self.next_moves, self.move_cost_func, self.sight_range = unit_type

    def next_pos(self):
        return [self.cur_pos + move for move in self.next_moves]

    def cur_sight(self):
        return [self.cur_pos + move for move in self.sight_range]

    def visible_from(self, other):
        return self.cur_pos in other.get_cur_sight()

    # TODO: simplify visible range as formula and remove multiple implementations
    def can_see_point(self, other_point):
        return other_point in self.cur_sight()

    def can_see(self, other):
        return other.cur_pos in self.cur_sight()

    def poten_at(self, point):
        return self.pot_func(self.cur_pos, point)


if __name__ == "__main__":
    for key in TYPES.keys():
        print(TYPES[key])
