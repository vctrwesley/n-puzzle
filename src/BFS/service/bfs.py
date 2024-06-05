from model.N_puzzle import N_puzzle
from collections import deque
from time import time
from memory_profiler import memory_usage

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

    nos_expandidos = 0
    total_sucessores = 0

    while queue:
        current_state = queue.popleft()
        nos_expandidos += 1

        if current_state.board == goal:
            return reconstruct_path(current_state), nos_expandidos, total_sucessores

        visited.add(tuple(current_state.board))

        for neighbor in current_state.get_neighbors():
            total_sucessores += 1
            if tuple(neighbor.board) not in visited:
                queue.append(neighbor)

    return None, nos_expandidos, total_sucessores

def relatorio(inicial, objetivo):
    max_memoria_usada = max(memory_usage((bfs, (inicial, objetivo))))

    timeInicial = time()
    path, nos_expandidos, total_sucessores = bfs(inicial, objetivo)
    timeFinal = time() - timeInicial

    fator_ramificacao = 0

    if total_sucessores > 0:
        fator_ramificacao = total_sucessores/nos_expandidos

    if path:
        return path, max_memoria_usada, timeFinal, nos_expandidos, fator_ramificacao
    return path, max_memoria_usada, 0, nos_expandidos, fator_ramificacao