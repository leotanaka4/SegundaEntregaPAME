from classes import *

dicionarioOnibus = {}
dicionarioPontos = {}
dicionarioMotoristas = {}
dicionarioFiscais = {}

#Funções de criar
def criarOnibus():
    placa = input("Digite a placa do ônibus: ")
    modelo = input("Digite o modelo do ônibus: ")
    #Já que todo ônibus precisa de motorista
    nome = input("Digite o nome do motorista: ")
    data = input("Digite a data de nascimento do motorista: ")
    genero = input("Digite o gênero do motorista: ")
    comando = " "
    i = 0
    while (comando != "ID disponível!"):
        i += 1
        comando = dicionarioOnibus.get(i,"ID disponível!")
    j = 0
    while (comando != "ID disponível!"):
        j += 1
        comando = dicionarioMotoristas.get(j, "ID disponível!")
    dicionarioMotoristas[j] = Motorista(i, nome, data, genero)
    dicionarioOnibus[i] = Onibus(placa, modelo, dicionarioMotoristas[nome])
def criarPonto():
    nome = input("Digite o nome do ponto de parada: ")
    rua = input("Digite a rua do ponto de parada: ")
    bairro = input("Digite o bairro do ponto de parada: ")
    comando = " "
    i = 0
    while (comando != "ID disponível!"):
        i += 1
        comando = dicionarioPontos.get(i, "ID disponível!")
    dicionarioPontos[i] = Ponto(i, nome, rua, bairro)
def criarMotorista():
    nome = input("Digite o nome do motorista: ")
    data = input("Digite a data de nascimento do motorista: ")
    genero = input("Digite o gênero do motorista: ")
    comando = " "
    i = 0
    while (comando != "ID disponível!"):
        i += 1
        comando = dicionarioMotoristas.get(i, "ID disponível!")
    dicionarioMotoristas[i] = Motorista(i, nome, data, genero)
def criarFiscal():
    nome = input("Digite o nome do fiscal: ")
    data = input("Digite a data de nascimento do fiscal: ")
    genero = input("Digite o gênero do fiscal: ")
    comando = " "
    i = 0
    while (comando != "ID disponível!"):
        i += 1
        comando = dicionarioFiscais.get(i, "ID disponível!")
    dicionarioFiscais[i] = Fiscal(i, nome, data, genero)

#Funções de relacionar
def relacionarMotorista():
    identidade1 = input("Digite o id do motorista: ")
    identidade2 = input("Digite o id do ônibus: ")
    motorista = dicionarioMotoristas[identidade1]
    onibus = dicionarioOnibus[identidade2]
    onibus.adicionarMotorista(motorista)
    dicionarioOnibus[identidade2] = onibus
def relacionarFiscal():
    identidade1 = input("Digite o id do fiscal: ")
    identidade2 = input("Digite o id do ônibus: ")
    fiscal = dicionarioFiscais[identidade1]
    onibus = dicionarioOnibus[identidade2]
    onibus.adicionarFiscal(fiscal)
    dicionarioOnibus[identidade2] = onibus
def relacionarPonto():
    identidade1 = input("Digite o id da parada: ")
    identidade2 = input("Digite o id do ônibus: ")
    ponto = dicionarioPontos[identidade1]
    onibus = dicionarioOnibus[identidade2]
    onibus.adicionarPonto(ponto)
    dicionarioOnibus[identidade2] = onibus