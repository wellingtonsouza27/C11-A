import numpy as np

def exercicio1():
    dados = np.genfromtxt("Cap4Parte3/space.csv", delimiter=";", dtype=str, encoding="utf-8")

    cabecalho = dados[0]
    dados = dados[1:]

    status = dados[:, cabecalho.tolist().index("Status Mission")]
    total = len(status)
    sucesso = np.sum(status == "Success")
    porcentagem = (sucesso / total) * 100

    print("1) Porcentagem de missões com sucesso:")
    print(porcentagem)

    custos = dados[:, cabecalho.tolist().index(" Cost")]
    custos = np.array([float(c) if c != "" else 0 for c in custos])
    custos_validos = custos[custos > 0]

    media = np.mean(custos_validos)

    print("\n2) Média de gastos das missões:")
    print(media)

    local = dados[:, cabecalho.tolist().index("Location")]
    missoes_eua = np.sum(np.char.find(local, "USA") >= 0)

    print("\n3) Missões realizadas pelos EUA:")
    print(missoes_eua)

    empresas = dados[:, cabecalho.tolist().index("Company Name")]
    detalhes = dados[:, cabecalho.tolist().index("Detail")]

    mask_spacex = empresas == "SpaceX"
    custos_spacex = custos[mask_spacex]
    detalhes_spacex = detalhes[mask_spacex]

    indice = np.argmax(custos_spacex)

    print("\n4) Missão mais cara da SpaceX:")
    print(detalhes_spacex[indice])

    empresas_unicas, contagens = np.unique(empresas, return_counts=True)

    print("\n5) Empresas e quantidade de missões:")
    for i in range(len(empresas_unicas)):
        print(empresas_unicas[i], "-", contagens[i])

def main():
    exercicio1()

if __name__ == "__main__":
    main()