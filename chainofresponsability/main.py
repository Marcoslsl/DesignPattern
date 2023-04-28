# serve para a carne e nos
from validators import BananaValidator

# ao inves disso

#class Validador:
#
#    def validar(self, comida: str):
#        if (comida == 'banana'):
#            self.__acao1()
#        elif (comida == 'nos'):
#            self.__acao2()
#        elif (comida == 'carne'):
#            self.__acao3()
#        else:
#            self.__acaoDefault()
#
#    def __acao1(self):
#        print("o macaco come banana")
#
#    def __acao2(self):
#        print("o esquilo come nos")
#
#    def __acao3(self):
#        print("o leao come carne")
#
#    def __acaoDefault(self):
#        print("comida indefinida")
        
class Validacao:

    def __init__(self) -> None:
        self.val = [
            BananaValidator()
        ]

    def process(self, comida: str):
        for v in self.val:
            if v.validate(comida): return v.action()

validacao = Validacao()
validacao.process('banana')