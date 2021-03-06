from mapworks import map_generator
from mapworks.visualization import animate_game_state
from game_map import Map
from mock_object import PathObject, WallObject
from movement_cost import linear_cost
from moves import adjacent_linear
from path_finding import PathFinder
from point import Point
from unit import FormationUnit, FORMATION, SCOUT
from formation import Formation
# from terrain.potential import manhattan
# from terrain.terrain_analysis import TerrainAnalyzer
from itertools import cycle

map_data = None


def is_valid_pos(cur_pos):
    x, y = cur_pos.x, cur_pos.y
    return 0 <= x < 100 and 0 <= y < 100 and map_data[y][x]


if __name__ == "__main__":
    map_data = map_generator.generate_map(100, 100, seed=25, obstacle_density=0.35)
    game_map = Map(map_data)
    start = Point(2, 2)
    end = Point(25, 65)
    rel_pos = [
        Point(-1, 1),
        Point(1, 1),
        Point(0, 0),
        Point(-1, -1),
        Point(1, -1),
    ]

    units_pos = [start + pos for pos in rel_pos]
    units = []
    for i, unit_pos in enumerate(units_pos):
        unit = FORMATION.copy(start + rel_pos[i])
        unit.add_to_formation(Formation(i, rel_pos, start, units_pos, game_map.is_valid_point), i == 2)  # 2nd index unit is leader
        unit.set_dest(end)
        unit.game_map = game_map
        units.append(unit)

    game_map = Map(map_data)
    game_map.active = units

    anim = animate_game_state(game_map, frames=200)
    anim.save('run_game.gif', writer='imagemagick', fps=10)
