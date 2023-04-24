from .controller import write_in_database
from .helper import Adapter

def route1(message):

    processo = Adapter(Code())
    processo.handler(message)


class Code():

    def handler(self, message):
        token = message['header']['token']

        if token:
            print("autenticando o token")
            write_in_database(message['body']['name'], message['body']['message'])
