class Guerreiro:

    def __init__(self, habilidade_arco, habilidade_cura, habildade_luta):

        self.habilidade_arco = habilidade_arco
        self.habilidade_cura = habilidade_cura
        self.habilidade_luta = habildade_luta

    def curar(self):
        print("curar outro guerreiro")

    def lutar(self):
        print("atacar com espada")

    def flexada(self):
        print("atacar com flexas")

    def attributos(self):
        print("""
             nivel arco: {}
             nivel cura: {}
             nivel luta: {}""".format(self.habilidade_arco,
                                      self.habilidade_cura,
                                      self.habilidade_luta))