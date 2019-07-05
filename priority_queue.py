import heapq

from collections import deque

class PriorityQueue:

    def __init__(self):
        self.elements = []

    def push(score, element):
        heapq.heappush(self.elements, (score, element))

    def pop():
        return heapq.heappop(self.elements)

    def pop_element():
        return heapq.heappop(self.elements)[1]

    def is_empty():
        return len(self.elements) == 0

class SimpleQueue:

    def __init(self):
        self.elements = deque()

    def push(element):
        self.elements.append(element)

    def pop():
        return self.elements.pop()

    def is_empty():
        return len(self.elements) == 0

