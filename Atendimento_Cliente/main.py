import csv
import random
from servidor import Servidor
from graficos import grafico_barras, grafico_linhas, grafico_pizza
from simulacao import Simulacao
from atendente import Atendente

servidores = [Servidor(id=i, capacidade=random.randint(8, 20)) for i in range(3)]

simulacao = Simulacao(servidores, timesteps=10)

for servidor in servidores:
    for i in range(5):
        tipo_atendente = random.choice(["Suporte Técnico", "Vendas"])
        atendente = Atendente(id=f"A{i}", tipo=tipo_atendente)
        servidor.adicionar_atendente(atendente)

dados_status, mensagens_falha = simulacao.executar()

with open("falhas_servidores.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Timestep", "Servidor ID", "Mensagem"])
    for linha in mensagens_falha:
        writer.writerow(linha)

print("\nNúmero de redirecionamentos por servidor:")
for servidor in servidores:
    print(f"Servidor {servidor.id}: {servidor.redirecionamentos} redirecionamentos")

with open("redirecionamentos.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Servidor ID", "Redirecionamentos"])
    for servidor in servidores:
        writer.writerow([servidor.id, servidor.redirecionamentos])

print("\nAtendentes por servidor:")
for servidor in servidores:
    suporte_tec = sum(1 for atendente in servidor.atendentes if atendente.tipo == "Suporte Técnico")
    vendas = sum(1 for atendente in servidor.atendentes if atendente.tipo == "Vendas")
    print(f"Servidor {servidor.id}: {suporte_tec} Suporte Técnico, {vendas} Vendas")

dados_para_graficos = [linha[:4] for linha in dados_status]

grafico_barras(dados_para_graficos)
grafico_linhas(dados_para_graficos)
grafico_pizza(servidores)
