class N_puzzle:
    def __init__(self, board, parent=None):
        self.board = board
        self.parent = parent  

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
                new_board = self.board[:]
                new_index = new_row * board_size + new_col
                new_board[zero_index], new_board[new_index] = new_board[new_index], new_board[zero_index]
                neighbors.append(N_puzzle(new_board, self))
                
        return neighbors