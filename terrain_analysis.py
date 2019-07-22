import matplotlib.pyplot as plt
from potential import manhattan
from helper import get_neighbors


class TerrainAnalyzer:
    def __init__(self, map_data):
        """Create and initialize Terrain Analyzer.
        a) map_data:        Boolean numpy array. True for passable, False for impassable.
        """
        self.map_data = map_data
        self.map_size = map_data.shape
        self.height_map, self.height_vector = manhattan(map_data, True)
        self.max_height = len(self.height_vector)
        self.zone_map = map_data * 0
        self.zone_no = 0
        self.gate_points = []
        self.water_level_decomposition()
        return

    def view_terrain(self, gates=False):
        """View all zones in the terrain
        a) gates:           Boolean Value. Do you want to show the gates?
        """
        plt.imshow(self.zone_map)
        plt.colorbar()
        if gates:
            x, y = zip(*self.gate_points)
            plt.scatter(x, y, edgecolors=green)
        plt.show()
        return

    def water_level_decomposition(self):
        """Perform water level decomposition to split zones."""
        for current_water_level in range(0, self.max_height):
            for tile in self.height_vector[current_water_level]:
                nbors = get_neighbors(tile, self.map_size)
                zone_id1 = zone_id2 = 0
                for point in nbors:
                    if self.zone_map[point[1]][point[0]] != 0:
                        if zone_id1 != 0:
                            zone_id2 = self.zone_map[point[1]][point[0]]
                            break
                        else:
                            zone_id1 = self.zone_map[point[1]][point[0]]
                if zone_id1 == 0:
                    self.zone_no += 1
                    self.zone_map[tile[1]][tile[0]] = self.zone_no
                else:
                    self.zone_map[tile[1]][tile[0]] = zone_id1
                    if zone_id1 != zone_id2 and zone_id2 != 0:
                        self.gate_points.append(tile)
        return
