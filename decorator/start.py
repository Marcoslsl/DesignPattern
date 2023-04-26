
def decorato(funcao):
    def funcao_teste():
        print('kkk')
        funcao()
    return funcao_teste

@decorato
def minha_funcao():
    print('ola mundo')


minha_funcao()