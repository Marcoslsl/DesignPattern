from src import Guerreiro, LutaEspada, LutarArco, Curar

cavaeiro = Guerreiro(LutaEspada(6))
arqueiro = Guerreiro(LutarArco(9))

arqueiro.acao()
cavaeiro.acao()