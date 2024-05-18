from model.N_puzzle import N_puzzle
from collections import deque

def reconstruct_path(state):
    path = []
    while state:
        path.append(state.board)
        state = state.parent
    return path[::-1]

def bfs(initial, goal):
    queue = deque()
    visited = set()
    initial_state = N_puzzle(initial)
    queue.append(initial_state)

    while queue:
        current_state = queue.popleft()

        if current_state.board == goal:
            return reconstruct_path(current_state)

        visited.add(tuple(current_state.board))

        for neighbor in current_state.get_neighbors():
            if tuple(neighbor.board) not in visited:
                queue.append(neighbor)

    return None