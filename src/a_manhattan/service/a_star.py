from model.N_puzzle import N_puzzle
from time import time
from memory_profiler import memory_usage

def reconstruct_path(estado):
    path = []
    while estado:
        path.append(estado.estado_atual)
        estado = estado.estado_pai
    return path[::-1]

def a_star(inicial, objetivo):
    lista_inicial = []
    lista_final = set()
    estado_inicial = N_puzzle(inicial, objetivo)
    lista_inicial.append(estado_inicial)

    nos_expandidos = 0
    total_sucessores = 0

    while lista_inicial:
        lista_inicial.sort(key=lambda x: x.f)
        estado_atual = lista_inicial.pop(0)
        nos_expandidos += 1

        if estado_atual.estado_atual == objetivo:
            return reconstruct_path(estado_atual), nos_expandidos, total_sucessores

        lista_final.add(tuple(estado_atual.estado_atual))

        for vizinho in estado_atual.estados_sucessores():
            total_sucessores += 1
            if tuple(vizinho.estado_atual) in lista_final:
                continue

            if vizinho not in lista_inicial or vizinho.g < estado_atual.g:
                lista_inicial.append(vizinho)

    return None, nos_expandidos, total_sucessores

def relatorio(inicial, objetivo):
    max_memoria_usada = max(memory_usage((a_star, (inicial, objetivo))))

    timeInicial = time()
    path, nos_expandidos, total_sucessores = a_star(inicial, objetivo)
    timeFinal = time() - timeInicial

    fator_ramificacao = 0

    if total_sucessores > 0:
        fator_ramificacao = total_sucessores/nos_expandidos

    if path:
        return path, max_memoria_usada, timeFinal, nos_expandidos, fator_ramificacao
    return path, max_memoria_usada, 0, nos_expandidos, fator_ramificacao