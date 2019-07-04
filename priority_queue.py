import heapq

class PriorityQueue:

    def __init__(self):
        self.elements = []

    def push(point, score):
        heapq.heappush(self.elements, (score, point))

    def pop():
        heapq.heappop(self.elements)

    def pop_point():
        heapq.heappop(self.elements)[1]

