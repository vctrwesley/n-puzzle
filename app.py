from src.utils.order import order

def main():
    initList = [1, 2, 3, 4, 0, 5, 6, 7, 8]
    objetiveList = order(initList)
    print("initList: ", initList)
    print("objetiveList: ", objetiveList)


if __name__ == '__main__':
    main()