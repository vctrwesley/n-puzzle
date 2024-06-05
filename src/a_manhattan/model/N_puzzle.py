class N_puzzle:
    def __init__(self, estado_atual, objetivo, g=0, estado_pai=None):
        self.estado_atual = estado_atual
        self.objetivo = objetivo
        self.g = g
        self.estado_pai = estado_pai
        self.h = self.heuristica()
        self.f = self.g + self.h

    def heuristica(self):
        n = int(len(self.estado_atual) ** 0.5)
        distance = 0
        for index, value in enumerate(self.estado_atual):
            if value != 0:
                target_index = self.objetivo.index(value)
                current_x, current_y = divmod(index, n)
                target_x, target_y = divmod(target_index, n)
                distance += abs(current_x - target_x) + abs(current_y - target_y)
        return distance

    def estados_sucessores(self):
        lista_estados_sucessores = []
        posicao_zero = self.estado_atual.index(0)
        tamanho_estado_atual = int(len(self.estado_atual) ** 0.5)
        linha, coluna = divmod(posicao_zero, tamanho_estado_atual)
        
        movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for movi in movimentos:
            new_linha = linha + movi[0]
            new_coluna = coluna + movi[1]
            
            if 0 <= new_linha < tamanho_estado_atual and 0 <= new_coluna < tamanho_estado_atual:
                new_posicao_zero = new_linha * tamanho_estado_atual + new_coluna

                new_estado_atual = self.estado_atual[:]

                aux_posicao_zero = new_estado_atual[posicao_zero]
                new_estado_atual[posicao_zero] = new_estado_atual[new_posicao_zero]
                new_estado_atual[new_posicao_zero] = aux_posicao_zero
                
                lista_estados_sucessores.append(N_puzzle(new_estado_atual, self.objetivo, self.g + 1, self))
        return lista_estados_sucessores