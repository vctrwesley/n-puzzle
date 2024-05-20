from model.N_puzzle import N_puzzle
from collections import deque

def reconstruct_path(state):
    path = []
    while state:
        path.append(state.board)
        state = state.parent
    return path[::-1]

def dls(state, goal, depth):
    print(f"Current state: {state.board}, Current depth: {depth}")
    if depth == 0 and state.board == goal:
        return state
    elif depth > 0:
        for neighbor in state.get_neighbors():
            found = dls(neighbor, goal, depth - 1)
            if found:
                return found
    return None

def ids(initial, goal, max_depth):
    initial_state = N_puzzle(initial)
    for depth in range(max_depth):
        found = dls(initial_state, goal, depth)
        if found:
            return reconstruct_path(found)
    return None