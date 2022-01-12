from funcoes import *

print("Bem vindo a rede de transportes!\nO que você deseja fazer?")

comando=""

while (comando != "Sair"):
    a = input("Que ação você deseja tomar (Criar/Mostrar/Relacionar/Alterar/Deletar/Sair)?\n")
    b=""
    if (a == "Criar"):
        b = input("Digite uma das seguintes opções (Ônibus/Ponto/Motorista/Fiscal):\n")
        if (b == "Ônibus"):
            criarOnibus()
        elif (b == "Ponto"):
            criarPonto()
        elif (b == "Motorista"):
            criarMotorista()
        elif (b == "Fiscal"):
            criarFiscal()
        else:
            print("Essa opção não existe!")
    elif(a == "Mostrar"):
        b = input("Digite uma das seguintes opções (Ônibus/Rotas/Motoristas/Fiscais):\n")
        if (b == "Ônibus"):
            for idonibus in dicionarioOnibus:
                print(dicionarioOnibus[idonibus])
        elif (b == "Rotas"):
            for idponto in dicionarioPontos:
                print(dicionarioPontos[idponto])
        elif (b == "Motoristas"):
            for idmotorista in dicionarioMotoristas:
                print(dicionarioMotoristas[idmotorista])
        elif (b == "Fiscais"):
            for idfiscal in dicionarioFiscais:
                print(dicionarioFiscais[idfiscal])
        else:
            print("Essa opção não existe!")
    elif(a == "Relacionar"):
        b = input("Digite uma das seguintes opções (Motorista/Fiscal/Ponto):\n")
        if (b == "Motorista"):
            relacionarMotorista()
        elif (b == "Fiscal"):
            relacionarFiscal()
        elif (b == "Ponto"):
            relacionarPonto()
        else:
            print("Essa opção não existe!")
    elif(a == "Alterar"):
        b = input("Digite uma das seguintes opções ()Ônibus/Ponto/Motorista/Fiscal/Rota):\n")
        if (b == "Ônibus"):
            alterarOnibus()
        elif (b == "Ponto"):
            alterarPonto()
        elif (b == "Motorista"):
            alterarMotorista()
        elif (b == "Fiscal"):
            alterarFiscal()
        elif (b == "Rota"):
            pass
            alterarRota()
        else:
            print("Essa opção não existe!")
    elif(a == "Deletar"):
        b = input("Digite uma das seguintes opções (Ônibus/Ponto/Motorista/Fiscal):\n")
        if (b == "Ônibus"):
            deletarOnibus()
        elif (b == "Ponto"):
            deletarPonto()
        elif (b == "Motorista"):
            deletarMotorista()
        elif (b == "Fiscal"):
            deletarFiscal()
        else:
            print("Essa opção não existe!")
    elif(a == "Sair"):
        comando = a
    else:
        print("Essa opção não existe!")