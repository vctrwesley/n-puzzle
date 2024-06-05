from service.ids import relatorio 

def main():
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    initial = [1, 2, 3, 4, 5, 0, 6, 7, 8]
    path, max_memoria_usada, timeFinal, nos_expandidos, fator_ramificacao = relatorio(initial, goal)

    print("--------------------------------------\n")
    print("Uso maximo de memoria: ", max_memoria_usada, "MB")
    print("Quantidade de nos expandidos: ", nos_expandidos)
    print("Fator de ramificacao media: ", fator_ramificacao)
    print("Tempo de execucao: ", timeFinal)
    print("\n--------------------------------------\n")

    if path:
        for aux, step in enumerate(path):
            print(f"Passo {aux}: ", step)
    else:
        print("Da pa resolve n irmao!")

if __name__ == "__main__":
    main()