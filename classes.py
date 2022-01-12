class Pessoa:
    def __init__(self, nome, data, genero):
        self.nome = nome
        self.data = data
        self.genero = genero
    
    def __str__(self):
        return f"Nome: { self.nome }\
                \nData: { self.data }\
                \nGênero: { self.genero }"
    
class Motorista(Pessoa):
    def alterarMotorista(self):
        self.nome = input("Digite o nome do motorista: ")
        self.data = input("Digite a data de nascimento do motorista: ")
        self.genero = input("Digite o gênero do motorista: ")
        return self

class Fiscal(Pessoa):
    def alterarFiscal(self):
        if (self == " "):
            print("Não existe fiscal que possa ser editado!")
        else:
            self.nome = input("Digite o nome do fiscal: ")
            self.data = input("Digite a data de nascimento do fiscal: ")
            self.genero = input("Digite o gênero do fiscal: ")
        return self

class Ponto:
    def __init__(self, nome, rua, bairro):
        self.nome = nome
        self.rua = rua
        self.bairro = bairro

    def __str__(self):
        return f"Nome: { self.nome }\
                \nRua: { self.rua }\
                \nBairro: { self.bairro }"
    
    def alterarPonto(self):
        self.nome = input("Digite o nome do ponto de parada: ")
        self.rua = input("Digite a rua do ponto de parada: ")
        self.bairro = input("Digite o bairro do potno de parada: ")
        return self

class Onibus:
    def __init__(self, placa, modelo, motorista):
        self.placa = placa
        self.modelo = modelo
        self.rota = []
        self.motorista = motorista
        self.fiscal = " "
        self.passagem = 0.2*len(self.rota)
    
    def __str__(self):
        return f"Placa: { self.placa }\
                \nModelo: { self.modelo }\
                \nMotorista: { self.motorista }\
                \nFiscal: { self.fiscal }\
                \nValor: R$ { self.passagem }"

    def adicionarMotorista(self, motorista):
        print("O motorista foi removido do ônibus e movido para realocação!")
        motoristaRemovido = self.motorista
        self.motorista = motorista
        print("O novo motorista foi adicionado ao ônibus e saiu da realocação!")
        return motoristaRemovido

    def adicionarFiscal(self, fiscal):
        if (self.motorista != " "):
            pass
        else:
            print("O motorista foi removido do ônibus e movido para realocação!")
            fiscalRemovido = self.motorista
        self.fiscal = fiscal
        print("O novo fiscal foi adicionado ao ônibus e saiu da realocação!")
        return fiscalRemovido
    
    def adicionarPonto(self, idponto, ponto):
        self.rota.insert(idponto, ponto)

    def alterarDados(self):
        self.placa = input("Digite a placa do ônibus: ")
        self.modelo = input("Digite o modelo do onibus: ")

    def valorPassagem(self):#Utilizada para atualizar o valor da passagem
        self.passagem = 0.2*len(self.rota)