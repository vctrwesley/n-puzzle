from model.N_puzzle import N_puzzle
from collections import deque
from time import time
from memory_profiler import memory_usage

sucessores = 0
expandidos = 0

def reconstruct_path(state):
    path = []
    while state:
        path.append(state.board)
        state = state.parent
    return path[::-1]

def dfs(state, goal, max_depth):
    global sucessores, expandidos
    expandidos += 1
    if state.board == goal:
        return state
    elif max_depth > 0:
        for neighbor in state.get_neighbors():
            sucessores += 1
            if tuple(neighbor.board) not in explored:
                explored.add(tuple(neighbor.board))
                found = dfs(neighbor, goal, max_depth - 1)
                if found:
                    return found
    return None

def ids(initial, goal, max_depth):
    initial_state = N_puzzle(initial)
    nos_expandidos = 0
    total_sucessores = 0
    global explored
    global sucessores, expandidos
    for depth in range(max_depth):
        explored = set()

        sucessores = 0
        expandidos = 0

        found = dfs(initial_state, goal, depth)
        nos_expandidos += expandidos
        total_sucessores += sucessores
        if found:
            return reconstruct_path(found), nos_expandidos, total_sucessores
    return None, nos_expandidos, total_sucessores

def relatorio(inicial, objetivo):
    max_depth = 30
    max_memoria_usada = max(memory_usage((ids, (inicial, objetivo, max_depth))))

    timeInicial = time()
    path, nos_expandidos, total_sucessores = ids(inicial, objetivo, max_depth)
    timeFinal = time() - timeInicial

    fator_ramificacao = 0

    if total_sucessores > 0:
        fator_ramificacao = total_sucessores/nos_expandidos

    if path:
        return path, max_memoria_usada, timeFinal, nos_expandidos, fator_ramificacao
    return path, max_memoria_usada, 0, nos_expandidos, fator_ramificacao