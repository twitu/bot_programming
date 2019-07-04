import heuristic
import priority_queue
import helper

class PathFinder:

    def __init__(cost_func):
        self.cost_func = cost_func

    def path_from_start_to_end(map, moves, start, end):
        """
        Takes start and end point and returns a list of points indicating path in the forward direction

        Args:
            start {x, y}: dictionary contains x and y coordinates of start point
            end   {x, y}: dictionary contains x and y coordinates of end point

        Return:
            List[int]: List of points to take to reach end in the forward direction
        """
        store = generic_a_star(map, moves, start, end)
        path = []
        path_itr = end
        while path_itr != path_itr:
            if path_itr not in store: break
            path.append(path_itr)
            path_itr = store[path_itr]

        return path

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

        queue = priority_queue.Priority_Queue()
        queue.heappush(start, 0)
        store = {start: start}

        while (not queue.is_empty()):
            pos = queue.heappop()
            if pos == end: return store  # return store on reaching end

            pos_cost = self.cost_func(pos)
            next_moves = [helper.add_elements(pos, move) for move in moves]
            valid_pos = [move for move in next_moves if is_valid_pos(move)]
            next_pos = [next_pos for next_pos in valid_pos if self.cost_func(next_pos) <= pos_cost]
            store[move] = pos for move in valid_moves if move not in store
            queue.heappush(valid_move) for move in valid_moves

        return {}
