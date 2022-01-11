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
    onibus.adicionarPonto(identidade1, ponto)
    dicionarioOnibus[identidade2] = onibus

#Funções de alterar
def alterarOnibus():
    identidade = input("Digite o id do onibus: ")
    onibus = dicionarioOnibus[identidade]
    onibus.placa = input("Digite a placa do ônibus: ")
    onibus.modelo = input("Digite o modelo do onibus: ")
    #alterar pontos
    #alterar motorista
    #alterar fiscal
    dicionarioOnibus[identidade] = onibus
def alterarPonto():
    identidade = input("Digite o id do ponto de parada: ")
    ponto = dicionarioPontos[identidade]
    ponto.nome = input("Digite o nome do ponto de parada: ")
    ponto.rua = input("Digite a rua do ponto de parada: ")
    ponto.bairro = input("Digite o bairro do potno de parada: ")
    dicionarioPontos[identidade] = ponto
    #gerar conexão com onibus
def alterarMotorista():
    identidade = input("Digite o id do motorista: ")
    motorista = dicionarioMotoristas[identidade]
    motorista.nome = input("Digite o nome do motorista: ")
    motorista.data = input("Digite a data de nascimento do motorista: ")
    motorista.genero = input("Digite o gênero do fiscal: ")
    dicionarioMotoristas[identidade] = motorista
    #gerar conexão com onibus
def alterarFiscal():
    identidade = input("Digite o id do fiscal: ")
    fiscal = dicionarioFiscais[identidade]
    fiscal.nome = input("Digite o nome do fiscal: ")
    fiscal.data = input("Digite a data de nascimento do fiscal: ")
    fiscal.genero = input("Digite o gênero do fiscal: ")
    dicionarioFiscais[identidade] = fiscal
    #gerar conexão com onibus
#Alterar rota ainda não pensada

#Funções de deletar
def deletarOnibus():
    identidade = input("Digite o id do ônibus: ")
    deletado = dicionarioOnibus.pop(identidade)
def deletarPonto():
    identidade = input("Digite o id do ponto de parada: ")
    deletado = dicionarioPontos.pop(identidade)
def deletarMotorista():
    identidade = input("Digite o id do motorista: ")
    deletado = dicionarioMotoristas.pop(identidade)
def deletarFiscal():
    identidade = input("Digite o id do fiscal: ")
    deletado = dicionarioFiscais.pop(identidade)