import functools
import itertools

import helper
import priority_queue


class PathFinder:
    MAX_VALID_NODES = 10000
    def __init__(self, movement_cost, heuristic_cost, is_valid_move):
        """
        Initializes the path finder with relevant functions. Helps reduce the number of
        parameters in a function.

        Args:
            movement_cost: real movement cost, logically equivalent to h(n)
            heuristic_cost: assumed movement cost, logically equivalent to g(n)
            is_valid_move: takes a point and returns whether it is a valid position or not,
                and is used in the a* algorithm to element potential points

        Return:
            List[(int, int)]: List of points to take to reach end in the forward direction
        """

        self.movement_cost = movement_cost
        self.heuristic_cost = heuristic_cost
        self.is_valid_move = is_valid_move

    @staticmethod
    def _get_path_from_store(end, store):
        path = []
        path_itr = end

        # iteration stops when path reaches start point or a point with no parent
        while path_itr in store:
            (_, parent) = store[path_itr]

            if path_itr == parent:
                break
            else:
                path.append(path_itr)
                path_itr = parent

        path.reverse()
        return path

    def find_path(self, *args, return_store=False):
        """
        Takes start and end point and returns a list of points indicating path in the forward direction

        Args:
            *args: arguments required by generic_a_star function
            return_store: returns the store as well if set to True

        Return:
            List[(int, int)]: List of points to take to reach end in the forward direction
            Dictionary{point: (score, parent)}: Optional. Dictionary containing all points that were evaluated
        """

        store = self.generic_a_star(*args)
        if not store:  # if store is empty return empty path
            if return_store:
                return [], {}
            else:
                return []

        end = args[2]  # 3rd argument contains end point
        path = PathFinder._get_path_from_store(end, store)

        if return_store:
            return path, store
        else:
            return path

    def find_path_waypoints(self, moves, waypoints, return_store=False):
        """
        Takes a list of waypoint and returns a list of points indicating a path passing through all the waypoints in
        the forward direction

        Args:
            moves: list of legal next moves
            waypoints: List of points including start and end point that the path should visit
            return_store: returns the store as well if set to True

        Return: List (int, int): Returns List of points to take to reach end in the forward direction. Dictionary{
        point: (score, parent)}: Optional. Dictionary containing all points that were evaluated. Note: for a point
        visited multiple times, the (score, parent) value will be one of the waypoint segment visited later
        """

        paths = []
        stores = []
        for start, end in helper.pairwise(waypoints):
            stores.append(self.generic_a_star(moves, start, end))
            paths.append(PathFinder._get_path_from_store(end, stores[-1]))

        path = []
        end = waypoints[-1]
        # if any path is empty, the path cannot be calculated
        if all(paths):
            for path in paths:
                path.pop()

            paths[-1].append(end)
            path = list(itertools.chain.from_iterable(paths))

        if return_store:
            # lazy merge stores, z = {**x, **y}, common keys
            # in x and y written over by value of y
            store = functools.reduce(lambda x, y: {**x, **y}, stores)
            return path, store
        else:
            return path

    def find_step(self, *args):
        """
        Takes start and end point and returns next step in the forward direction

        Args:
            *args: arguments required by generic_a_star function

        Return:
            (int, int): List of points to take to reach end in the forward direction
        """

        return self.find_path(*args)[0]

    def repair_path(self, moves, prev_path, m_steps):
        """
        Takes an existing path and performs repair/recomputation upto m steps ahead

        Args:
            moves: list of allowed moves at each point
            prev_path: previously calculated path where head of list indicates current position
            m_steps: number of steps ahead, to repair

        Return:
            List[(int, int)]: List of points to take to reach end in the forward direction
        """

        start = moves[0]
        end_index = m_steps if m_steps < len(prev_path) else -1
        end = prev_path[end_index]

        repaired_path = self.find_path(moves, start, end)

        # extend path when end point is not same as end of previous path
        if end_index != -1:
            return repaired_path.extend(prev_path[end_index:-1])
        else:
            return repaired_path

    def generic_a_star(self, moves, start, end, max_nodes=MAX_VALID_NODES):
        """
        Performs an a* search on the map with the given set of moves
        queue implementation stores the state which consists of
        current position and estimated cost to end point. Based on
        the estimated cost the queue is sorted. The store is indexed
        on position and stores actual cost of reaching the point
        along with parent point.

        Note: end should be a valid point on the map for path to be found

        Args:
            moves: list of allowed moves at each point
            start: x and y coordinates of start point
            end: x and y coordinates of end point
            max_nodes: max number of valid nodes to process

        Returns:
            store: contains the all the states encountered with links to parent states
                it can be used to generate the path and the next step
        """

        def total_cost(cur_pos, next_pos, end):
            return self.movement_cost(cur_pos, next_pos) + self.heuristic_cost(next_pos, end)

        queue = priority_queue.PriorityQueue()
        queue.push((self.heuristic_cost(start, end), start))
        store = {start: (0, start)}

        while not queue.is_empty():
            (_, cur_pos) = queue.pop()
            (cur_score, _) = store[cur_pos]
            if cur_pos == end or max_nodes <= 0:
                return store  # return store on reaching end or when exhausted nodes

            next_moves = [cur_pos + move for move in moves]
            valid_moves = [move for move in next_moves if self.is_valid_move(move)]
            max_nodes -= len(valid_moves)
            possible_state = [(total_cost(cur_pos, move, end), move) for move in valid_moves]
            valid_state = [(next_score, next_pos) for (next_score, next_pos) in possible_state
                           if next_score <= cur_score + self.heuristic_cost(cur_pos, end)]
            update_state = [state for state in valid_state if state[1] not in store]
            for (next_score, next_pos) in update_state:
                store[next_pos] = (cur_score + self.movement_cost(cur_pos, next_pos), cur_pos)
                queue.push((next_score, next_pos))

        return {}

    def best_potential_step(self, game_map, cur_unit):
        """
        Finds the point with the best potential score for the next step.
        If path and range is given, finds the best potential score point
        within the range of the next step prescribed by path.

        Note: function does not compare does not calculate score of current
        position. This may cause thrashing as unit might try to move to points
        that are not an improvement on the current position. TODO

        Args:
            cur_pos Point: current unit
            path List(Point): prescribed path from source to destination
            range int: cutoff range from points along the path

        Return:
            Point: best step
        """
        next_pos = game_map.valid_next_pos(cur_unit)
        potential_values = game_map.next_pos_potential(cur_unit, next_pos)
        best_state = min(potential_values)
        return best_state[1]

    def reconstruct_path(self, moves, cur_pos, path):
        """
        TODO
        Reconstructs a new path from current position,
        that joins the given path at some point.

        Note: consider intersecting intersecting further along the
        path based on point sensitivity TODO

        Args:
            moves: set of moves possible on each turn
            cur_pos: current position of unit
            path: previous path from which unit has deviated

        Return:
            New path
        """
        dest = path.popleft()
        correction = self.find_path(moves, cur_pos, dest)
        path.extendleft(correction.reverse())
        return path
