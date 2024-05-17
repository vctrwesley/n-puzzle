import heapq

class N_puzzle:
    def __init__(self, currentStatus, objectiveState, g=0, parent=None):
        self.currentStatus = currentStatus
        self.objectiveState = objectiveState
        self.g = g
        self.h = self.heuristic()
        self.f = self.g + self.h
        self.parent = parent

    def heuristic(self):
        return sum(1 for i in range(len(self.currentStatus)) if self.currentStatus[i] != self.objectiveState[i] and self.currentStatus[i] != 0)
    