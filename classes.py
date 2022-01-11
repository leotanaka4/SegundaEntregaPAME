class Pessoa:
    def __init__(self, nome, data, genero):
        self.nome = nome
        self.data = data
        self.genero = genero

class Motorista(Pessoa):
    pass

class Fiscal(Pessoa):
    pass

class Ponto:
    def __init__(self, nome, rua, bairro):
        self.nome = nome
        self.rua = rua
        self.bairro = bairro

class Onibus:
    def __init__(self, placa, modelo, pontos, motorista, fiscal):
        self.placa = placa
        self.modelo = modelo
        self.pontos = pontos
        self.motorista = motorista
        self.fiscal = fiscal
