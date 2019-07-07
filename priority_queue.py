import heapq

from collections import deque

class PriorityQueue:

    def __init__(self):
        self.elements = []

    def push(self, score, element):
        heapq.heappush(self.elements, (score, element))

    def pop(self):
        return heapq.heappop(self.elements)

    def pop_element(self):
        return heapq.heappop(self.elements)[1]

    def is_empty(self):
        return len(self.elements) == 0

class SimpleQueue:

    def __init(self):
        self.elements = deque()

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop()

    def is_empty(self):
        return len(self.elements) == 0

