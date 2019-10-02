from collections import deque

from path_finding import PathFinder
from movement_cost import diagonal_cost, linear_cost
from moves import adjacent_linear, bc19_9_radius, adjacent_octile
from potential_func import inert_repel


# TODO: Create subclasses
class Unit:
    """
    Unit represents a movable entity with methods to calculate path,
    potential, visible units etc. For the unit single source of truth
    for the game world is game_map. Keeping a reference to the game_map
    object eliminates a lot of message passing about game state. Game_map
    object also makes it easy to use potential field based movement that
    depends on the game state. mock attribute can be changed, however changes to it will not be persistent
    over the turns as other units can empty and overwrite it.

    Note: However the unit must not change static and active attributes of the game_map.
    """

    def __init__(self, cur_pos, name, poten_func, next_moves, move_cost_func, sight_range):
        self.name = name
        self.cur_pos = cur_pos
        self.poten_func = poten_func
        self.next_moves = next_moves
        self.move_cost_func = move_cost_func
        self.sight_range = sight_range
        self.game_map = None
        self.path = None
        self.dest = None
        self.path_finder = None

    def set_game_state(self, game_map):
        self.game_map = game_map
        self.path_finder = PathFinder(self.move_cost_func, self.move_cost_func, self.game_map.is_valid_point)

    def find_path(self, dest):
        self.dest = dest
        self.path = deque(self.path_finder.find_path(self.next_moves, self.cur_pos, dest))

    def update_pos(self):
        if self.path:
            self.cur_pos = self.path.popleft()

    def copy(self, cur_pos):
        if not cur_pos:
            cur_pos = self.cur_pos
        return Unit(cur_pos, self.name, self.poten_func, self.next_moves, self.move_cost_func, self.sight_range)

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

    def __str__(self):
        return "{}: {}".format(self.name, self.cur_pos)

    def __repr__(self):
        return "{}: {}".format(self.name, self.cur_pos)


class FormationUnit(Unit):
    MAX_PREDICT = 5

    def __init__(self, *args):
        super().__init__(*args)
        self.is_leader = None
        self.formation = None
        self.leader_path = None
        self.path = None
        self.game_map = None

    def copy(self, cur_pos):
        if not cur_pos:
            cur_pos = self.cur_pos
        return FormationUnit(cur_pos, self.poten_func, self.next_moves, self.move_cost_func, self.sight_range)

    def add_to_formation(self, formation, is_leader):
        self.is_leader = is_leader
        self.formation = formation

    def set_dest(self, dest):
        self.formation.init_dest(dest)
        if self.is_leader:
            self.path = deque(self.formation.leader_path)
        else:
            self.leader_path = deque(self.formation.leader_path)

    def find_path(self):
        if len(self.leader_path) > FormationUnit.MAX_PREDICT:
            future_leader_pos = self.leader_path[FormationUnit.MAX_PREDICT]
        else:
            future_leader_pos = self.leader_path[-1]

        _, short_dest = self.formation.predict_pos_from(future_leader_pos)
        self.path = deque(self.formation.find_path(self.cur_pos, short_dest))

    def update_pos(self):
        if not self.path:
            self.find_path()

        self.leader_path.popleft()
        next_pos = self.path.popleft()
        if self.game_map.is_valid_pos(next_pos):
            self.cur_pos = next_pos
        else:
            self.cur_pos = next_pos

    def update_formation(self):
        leader_pos = self.leader_path[0]
        units = self.game_map.active
        self.formation.update_units(units, leader_pos)

    def __str__(self):
        return "{} {}: {}".format(self.name, self.formation.index, self.cur_pos)

    def __repr__(self):
        return "{} {}: {}".format(self.name, self.formation.index, self.cur_pos)


# Sample units
SCOUT = Unit(None, "Scout", inert_repel, adjacent_linear(), linear_cost(), bc19_9_radius())
FORMATION = FormationUnit(None, "Formation", None, adjacent_octile, diagonal_cost(), bc19_9_radius())
