import collections

class CodeRoyaleGameState:

    def __init__(self, N):
        self.que = collections.deque()
        self.baracks = [None]*N
        self.units = {"archer": 3, "soldier": 2}

    def schedule_troop(self, troop, barrack=None):
        """
        Troop is added to que, if no barack id
        is given troop will be pipelined in any
        available barack
        """
        self.que.append((troop, barrack))

    def deschedule_troop(self):
        """
        Removes last added troop. Note: will throw
        an error if queue is empty

        Returns:
            (troop, barack): Last scheduled troop
        """
        return self.que.pop()

    def next_troop_to_produce(self):
        """
        Peeks at first element from the left in queue.
        Note: will throw error if que is empty

        Returns:
            (troop, barack): head of queue
        """
        return self.que[0]

    def update_next_troop_to_produce(self, troop, barack):
        """
        Updates content add head of queue. barack id is required.
        """

        self.que[0] = (troop, barack)

    def produce_troop(self):
        """
        Pops head of queue and assigns the troop to production
        in a barack. If no barack is specified closest barack
        is assigned.

        Note: will throw error if que is empty

        Returns:
            (troop, barack): if successfully added to production
            None: if failed
        """
        troop, barack = self.que[0]
        time = self.units[troop]

        if not self.baracks[barack]:
            self.baracks[barack] = [troop, time]
            return self.que.popleft()

        return None

    def manual_produce_troop(self, troop, barack):
        """
        Manually override troop production. ignores
        queue.

        Note: will throw error if que is empty

        Args:
            troop: troop type
            barack: barack id must be specified

        Returns:
            (troop, barack): if successfully added to production
            None: if failed
        """
        time = self.units[troop]

        if not self.baracks[barack]:
            self.baracks[barack] = [troop, time]

        return None

    def pipeline(self):
        """
        Troops that are being created right now. Should ideally
        be called after tick() for the turn.

        Returns:
            List (troop, barrack, time): returns troop type, barrack id
                and ticks required to make it
        """

        return [(barack[0], i, barack[1]) for i, barack in enumerate(self.baracks) if barack]

    def tick(self):
        """
        Represents one complete turn or one time unit. Should
        ideally be called at the beginning of each turn

        Returns:
            List(troop, barack): returns completed troop, with barack id
        """

        # decrement one unit time from all units in production
        for barack in self.baracks:
            if barack:
                barack[1] -= 1

        completed = [(unit[0], i) for i, unit in enumerate(self.baracks) if unit and unit[1] == 0]
        self.finish(completed)
        return completed

    def finish(self, completed):
        """
        Empties given baracks. Should ideally be
        called with completed list of troops.

        Args:
            completed: List(barack): troop type with barack id
        """

        for _,barack in completed:
            self.baracks[barack] = None

    def empty_baracks(self):
        """
        Returns list of empty baracks

        Returns:
            List(int): list of barack ids
        """

        return [i for i, barack in enumerate(self.baracks) if not barack]

if __name__ == "__main__":
    state = CodeRoyaleGameState(10)
    state.schedule_troop("archer", 1)
    state.schedule_troop("soldier", 2)
    print(state.tick())
    print(state.produce_troop())
    print(state.pipeline())
    print(state.tick())
    print(state.pipeline())
    print(state.next_troop_to_produce())
    print(state.produce_troop())
    print(state.tick())
    print(state.empty_baracks())
    print(state.tick())

