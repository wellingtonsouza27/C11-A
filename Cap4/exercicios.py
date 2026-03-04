import numpy as np
import random

def exercicio1():
    array1 = np.ones(8, dtype=int)

    array2 = np.random.randint(0, 10, 8)

    array3 = array1 + array2

    print("Array 1 (só 1's):")
    print(array1)

    print("\nArray 2 (aleatório 0-9):")
    print(array2)

    print("\nArray Resultante (soma):")
    print(array3)

    soma_total = np.sum(array3)
    print(f"\nSoma total dos elementos: {soma_total}")

    if soma_total >= 40:
        matriz = array3.reshape(4, 2)
        print("\nMatriz com MAIS LINHAS do que COLUNAS (4x2):")
    else:
        matriz = array3.reshape(2, 4)
        print("\nMatriz com MAIS COLUNAS do que LINHAS (2x4):")

    print(matriz)

def exercicio2():
    array1 = np.arange(0, 52, 2)
    array2 = np.arange(100, 49, -2)

    concatenado = np.concatenate((array1, array2))
    ordenado = np.sort(concatenado)

    print("Array 1:")
    print(array1)

    print("\nArray 2:")
    print(array2)

    print("\nConcatenado:")
    print(concatenado)

    print("\nOrdenado:")
    print(ordenado)

def exercicio3():
    campo = np.zeros((2,2), dtype=int)

    linha_bomba = random.randint(0,1)
    coluna_bomba = random.randint(0,1)

    campo[linha_bomba][coluna_bomba] = 1

    tentativas = 0
    posicoes_seguras = 0

    while tentativas < 3:
        print("\nMatriz:")
        print(campo * 0)

        linha = int(input("Escolha a linha (0 ou 1): "))
        coluna = int(input("Escolha a coluna (0 ou 1): "))

        tentativas += 1

        if campo[linha][coluna] == 1:
            print("Game Over! :( Try Again!")
            return
        else:
            posicoes_seguras += 1
            print("Posição segura!")

            if posicoes_seguras == 3:
                print("Congratulations! You beat the game! :)")
                return

    print("Game Over! :( Try Again!")

def exercicio4():
    linhas = int(input("Número de linhas: "))
    colunas = int(input("Número de colunas: "))

    matriz = np.random.randint(0, 10, (linhas, colunas))

    print("\nMatriz:")
    print(matriz)

    total_elementos = linhas * colunas

    print(f"\nTotal de elementos: {total_elementos}")

    if total_elementos % 2 == 0:
        print("A matriz pode se tornar um vetor unidimensional com número PAR de elementos.")
    else:
        print("A matriz pode se tornar um vetor unidimensional com número ÍMPAR de elementos.")

def exercicio5():
    np.random.seed(10)
    matriz = np.random.randint(1, 51, (4, 4))

    print("Matriz:")
    print(matriz)

    media_linhas = np.mean(matriz, axis=1)
    media_colunas = np.mean(matriz, axis=0)

    print("\nMédia das linhas:")
    print(media_linhas)

    print("\nMédia das colunas:")
    print(media_colunas)

    print("\nMaior média das linhas:")
    print(np.max(media_linhas))

    print("\nMaior média das colunas:")
    print(np.max(media_colunas))

    valores, contagens = np.unique(matriz, return_counts=True)

    print("\nQuantidade de aparições de cada número:")
    for v, c in zip(valores, contagens):
        print(f"{v} aparece {c} vez(es)")

    print("\nNúmeros que aparecem 2 vezes:")
    print(valores[contagens == 2])

def exibir_opcoes():
    print('\n1- Exercicio 1')
    print('2- Exercicio 2')
    print('3- Exercicio 3')
    print('4- Exercicio 4')
    print('5- Exercicio 5')
    print('6- Sair\n')

def escolher_exercicio():
    try:
        opcao_escolhida = int(input("\nEscolha uma opção: "))
        print()

        if opcao_escolhida == 1:
            exercicio1()     
        elif opcao_escolhida == 2:
            exercicio2()   
        elif opcao_escolhida == 3:
            exercicio3()      
        elif opcao_escolhida == 4:
            exercicio4()
        elif opcao_escolhida == 5:
            exercicio5() 
        elif opcao_escolhida == 6:
            sair()   
        else:
            opcao_invalida()

    except Exception:
        opcao_invalida()

def sair():
    print("Saindo...")
    exit()

def opcao_invalida():
    print("Opção inválida")

def main():
    while True:
        exibir_opcoes()
        escolher_exercicio()

if __name__ == '__main__':
    main()