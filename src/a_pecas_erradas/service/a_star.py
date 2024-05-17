from model.N_puzzle import N_puzzle

def reconstruct_path(state):
    path = []
    while state:
        path.append(state.board)
        state = state.parent
    return path[::-1]

def a_star(initial, goal):
    open_list = []
    closed_set = set()
    initial_state = N_puzzle(initial, goal)
    open_list.append(initial_state)

    while open_list:
        open_list.sort(key=lambda x: x.f)
        current_state = open_list.pop(0)

        if current_state.board == goal:
            return reconstruct_path(current_state)

        closed_set.add(tuple(current_state.board))

        for neighbor in current_state.get_neighbors():
            if tuple(neighbor.board) in closed_set:
                continue

            if neighbor not in open_list or neighbor.g < current_state.g:
                open_list.append(neighbor)

    return None