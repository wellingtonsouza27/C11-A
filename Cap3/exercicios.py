import math

def exercicio1():
    times = ["Barcelona", "Real Madrid", "Villarreal", "Atlético Madrid", "Betis"]

    print(f"3 primeiros colocados: {', '.join(times[:3])}")
    print(f"Últimos 2 colocados: {', '.join(times[-2:])}")
    print(f"Ordem alfabética: {', '.join(sorted(times))}")

    posicao = times.index("Barcelona") + 1
    print(f"Barcelona está na posição: {posicao}")

def exercicio2():
    loja1 = {"iPhone 13", "Samsung S22", "Xiaomi 12", "Moto G100"}
    loja2 = {"Samsung S22", "iPhone 13", "Xiaomi 13", "Pixel 7"}

    todos_modelos = loja1 | loja2

    modelos_comuns = loja1 & loja2

    print(f"Modelos disponíveis no total: {', '.join(todos_modelos)}")
    print(f"Modelos disponíveis nas duas lojas: {', '.join(modelos_comuns)}")

def exercicio3():
    aluno = {}

    aluno["nome"] = input("Nome do aluno: ")
    aluno["media"] = float(input("Média do aluno: "))

    if aluno["media"] >= 50:
        aluno["situacao"] = "AP"
    else:
        aluno["situacao"] = "RP"

    print("\nConteúdo do dicionário:")
    for chave, valor in aluno.items():
        print(f"{chave}: {valor}")

def exercicio4():
    pessoas = []

    for i in range(3):
        nome = input(f"Nome da {i+1}ª pessoa: ")
        peso = float(input(f"Peso da {i+1}ª pessoa: "))
        pessoas.append((nome, peso))

    mais_pesada = max(pessoas, key=lambda p: p[1])
    mais_leve = min(pessoas, key=lambda p: p[1])

    print(f"\nPessoa mais pesada: {mais_pesada[0]}")
    print(f"Pessoa mais leve: {mais_leve[0]}")

def exercicio5():
    total_idade = 0
    mulheres_menos_20 = 0

    n = int(input("Quantas pessoas deseja cadastrar? "))

    for i in range(n):
        print(f"\nPessoa {i+1}")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        sexo = input("Sexo (M/F): ").strip().upper()

        total_idade += idade

        if sexo == "F" and idade < 20:
            mulheres_menos_20 += 1

    media = total_idade / n if n > 0 else 0

    print(f"\nMédia de idade do grupo: {media:.2f}")
    print(f"Mulheres com menos de 20 anos: {mulheres_menos_20}")

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