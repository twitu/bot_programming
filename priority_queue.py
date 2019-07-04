import heapq

class PriorityQueue:

    def __init__(self):
        self.elements = []

    def push(element, score):
        heapq.heappush(self.elements, (score, element))

    def pop():
        heapq.heappop(self.elements)

    def pop_element():
        heapq.heappop(self.elements)[1]

