import pandas as pd

def exercicio_series_dataframe():

    # -------------------------
    # QUESTÃO 1
    # -------------------------
    seriesAno1 = pd.Series({
        'Java': 16.25,
        'C': 16.04,
        'Python': 9.85
    })

    seriesAno2 = pd.Series({
        'C': 16.21,
        'Python': 12.12,
        'Java': 11.68
    })

    print("1) Series criadas:")
    print("\nAno 1:\n", seriesAno1)
    print("\nAno 2:\n", seriesAno2)

    # -------------------------
    # QUESTÃO 2
    # -------------------------
    print("\n2) Total de mercado:")

    print("Ano 1:", seriesAno1.sum())
    print("Ano 2:", seriesAno2.sum())

    # -------------------------
    # QUESTÃO 3
    # -------------------------
    crescimento = seriesAno2 - seriesAno1

    print("\n3) Crescimento/Declínio:")
    print(crescimento)

    # -------------------------
    # QUESTÃO 4
    # -------------------------
    crescimento_positivo = crescimento[crescimento > 0]

    print("\n4) Linguagens que cresceram:")
    print(crescimento_positivo)

    # -------------------------
    # QUESTÃO 5
    # -------------------------
    # projeção para +2 anos
    projecao = seriesAno2 + (crescimento * 2)

    print("\n5) Projeção futura:")
    print(projecao)

    print("\nMais popular:")
    print(projecao.nlargest(1))

    # -------------------------
    # QUESTÃO 6, 7 e 8
    # -------------------------
    # DataFrame exemplo
    df = pd.DataFrame({
        'W': [10, 29, 30, 43, 37],
        'X': [37, 26, 9, 41, 48],
        'Y': [16, 30, 10, 37, 12],
        'Z': [1, 49, 1, 17, 25]
    }, index=['A', 'B', 'C', 'D', 'E'])

    print("\nDataFrame:\n", df)

    # QUESTÃO 6
    media_x_menor_30 = df[df['X'] < 30]['X'].mean()

    print("\n6) Média de X < 30:")
    print(media_x_menor_30)

    # QUESTÃO 7
    media_linha_D = df.loc['D'].mean()
    soma_linha_E = df.iloc[4].sum()

    print("\n7) Média linha D (loc):", media_linha_D)
    print("Soma linha E (iloc):", soma_linha_E)

    # QUESTÃO 8
    slicing = df.loc[['A', 'C', 'E'], ['X', 'Y']]

    print("\n8) Slicing:")
    print(slicing)

    print("\nSoma das linhas:")
    print(slicing.sum(axis=1))

    print("\nSoma das colunas:")
    print(slicing.sum(axis=0))


def main():
    exercicio_series_dataframe()


if __name__ == "__main__":
    main()