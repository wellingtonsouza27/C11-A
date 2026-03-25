import numpy as np

def exercicio_paises():
    dados = np.genfromtxt(
        "Cap4Extra/paises.csv",
        delimiter=";",
        dtype=str,
        encoding="utf-8"
    )

    cabecalho = dados[0]
    cabecalho = [col.strip().replace("\ufeff", "") for col in cabecalho]

    dados = dados[1:]
    dados = np.char.strip(dados)

    print("1) País, Região, População e Área:\n")

    col_country = cabecalho.index("Country")
    col_region = cabecalho.index("Region")
    col_population = cabecalho.index("Population")
    col_area = cabecalho.index("Area (sq. mi.)")

    resultado = dados[:, [col_country, col_region, col_population, col_area]]
    print(resultado)

    # QUESTÃO 2
    regioes = dados[:, col_region]
    print("\n2) Regiões:")
    print(np.unique(regioes))

    # QUESTÃO 3
    col_literacy = cabecalho.index("Literacy (%)")
    literacy = np.array([float(x) if x != "" else 0 for x in dados[:, col_literacy]])
    literacy = literacy[literacy > 0]

    print("\n3) Média de alfabetização:")
    print(np.mean(literacy))

    # QUESTÃO 4
    print("\n4) América do Norte:")
    print(np.sum(regioes == "NORTHERN AMERICA"))

    # QUESTÃO 5
    col_gdp = cabecalho.index("GDP ($ per capita)")
    gdp = np.array([float(x) if x != "" else 0 for x in dados[:, col_gdp]])

    mask = regioes == "LATIN AMER. & CARIB"
    paises = dados[:, col_country][mask]
    gdp_latam = gdp[mask]

    print("\n5) Maior PIB per capita (LATAM):")
    print(paises[np.argmax(gdp_latam)])


def main():
    exercicio_paises()


if __name__ == "__main__":
    main()