class Zone:
    def __init__(self, zone_id):
        """Create and initialize a new zone.
        a) zone_id:     Id of new zone
        """
        self.zone_id = zone_id
        self.points = []
        self.size = 0
