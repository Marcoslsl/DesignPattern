from. interface import IHabilidade

class LutaEspada(IHabilidade):

    def __init__(self, nivel):
        self.nivel = nivel

    def comportamento(self):
        print("lutar com espada")

    def nivel_atributo(self):
        print("nive de uso de espada: {}".format(self.nivel))