import matplotlib.pyplot as plt
import numpy as np
import queue
from terrain import zone
from terrain.potential import manhattan
from helper import get_neighbors


class TerrainAnalyzer:
    def __init__(self, map_data, choke_width=5):
        """Create and initialize Terrain Analyzer.
        a) map_data:        Boolean numpy array. True for passable, False for impassable.
        b) choke_width:     Parameter. Width of choke point.
        """
        self.map_data = map_data
        self.map_size = map_data.shape
        self.height_map, self.height_vector = manhattan(map_data, max_depth=choke_width, return_depth_vector=True)
        self.max_height = len(self.height_vector)
        self.zone_map = map_data * 0 - 1
        self.zone_no = -1
        self.zones = []
        self.gate_points = []
        self.manhattan_flood()
        return

    def view_terrain(self, grid=True, gates=True, graph=True):
        """View all zones in the terrain
        a) grid:            Boolean Value. Display grid?
        b) gates:           Boolean Value. Do you want to show the gates?
        c) graph:           Boolean Value. Plot connectivity graph?
        """
        plt.imshow(self.zone_map)
        plt.colorbar()
        plt.xticks(np.arange(0.5, self.map_size[1], 1.0), [])
        plt.yticks(np.arange(-0.5, self.map_size[0], 1.0), [])
        plt.gca().set_xlim([-0.5, self.map_size[1] - 0.5])
        plt.gca().set_ylim([-0.5, self.map_size[0] - 0.5])
        plt.gca().invert_yaxis()
        plt.grid(grid)
        plt.connect('button_press_event', self.mouse_move)
        if gates and self.gate_points:
            x, y = zip(*self.gate_points)
            plt.scatter(x, y, color='green')
        print(self.zone_no, "zones found")
        x, y = zip(*[Z.center for Z in self.zones])
        plt.scatter(x, y, edgecolors='white', color='red')
        if graph:
            for Z in self.zones:
                p1 = Z.center
                for zone_id in Z.entry_points:
                    p2 = self.zones[zone_id].center
                    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color='white')
        plt.show()
        return

    # noinspection PyTypeChecker
    def manhattan_flood(self):
        """Perform water level decomposition to split zones."""
        wavefront = queue.Queue()
        for i in range(0, len(self.height_vector[0])):
            x, y = self.height_vector[0][i]
            if self.zone_map[y][x] == -1:
                self.zone_no += 1
                self.zones.append(zone.Zone(self.zone_no))
                self.flood_sea_floor((x, y), wavefront)
        while not wavefront.empty():
            tile = wavefront.get()
            if self.zone_map[tile[1]][tile[0]] != -1:
                continue
            nbors = get_neighbors(tile, self.map_size)
            zone_id = -1
            nbor_id = -1
            for point in nbors:
                if self.zone_map[point[1]][point[0]] != -1:
                    if zone_id != -1 and nbor_id == -1 and self.zone_map[point[1]][point[0]] != zone_id:
                        nbor_id = self.zone_map[point[1]][point[0]]
                        self.gate_points.append(tile)
                        self.zones[zone_id].add_gate_point(nbor_id, tile)
                        self.zones[nbor_id].add_gate_point(zone_id, tile)
                    elif zone_id == -1:
                        zone_id = self.zone_map[point[1]][point[0]]
                elif self.map_data[point[1]][point[0]]:
                    wavefront.put(point)
            if zone_id != -1:
                self.zone_map[tile[1]][tile[0]] = zone_id
                self.zones[zone_id].points.append(tile)
        self.zone_no += 1
        for Z in self.zones:
            Z.size = len(Z.points)
            Z.update_center()
        return

    def flood_sea_floor(self, current, wavefront):
        """Recursively flood fill a given region in the sea floor with a given zone id.
        a) current:         Current point being processed (int, int).
        b) wavefront:       Huygens wavefront created by boundary of fill (queue.Queue()).
        """
        q = queue.Queue()
        q.put(current)
        self.zone_map[current[1]][current[0]] = self.zone_no
        self.zones[-1].points.append(current)
        while not q.empty():
            new_point = q.get()
            nbors = get_neighbors(new_point, self.map_size)
            for point in nbors:
                x, y = point
                if not self.map_data[y][x]:
                    continue
                if self.zone_map[y][x] == -1 and self.height_map[y][x] == 0:
                    q.put(point)
                    self.zone_map[y][x] = self.zone_no
                    self.zones[-1].points.append(point)
                elif self.zone_map[y][x] == -1 and self.height_map[y][x] != 0:
                    wavefront.put(point)
        return

    def mouse_move(self, event):
        """Show coordinates of selected point"""
        if event.xdata is None or event.ydata is None:
            return
        x, y = int(round(event.xdata)), int(round(event.ydata))
        zone_id = self.zone_map[y][x]
        if zone_id != -1:
            print((x, y), "zone ->", zone_id, "size ->", self.zones[zone_id].size)
        else:
            print((x, y), "impassable terrain")
        return
