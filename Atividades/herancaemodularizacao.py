# Arquivo banco.py
class Banco:
    def __init__(self, nome, endereco):
        self._nome = nome
        self._endereco = endereco

# Arquivo agencia.py
# from banco import Banco <- utilizado quando é importado de outro arquivo

class Agencia(Banco):
    def __init__(self, nome, endereco, numero):
        super().__init__(nome, endereco)
        self._numero = numero