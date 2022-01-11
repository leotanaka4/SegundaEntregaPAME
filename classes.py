class Pessoa:
    def __init__(self, nome, idade, nacionalidade):
        self.nome = nome
        self.idade = idade
        self.nacionalidade = nacionalidade

class Motorista(Pessoa):
    pass

class Fiscal(Pessoa):
    pass

class Ponto:
    def __init__(self, nome, rua, bairro, cidade):
        self.nome = nome
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade

class Onibus:
    def __init__(self, modelo, pontos, motorista, fiscal):
        self.modelo = modelo
        self.pontos = pontos
        self.motorista = motorista
        self.fiscal = fiscal
