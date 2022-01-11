from classes import *

dicionarioOnibus = {}
dicionarioPontos = {}
dicionarioMotoristas = {}
dicionarioFiscais = {}

def criarOnibus():
    x = Onibus()
    x.motorista = Motorista()
    x.placa = input("Digite a placa do ônibus: ")
    x.modelo = input("Digite o modelo do ônibus: ")
    #Já que todo ônibus precisa de motorista
    x.motorista.nome = input("Digite o nome do motorista: ")
    x.motorista.data = input("Digite a data de nascimento do motorista: ")
    x.motorista.genero = input("Digite o gênero do motorista: ")
    dicionarioOnibus[x.placa] = x
    dicionarioMotoristas[x.motorista.nome] = x.motorista


def criarPonto():
    x = Ponto()
    x.nome = input("Digite o nome do ponto de parada: ")
    x.rua = input("Digite a rua do ponto de parada: ")
    x.bairro = input("Digite o bairro do ponto de parada: ")
    dicionarioPontos[x.nome] = x

def criarMotorista():
    x = Motorista()
    x.nome = input("Digite o nome do motorista: ")
    x.data = input("Digite a data de nascimento do motorista: ")
    x.genero = input("Digite o gênero do motorista: ")
    dicionarioMotoristas[x.nome] = x

def criarFiscal():
    x = Motorista()
    x.nome = input("Digite o nome do fiscal: ")
    x.data = input("Digite a data de nascimento do fiscal: ")
    x.genero = input("Digite o gênero do fiscal: ")
    dicionarioFiscais[x.nome] = x

print("Bem vindo a rede de transportes!\nO que você deseja fazer?")

comando=""

while (comando != "Sair"):
    a = input("Digite Criar/Mostrar/Relacionar/Alterar/Deletar/Sair\n")
    b=""
    if (a == "Criar"):
        b = input("Digite Ônibus/Ponto/Motorista/Fiscal\n")
        if (b == "Ônibus: "):
            criarOnibus()
        elif (b == "Ponto: "):
            criarPonto()
        elif (b == "Motorista: "):
            criarMotorista()
        elif (b == "Fiscal: "):
            criarFiscal()
        else:
            print("Essa opção não existe!")
    elif(a == "Mostrar"):
        b = input("Digite Ônibus/Rotas/Motoristas/Fiscais\n")
        if (b == "Ônibus: "):
            pass
        elif (b == "Rotas: "):
            pass
        elif (b == "Motoristas: "):
            pass
        elif (b == "Fiscal: "):
            pass
        else:
            print("Essa opção não existe!")
    elif(a == "Relacionar"):
        b = input("Digite Motorista/Fiscal/Ponto\n")
        if (b == "Motorista: "):
            pass
        elif (b == "Fiscal: "):
            pass
        elif (b == "Ponto: "):
            pass
        else:
            print("Essa opção não existe!")
    elif(a == "Alterar"):
        b = input("Digite Ônibus/Ponto/Motorista/Fiscal/Rota\n")
        if (b == "Ônibus: "):
            pass
        elif (b == "Ponto: "):
            pass
        elif (b == "Motorista: "):
            pass
        elif (b == "Fiscal: "):
            pass
        elif (b == "Rota: "):
            pass
        else:
            print("Essa opção não existe!")
    elif(a == "Deletar"):
        b = input("Digite Ônibus/Ponto/Motorista/Fiscal\n")
        if (b == "Ônibus: "):
            pass
        elif (b == "Ponto: "):
            pass
        elif (b == "Motorista: "):
            pass
        elif (b == "Fiscal: "):
            pass
        else:
            print("Essa opção não existe!")
    elif(a == "Sair"):
        comando = a
    else:
        print("Essa opção não existe!")