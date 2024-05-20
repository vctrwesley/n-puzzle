class N_puzzle:
    def __init__(self, board, goal, g=0, parent=None):
        self.board = board
        self.goal = goal
        self.g = g
        self.parent = parent
        self.h = self.heuristic()
        self.f = self.g + self.h

    def heuristic(self):
        n = int(len(self.board) ** 0.5)
        distance = 0
        for index, value in enumerate(self.board):
            if value != 0:
                target_index = self.goal.index(value)
                current_x, current_y = divmod(index, n)
                target_x, target_y = divmod(target_index, n)
                distance += abs(current_x - target_x) + abs(current_y - target_y)
        return distance

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