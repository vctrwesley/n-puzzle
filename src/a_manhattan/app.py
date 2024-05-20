from service.a_star import a_star

def main():
    #initial = [1, 2, 3, 4, 0, 5, 6, 7, 8]
    initial = [7, 0, 6, 1, 5, 2, 3, 4, 8]
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    path = a_star(initial, goal)

    if path:
        for aux, step in enumerate(path):
            print(f"Passo {aux}: ", step)
    else:
        print("Da pa resolve n irmao!")

if __name__ == "__main__":
    main()