from service.ids import ids 
from service.ids import ids, N_puzzle

def main():
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    initial = [1, 2, 3, 4, 5, 0, 6, 7, 8]
    max_depth = 30
    path = ids(initial, goal, max_depth)  

    if path:
        for step in path:
            print(step)
    else:
        print("Sem resolução!")

if __name__ == "__main__":
    main()