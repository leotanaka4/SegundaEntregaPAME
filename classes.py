class Pessoa:
    def __init__(self, identidade, nome, data, genero):
        self.identidade = identidade
        self.nome = nome
        self.data = data
        self.genero = genero
    
    def __str__(self):
        return f"ID: {self.identidade}\
                \nNome: { self.nome }\
                \nData: { self.data }\
                \nGênero: { self.genero }"

class Motorista(Pessoa):
    pass

class Fiscal(Pessoa):
    pass

class Ponto:
    def __init__(self, identidade, nome, rua, bairro):
        self.identidade = identidade
        self.nome = nome
        self.rua = rua
        self.bairro = bairro

    def __str__(self):
        return f"ID: {self.identidade}\
                \nNome: { self.nome }\
                \nRua: { self.rua }\
                \nGênero: { self.bairro }"

class Onibus:
    def __init__(self, identidade, placa, modelo, motorista):
        self.identidade = identidade
        self.placa = placa
        self.modelo = modelo
        self.rota = []
        self.motorista = motorista
        self.fiscal = " "
    
    def __str__(self):
        return f"ID: {self.identidade}\
                \nPlaca: { self.placa }\
                \nModelo: { self.modelo }\
                \nPontos: { self.pontos }\
                \nMotorista: { self.motorista }\
                \nFiscal: { self.fiscal }"
    
    def adicionarMotorista(self, motorista):
        print("Motorista com ID %d foi removido!" %(self.motorista.identidade))
        self.motorista = motorista

    def adicionarFiscal(self, fiscal):
        if (self.motorista != " "):
            print("Fiscal com ID %d foi removido!" %(self.fiscal.identidade))
        self.fiscal = fiscal
    
    def adicionarPonto(self, identidade, ponto):
        self.rota.insert(identidade, ponto)