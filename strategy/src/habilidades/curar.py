from .interface import IHabilidade

class Curar(IHabilidade):

    def __init__(self, nivel):
        self.nivel = nivel

    def comportamento(self):
        print("Curar")

    def nivel_atributo(self):
        print("nive de uso de Cura: {}".format(self.nivel))