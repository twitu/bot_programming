import heuristic
import priority_queue
import helper

class PathFinder:

    def __init__(cost_func, is_valid_pos):
        """
        Initializes the path finder with relevant functions. Helps reduce the number of
        parameters in a function.

        Args:
            cost_func: cost function ideally expected to be a sum of g(n) and h(n) to
                use the harness the effectiveness of a* algorithm
            is_valid_pos: takes a point and returns whether it is a valid position or not,
                and is used in the a* algorithm to element potential points

        Return:
            List[(int, int)]: List of points to take to reach end in the forward direction
        """

        self.cost_func = cost_func
        self.is_valid_pos = is_valid_pos

    def find_path(*args):
        """
        Takes start and end point and returns a list of points indicating path in the forward direction

        Args:
            *args: arguments required by generic_a_star function

        Return:
            List[(int, int)]: List of points to take to reach end in the forward direction
        """

        store = generic_a_star(*args)
        path = []
        path_itr = end

        # iteration stops when path reaches start point or a point with no parent
        while path_itr != store.get(path_itr, path_itr):
            if path_itr not in store: break
            path.append(path_itr)
            path_itr = store[path_itr]

        return reversed(path)

    def find_step(*args):
        """
        Takes start and end point and returns next step in the forward direction

        Args:
            *args: arguments required by generic_a_star function

        Return:
            (int, int): List of points to take to reach end in the forward direction
        """

        return find_path(*args)[0]

    def repair_path(map, moves, prev_path, m_steps):
        """
        Takes an existing path and performs repair/recomputation upto m steps ahead

        Args:
            map: 2-D grid map with true and false indicating passable terrain
            moves: list of allowed moves at each point
            prev_path: previously calculated path where head of list indicates current position
            m_steps: number of steps ahead, to repair

        Return:
            List[(int, int)]: List of points to take to reach end in the forward direction
        """

        start = moves[0]
        end_index = m_steps if m_steps < len(prev_path) else -1
        end = prev_path[end_index]

        repaired_path = find_path(map, moves, start, end)

        # extend path when end point is not same as end of previous path
        if end_index != -1:
            return repaired_path.extend(prev_path[end_index:-1])
        else:
            return repaired_path


    def generic_a_star(map, moves, start, end):
        """
        Performs an a* search on the map with the given set of moves

        Args:
            map: 2-D grid map with true and false indicating passable terrain
            moves: list of allowed moves at each point
            start: x and y coordinates of start point
            end: x and y coordinates of end point

        Returns:
            store: contains the all the states encountered with links to parent states
                it can be used to generate the path and the next step
        """

        queue = priority_queue.PriorityQueue()
        queue.push(0, start)
        store = {start: start}

        while (not queue.is_empty()):
            pos = queue.pop()
            if pos == end: return store  # return store on reaching end

            next_moves = [helper.add_tuple_elements(pos, move) for move in moves]
            valid_pos = [(self.cost_func(move), move) for move in next_moves if self.is_valid_pos(move)]
            valid_moves = [next_pos for next_pos in valid_pos if next_pos[0] <= pos[0]]
            [store[move[1]] = pos for move in valid_moves if move[1] not in store]
            [queue.push(valid_move) for move in valid_moves]

        return {}

    def simple_bfs(map, moves, start, end):
        """
        Performs bfs search on the map with the given set of moves

        Args:
            map: 2-D grid map with true and false indicating passable terrain
            moves: list of allowed moves at each point
            start: x and y coordinates of start point
            end: x and y coordinates of end point

        Returns:
            store: contains the all the states encountered with links to parent states
                it can be used to generate the path and the next step
        """

        queue = priority_queue.SimpleQueue()
        queue.push(start)
        store = {start: start}

        while (not queue.is_empty()):
            pos = queue.pop()
            if pos == end: return store  # return store on reaching end

            next_moves = [helper.add_tuple_elements(pos, move) for move in moves]
            valid_pos = [move for move in next_moves if self.is_valid_pos(move)]
            [store[move] = pos for move in valid_moves if move not in store]
            [queue.push(valid_move) for move in valid_moves]

        return {}

