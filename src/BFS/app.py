from service.bfs import bfs  # Importa o algoritmo BFS

def main():
    initial = [1, 2, 3, 4, 0, 5, 6, 7, 8]
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    path = bfs(initial, goal)  # Use o algoritmo BFS

    if path:
        for step in path:
            print(step)
    else:
        print("Sem resolução!")

if __name__ == "__main__":
    main()