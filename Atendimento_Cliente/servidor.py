class Servidor:
    def __init__(self, id, capacidade):
        self.id = id
        self.capacidade = capacidade
        self.ocupados = 0
        self.falhas = 0
        self.redirecionamentos = 0
        self.clientes_atendidos = 0
        self.atendentes = []

    def adicionar_atendente(self, atendente):
        if len(self.atendentes) < self.capacidade:
            self.atendentes.append(atendente)
        else:
            print(f"Servidor {self.id} atingiu a capacidade máxima de atendentes.")

    def remover_atendente(self, atendente):
        if atendente in self.atendentes:
            self.atendentes.remove(atendente)
            print(f"Atendente {atendente.id} removido do Servidor {self.id}.")
        else:
            print(f"Atendente {atendente.id} não encontrado no Servidor {self.id}.")

    def processar_solicitacao(self, tipo_solicitacao):
        for atendente in self.atendentes:
            if atendente.tipo == tipo_solicitacao and not atendente.ocupado:
                atendente.atender()
                print(f"Atendente {atendente.id} está atendendo {tipo_solicitacao}.")
                return True
        return False

    def processar(self, demanda):
        if self.ocupados + demanda <= self.capacidade:
            self.ocupados += demanda
            self.clientes_atendidos += demanda
            return None
        else:
            self.falhas += 1
            mensagem = f"Falha no Servidor {self.id}: Demanda de {demanda} excedeu a capacidade de {self.capacidade}."
            print(mensagem)
            return mensagem

    def liberar(self):
        self.ocupados = 0
        self.falhas = 0
        for atendente in self.atendentes:
            atendente.liberar()
