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
    
    def get_neighbors(self):
        neighbors = []
        zero_index = self.board.index(0)
        board_size = int(len(self.board) ** 0.5)
        row, col = divmod(zero_index, board_size)
        
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for move in moves:
            new_row = row + move[0]
            new_col = col + move[1]
            
            if 0 <= new_row < board_size and 0 <= new_col < board_size:
                new_zero_index = new_row * board_size + new_col

                new_board = self.board[:]

                aux_zero_index = new_board[zero_index]
                new_board[zero_index] = new_board[new_zero_index]
                new_board[new_zero_index] = aux_zero_index
                
                neighbors.append(N_puzzle(new_board, self.goal, self.g + 1, self))
        return neighbors
