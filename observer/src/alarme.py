from typing import Type
from .interfaces import Observador

class Alarme:

    def __init__(self) -> None:
        self.beep = False
        self.dorminhocos = []

    def addPeassoa(self, pessoa: Type[Observador]):
        self.dorminhocos.append(pessoa)

    def estado_alarme(self):
        return self.beep
    
    def tocar(self):
        self.beed = True
        for pessoa in self.dorminhocos:
            pessoa.update()

        self.dorminhocos = []



