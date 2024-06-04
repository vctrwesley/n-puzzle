from model.N_puzzle import N_puzzle
from collections import deque

def reconstruct_path(state):
    path = []
    while state:
        path.append(state.board)
        state = state.parent
    return path[::-1]

def dfs(state, goal, max_depth):
    if state.board == goal:
        return state
    elif max_depth > 0:
        for neighbor in state.get_neighbors():
            if tuple(neighbor.board) not in explored:
                explored.add(tuple(neighbor.board))
                found = dfs(neighbor, goal, max_depth - 1)
                if found:
                    return found
    return None

def ids(initial, goal, max_depth):
    initial_state = N_puzzle(initial)
    global explored
    for depth in range(max_depth):
        explored = set()
        found = dfs(initial_state, goal, depth)
        if found:
            return reconstruct_path(found)
    return None