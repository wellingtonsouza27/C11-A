import math


def exercicio1():
    nome = input("Nome completo: ")
    print(f"\nNome maiúsculo: {nome.upper()}")
    print(f"\nNome minúsculo: {nome.lower()}")
    print(f"\nQuantidade de letras: {len(nome.replace(" ",""))}")

def exercicio2():
    num = int(input("Digite um número: "))
    inicio = int(input("Início do intervalo: "))
    fim = int(input("Fim do intervalo: "))
    
    print()

    for i in range(inicio, fim + 1):
        print(f"{num} * {i} = {num * i}")

def exercicio3():
    while(1):
        sexo = input("Digite M(homem) ou F(mulher): ")
        match sexo.upper():
            case 'M':
                print("Homem")
                break
            case 'F':
                print("Mulher")
                break
            case _:
                print("Sexo inválido\n")

def exercicio4():
    distancia = float(input("Distância em KM: "))
    if(distancia <= 200):
        preco = distancia*0.5
        print(f"Preço da passagem: R${preco:.2f}")
    else:
        preco = distancia*0.45
        print(f"Preço da passagem: R${preco:.2f}")

def exercicio5():
    num = int(input("Digite um número entre 1000 e 9999: "))
    if 1000 <= num <= 9999:
        unidade = num % 10
        dezena = (num // 10) % 10
        centena = (num // 100) % 10
        milhar = num // 1000

        print(f"\nUnidade: {unidade}")
        print(f"Dezena: {dezena}")
        print(f"Centena: {centena}")
        print(f"Milhar: {milhar}")
    else:
        print("Número inválido")

def exercicio6():
    num = float(input("Digite um número decimal: "))

    raiz = math.sqrt(num)
    teto = math.ceil(num)
    chao = math.floor(num)
    inteira = int(num)

    print(f"\nRaiz quadrada: {raiz}")
    print(f"Teto: {teto}")
    print(f"Chão: {chao}")
    print(f"Parte inteira: {inteira}")

def exibir_opcoes():
    print('\n1- Exercicio 1')
    print('2- Exercicio 2')
    print('3- Exercicio 3')
    print('4- Exercicio 4')
    print('5- Exercicio 5')
    print('6- Exercicio 6')
    print('7- Sair\n')

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
            exercicio6()
        elif opcao_escolhida == 7:
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