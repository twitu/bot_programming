class Zone:
    def __init__(self, zone_id):
        """Create and initialize a new zone.
        a) zone_id:         Id of new zone.
        """
        self.zone_id = zone_id
        self.points = []
        self.size = 0
        self.center = (0, 0)
        self.entry_points = {}

    def update_center(self):
        """Update center to mean of points."""
        x, y = zip(*self.points)
        x = int(round(sum(x) / self.size))
        y = int(round(sum(y) / self.size))
        self.center = (x, y)
        return

    def add_gate_point(self, adj_zone_id, gate_point):
        """Add a gate point to an adjacent zone.
        a) adj_zone_id:     Id of adjacent zone.
        b) gate_point:      Coords (int, int) of gate point.
        """
        if adj_zone_id in self.entry_points:
            self.entry_points[adj_zone_id].append(gate_point)
        else:
            self.entry_points.update({adj_zone_id: [gate_point]})
        return
