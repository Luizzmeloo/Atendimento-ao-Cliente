import matplotlib.pyplot as plt

def grafico_barras(dados):
    agrupados = {}
    for linha in dados:
        t, id, ocupados, falhas = linha[:4]
        if t not in agrupados:
            agrupados[t] = {}
        agrupados[t][id] = ocupados

    timesteps = sorted(agrupados.keys())
    servidores = sorted(agrupados[timesteps[0]].keys())
    valores = [[agrupados[t].get(s, 0) for s in servidores] for t in timesteps]

    for i, servidor in enumerate(servidores):
        plt.bar(
            [t + i * 0.2 for t in timesteps],
            [valores[t][i] for t in range(len(timesteps))],
            width=0.2,
            label=f"Servidor {servidor}",
        )

    plt.xlabel("Timestep")
    plt.ylabel("Atendimentos")
    plt.title("Atendimentos por Timestep")
    plt.legend()
    plt.show()

def grafico_linhas(dados):
    falhas_por_timestep = {}
    for t, _, _, falhas in dados:
        falhas_por_timestep[t] = falhas_por_timestep.get(t, 0) + falhas

    plt.plot(list(falhas_por_timestep.keys()), list(falhas_por_timestep.values()), label="Falhas")
    plt.xlabel("Timestep")
    plt.ylabel("Falhas")
    plt.title("Falhas por Timestep")
    plt.legend()
    plt.show()


def grafico_pizza(servidores):

    redirecionamentos = [servidor.redirecionamentos for servidor in servidores]

    if sum(redirecionamentos) == 0:
        print("Nenhum redirecionamento registrado. Não será gerado o gráfico de pizza.")
        return

    labels = [f"Servidor {i}" for i in range(len(servidores))]
    sizes = redirecionamentos

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title("Distribuição de Redirecionamentos entre Servidores")
    plt.show()
