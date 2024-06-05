class N_puzzle:
    def __init__(self, estado_atual, objetivo, g=0, estado_pai=None):
        self.estado_atual = estado_atual
        self.objetivo = objetivo
        self.g = g
        self.h = self.heuristic()
        self.f = self.g + self.h
        self.estado_pai = estado_pai  

    def heuristic(self):
        return sum(1 for i in range(len(self.estado_atual)) if self.estado_atual[i] != self.objetivo[i] and self.estado_atual[i] != 0)
    
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
