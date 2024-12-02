class Atendente:
    def __init__(self, id, tipo):
        self.id = id
        self.tipo = tipo
        self.ocupado = False

    def atender(self):
        self.ocupado = True

    def liberar(self):
        self.ocupado = False
