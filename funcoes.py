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
        var = dicionarioFiscais.get(i, comando = "ID disponível!")
    dicionarioFiscais[i] = Fiscal(i, nome, data, genero)

#Funções de relacionar
def relacionarMotorista():
    nome = input("Digite o nome do motorista: ")
    placa = input("Digite a placa do ônibus: ")
    motorista = dicionarioMotoristas[nome]
    onibus = dicionarioOnibus[placa]
    onibus.motorista = motorista
    dicionarioOnibus[placa] = onibus
def relacionarFiscal():
    nome = input("Digite o nome do fiscal: ")
    placa = input("Digite a placa do ônibus: ")
    fiscal = dicionarioFiscais[nome]
    onibus = dicionarioOnibus[placa]
    onibus.fiscal = fiscal
    dicionarioOnibus[placa] = onibus
def relacionarPonto():
    nome = input("Digite o nome do ponto de parada: ")
    placa = input("Digite a placa do ônibus: ")
    ponto = dicionarioPontos[nome]
    onibus = dicionarioOnibus[placa]
    onibus.pontos[nome] = ponto
    dicionarioOnibus[onibus.nome] = onibus