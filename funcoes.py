from classes import *

dicionarioOnibus = {} #Dicionário com ônibus
dicionarioPontos = {} #Pontos de parada não utilizados
dicionarioMotoristas = {} #Motoristas não utilizados
dicionarioFiscais = {} #Fiscais não utilizados

#Funções de criar
def criarOnibus():
    placa = input("Digite a placa do ônibus: ")
    modelo = input("Digite o modelo do ônibus: ")
    #Já que todo ônibus precisa de motorista
    nome = input("Digite o nome do motorista: ")
    data = input("Digite a data de nascimento do motorista: ")
    genero = input("Digite o gênero do motorista: ")
    comando = " "
    idonibus = 0
    while (comando != "ID disponível!"):
        idonibus += 1
        comando = dicionarioOnibus.get(idonibus,"ID disponível!")
    dicionarioOnibus[idonibus] = Onibus(placa, modelo, Motorista(nome, data, genero))
    print("ID do ônibus: "+str(idonibus))
def criarPonto():
    nome = input("Digite o nome do ponto de parada: ")
    rua = input("Digite a rua do ponto de parada: ")
    bairro = input("Digite o bairro do ponto de parada: ")
    comando = " "
    idponto = 0
    while (comando != "ID disponível!"):
        idponto += 1
        comando = dicionarioPontos.get(idponto, "ID disponível!")
    dicionarioPontos[idponto] = Ponto(nome, rua, bairro)
    print("ID do ponto: "+str(idponto))
def criarMotorista():
    nome = input("Digite o nome do motorista: ")
    data = input("Digite a data de nascimento do motorista: ")
    genero = input("Digite o gênero do motorista: ")
    comando = " "
    idmotorista = 0
    while (comando != "ID disponível!"):
        idmotorista += 1
        comando = dicionarioMotoristas.get(idmotorista, "ID disponível!")
    dicionarioMotoristas[idmotorista] = Motorista(nome, data, genero)
    print("ID do motorista: "+str(idmotorista))
def criarFiscal():
    nome = input("Digite o nome do fiscal: ")
    data = input("Digite a data de nascimento do fiscal: ")
    genero = input("Digite o gênero do fiscal: ")
    comando = " "
    idfiscal = 0
    while (comando != "ID disponível!"):
        idfiscal += 1
        comando = dicionarioFiscais.get(idfiscal, "ID disponível!")
    dicionarioFiscais[idfiscal] = Fiscal(nome, data, genero)
    print("ID do fiscal: "+str(idfiscal))

#Funções de relacionar
def relacionarMotorista():
    idmotorista = input("Digite o ID do motorista: ")
    idonibus = input("Digite o ID do ônibus: ")
    motorista = dicionarioMotoristas[idmotorista]
    onibus = dicionarioOnibus[idonibus]
    dicionarioMotoristas[idmotorista] = onibus.adicionarMotorista(motorista)
    dicionarioOnibus[idonibus] = onibus
def relacionarFiscal():
    idfiscal = input("Digite o ID do fiscal: ")
    idonibus = input("Digite o ID do ônibus: ")
    fiscal = dicionarioFiscais[idfiscal]
    onibus = dicionarioOnibus[idonibus]
    dicionarioFiscais[idfiscal] = onibus.adicionarFiscal(fiscal)
    dicionarioOnibus[idonibus] = onibus
def relacionarPonto():
    idponto = input("Digite o ID do ponto de parada: ")
    idonibus = input("Digite o ID do ônibus: ")
    ponto = dicionarioPontos[idponto]
    onibus = dicionarioOnibus[idonibus]
    onibus.adicionarPonto(idponto, ponto)
    dicionarioOnibus[idonibus] = onibus

#Funções de alterar
def alterarOnibus():
    idonibus = int(input("Digite o ID do ônibus: "))
    onibus = dicionarioOnibus[idonibus]
    onibus.alterarDados()#Altera somente placa e modelo
def alterarPonto():
    identidade = int(input("Digite o ID do ponto de parada: "))
    ponto = dicionarioPontos[identidade]
    dicionarioPontos[identidade] = ponto.alterarPonto()#Altera somente pontos de parada não utilizados
def alterarMotorista():
    resposta = input("Você deseja alterar um motorista Ativado ou Desativado? ")
    if (resposta == "Ativado"):
        idonibus = int(input("Digite o ID do ônibus: "))
        onibus = dicionarioOnibus[idonibus]
        onibus.motorista = onibus.motorista.alterarMotorista()
        dicionarioOnibus[idonibus] = onibus
    elif (resposta == "Desativado"):
        idmotorista = input("Digite o ID do motorista: ")
        motorista = dicionarioMotoristas[idmotorista]
        dicionarioMotoristas[idmotorista] = motorista.alterarMotorista()
    else:
        print("Não foi feita alteração!")
def alterarFiscal():
    resposta = input("Você deseja alterar um fiscal Ativado ou Desativado? ")
    if (resposta == "Ativado"):
        idonibus = int(input("Digite o ID do ônibus: "))
        onibus = dicionarioOnibus[idonibus]
        onibus.fiscal = onibus.fiscal.alterarFiscal()
        dicionarioOnibus[idonibus] = onibus
    elif (resposta == "Desativado"):
        idfiscal = int(input("Digite o ID do fiscal: "))
        fiscal = dicionarioFiscais[idfiscal]
        dicionarioFiscais[fiscal] = fiscal.alterarFiscal()
    else:
        print("Não foi feita alteração!")
def alterarRota():
    idonibus = int(input("Digite o ID do ônibus com a rota que deseja alterar: "))
    onibus = dicionarioOnibus[idonibus]
    for ponto in onibus.rota:
        print(ponto)
        resposta = input("Deseja Alterar/Remover/Manter esse ponto de parada? ")
        if (resposta == "Alterar"):
            comando = " "
            idponto = 0
            while (comando != "ID disponível!"):
                idponto += 1
                comando = dicionarioPontos.get(idponto, "ID disponível!")
            dicionarioPontos[idponto] = onibus.rota.pop(ponto)
            idponto = int(input("Digite o ID do ponto de parada que deseja usar: "))
            onibus.adicionarPonto(idponto, dicionarioPontos.pop(idponto))
            print("ID do ponto de parada:"+str(idponto))
        elif (resposta == "Remover"):
            comando = " "
            idponto = 0
            while (comando != "ID disponível!"):
                idponto += 1
                comando = dicionarioPontos.get(idponto, "ID disponível!")
            dicionarioPontos[idponto] = onibus.rota.pop(ponto)
            print("ID do ponto de parada:"+str(idponto))
    dicionarioOnibus[idonibus] = onibus

#Funções de deletar
def deletarOnibus():
    idonibus = int(input("Digite o ID do ônibus: "))
    onibus = dicionarioOnibus[idonibus]
    for ponto in onibus.rota:
        comando = " "
        idponto = 0
        while (comando != "ID disponível!"):
            idponto += 1
            comando = dicionarioPontos.get(idponto, "ID disponível!")
        dicionarioPontos[idponto] = ponto
    comando = " "
    idmotorista = 0
    while (comando != "ID disponível!"):
        idmotorista += 1
        comando = dicionarioMotoristas.get(idmotorista, "ID disponível!")
    dicionarioMotoristas[idmotorista] = onibus.motorista
    if (onibus.fiscal != " "):
        comando = " "
        idfiscal = 0
        while (comando != "ID disponível!"):
            idfiscal += 1
            comando = dicionarioFiscais.get(idfiscal, "ID disponível!")
        dicionarioFiscais[idfiscal] = onibus.fiscal
def deletarPonto():
    idponto = int(input("Digite o ID do ponto de parada: "))
    dicionarioPontos.pop(idponto)#Não é possível remover pontos utilizados
def deletarMotorista():
    idmotorista = int(input("Digite o ID do motorista: "))
    dicionarioMotoristas.pop(idmotorista)#Não é possível remover um motorista ativado para seguir lógica proposta
def deletarFiscal():
    resposta = input("Você deseja alterar um fiscal Ativado ou Desativado? ")
    if (resposta == "Ativado"):
        idonibus = int(input("Digite o id do ônibus: "))
        onibus = dicionarioOnibus[idonibus]
        onibus.fiscal = " "
    elif (resposta == "Desativado"):
        idfiscal = int(input("Digite o ID do fiscal: "))
        dicionarioFiscais.pop(idfiscal)