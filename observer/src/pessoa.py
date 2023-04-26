from .interfaces import Observador

class Pessoa(Observador):

    def __init__(self) -> None:
        self.acordada = False

    def esta_acordada(self):
        return self.acordada

    def update(self):
        print("opa, acordei")
        self.acordada = True