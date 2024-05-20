from model.N_puzzle import N_puzzle

def reconstruir(state):
    path = []
    while state:
        path.append(state.board)
        state = state.parent
    return path[::-1]

def a_star(initial, goal):
    lista_inicial = []
    lista_final = set()
    estado_inicial = N_puzzle(initial, goal)
    lista_inicial.append(estado_inicial)

    while lista_inicial:
        lista_inicial.sort(key=lambda x: x.f)
        estado_atual = lista_inicial.pop(0)

        if estado_atual.board == goal:
            return reconstruir(estado_atual)

        lista_final.add(tuple(estado_atual.board))

        for neighbor in estado_atual.estados_sucessores():
            if tuple(neighbor.board) in lista_final:
                continue

            if neighbor not in lista_inicial or neighbor.g < estado_atual.g:
                lista_inicial.append(neighbor)

    return None