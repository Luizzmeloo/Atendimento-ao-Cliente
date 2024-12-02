import random
from atendente import Atendente

class Simulacao:
    def __init__(self, servidores, timesteps):
        self.servidores = servidores
        self.timesteps = timesteps
        self.log_redirecionamentos = []

    def redistribuir_solicitacao(self, atendente_falhou):
        tipo_falha = atendente_falhou.tipo
        for atendente in servidores.atendentes:
            if atendente.tipo == tipo_falha and not atendente.ocupado:
                atendente.ocupar()
                break

    def redirecionar(self, timestep, servidor_id):
        for servidor in self.servidores:
            if servidor.id != servidor_id and servidor.ocupados < servidor.capacidade:
                servidor.redirecionamentos += 1
                self.log_redirecionamentos.append(
                    f"Timestep {timestep}: Servidor {servidor_id} falhou e redirecionou para Servidor {servidor.id}."
                )
                print(
                    f"Redirecionando para Servidor {servidor.id}. Total de redirecionamentos: {servidor.redirecionamentos}")
                break

    def adicionar_atendente(self, servidor, atendente):
        if len(servidor.atendentes) < servidor.capacidade:
            servidor.adicionar_atendente(atendente)
            print(f"Atendente {atendente.id} adicionado ao Servidor {servidor.id}.")
        else:
            print(f"Servidor {servidor.id} atingiu a capacidade máxima de atendentes.")

    def remover_atendente(self, servidor, atendente):
        if atendente in servidor.atendentes:
            servidor.remover_atendente(atendente)
            print(f"Atendente {atendente.id} removido do Servidor {servidor.id}.")
        else:
            print(f"Atendente {atendente.id} não encontrado no Servidor {servidor.id}.")

    def processar_solicitacoes(self):
        for t in range(self.timesteps):
            tipo_solicitacao = random.choice(["Suporte Técnico", "Vendas"])
            servidor_selecionado = random.choice(self.servidores)

            if not servidor_selecionado.processar_solicitacao(tipo_solicitacao):
                print(
                    f"Timestep {t}: Servidor {servidor_selecionado.id} não tem atendente disponível para {tipo_solicitacao}.")

    def executar(self):
        dados_status = []
        mensagens_falha = []
        for t in range(self.timesteps):
            print(f"\nTimestep {t}:")

            if t % 10 == 0:
                atendente = Atendente(id=f"A{t}", tipo=random.choice(["Suporte Técnico", "Vendas"]))
                servidor = random.choice(self.servidores)
                self.adicionar_atendente(servidor, atendente)

            if t % 15 == 0:
                servidor = random.choice(self.servidores)
                if servidor.atendentes:
                    atendente = random.choice(servidor.atendentes)
                    self.remover_atendente(servidor, atendente)

            for servidor in self.servidores:
                servidor.liberar()
                demanda = random.randint(5, 20)
                mensagem_falha = servidor.processar(demanda)

                if mensagem_falha:
                    self.redirecionar(t, servidor.id)
                    mensagens_falha.append([t, servidor.id, mensagem_falha])
                else:
                    mensagens_falha.append([t, servidor.id, "Sem falhas"])

                dados_status.append([t, servidor.id, servidor.ocupados, servidor.falhas])

        return dados_status, mensagens_falha

    def exibir_clientes_atendidos(self):
        print("Clientes atendidos por servidor:")
        for servidor in self.servidores:
            print(f"Servidor {servidor.id}: {servidor.clientes_atendidos} clientes")

    def gerar_solicitacoes(self):
        num_solicitacoes = random.randint(5, 15)
        for _ in range(num_solicitacoes):
            tipo_solicitacao = random.choice(["Suporte Técnico", "Vendas"])
            if tipo_solicitacao == "Suporte Técnico":
                fila_suporte.append(solicitacao)
            else:
                fila_vendas.append(solicitacao)