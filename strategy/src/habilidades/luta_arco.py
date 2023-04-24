from .interface import IHabilidade

class LutarArco(IHabilidade):

    def __init__(self, nivel):
        self.nivel = nivel

    def comportamento(self):
        print("atirar flexas")

    def nivel_atributo(self):
        print("nive de uso de Arco: {}".format(self.nivel))