class Map:

    def __init__(self, game_map):
        self.static = game_map
        self.active = []
        self.mock = []
        self.special = {}

    def is_valid_point(self, pos):
        return self.static[pos.y][pos.x]

    def valid_next_pos(self, cur_unit):
        return [pos for pos in cur_unit.next_pos() if self.is_valid_point(pos)]

    def visible_units(self, cur_unit):
        return [unit for unit in self.active if cur_unit.can_see(unit)]

    def _poten(self, next_pos, actors):
        poten = [0]*len(next_pos)

        for i, pos in enumerate(next_pos):
            for actor in actors:
                poten[i] += actor.poten_at(pos)

        return poten

    def mock_poten(self, next_pos):
        return self._poten(next_pos, self.mock)

    def active_poten(self, cur_unit, next_pos):
        active_units = self.visible_units(cur_unit)
        return self._poten(next_pos, active_units)

    def next_pos_potential(self, cur_unit, next_pos):
        mock_poten = self.mock_poten(next_pos)
        active_poten = self.active_poten(cur_unit, next_pos)
        # total_poten = [max(a, b) for a, b in zip(mock_poten, total_poten)]
        total_poten = [a + b for a, b in zip(mock_poten, active_poten)]
        return [(score, pos) for score, pos in zip(total_poten, next_pos)]

