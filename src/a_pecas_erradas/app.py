from service.a_star import a_star

def main():
    initial = [1, 2, 3, 4, 0, 5, 6, 7, 8]
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    path = a_star(initial, goal)

    if path:
        for step in path:
            print(step)
    else:
        print("Da pa resolve n irmao!")

if __name__ == "__main__":
    main()