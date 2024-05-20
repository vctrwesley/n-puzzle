class N_puzzle:
    def __init__(self, board, goal, g=0, parent=None):
        self.board = board
        self.goal = goal
        self.g = g
        self.h = self.heuristic()
        self.f = self.g + self.h
        self.parent = parent  

    def heuristic(self):
        return sum(1 for i in range(len(self.board)) if self.board[i] != self.goal[i] and self.board[i] != 0)
    
    def estados_sucessores(self):
        lista_estados_sucessores = []
        posicao_zero = self.board.index(0)
        board_size = int(len(self.board) ** 0.5)
        linha, coluna = divmod(posicao_zero, board_size)
        
        movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for movi in movimentos:
            new_linha = linha + movi[0]
            new_coluna = coluna + movi[1]
            
            if 0 <= new_linha < board_size and 0 <= new_coluna < board_size:
                new_posicao_zero = new_linha * board_size + new_coluna

                new_board = self.board[:]

                aux_posicao_zero = new_board[posicao_zero]
                new_board[posicao_zero] = new_board[new_posicao_zero]
                new_board[new_posicao_zero] = aux_posicao_zero
                
                lista_estados_sucessores.append(N_puzzle(new_board, self.goal, self.g + 1, self))
        return lista_estados_sucessores
