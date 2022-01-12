from funcoes import *

print("Bem vindo a rede de transportes!\nO que você deseja fazer?")

comando=""

while (comando != "Sair"):
    acao = input("Que ação você deseja tomar (Criar/Mostrar/Relacionar/Alterar/Deletar/Sair)?\n")
    opcao= " "
    if (acao == "Criar"):
        opcao = input("Digite uma das seguintes opções (Ônibus/Ponto/Motorista/Fiscal):\n")
        if (opcao == "Ônibus"):
            criarOnibus()
        elif (opcao == "Ponto"):
            criarPonto()
        elif (opcao == "Motorista"):
            criarMotorista()
        elif (opcao == "Fiscal"):
            criarFiscal()
        else:
            print("Essa opção não existe!")
    elif(acao == "Mostrar"):
        opcao = input("Digite uma das seguintes opções (Ônibus/Rotas/Motoristas/Fiscais):\n")
        if (opcao == "Ônibus"):
            for idonibus in dicionarioOnibus:
                print(dicionarioOnibus[idonibus])
        elif (opcao == "Rotas"):
            for idponto in dicionarioPontos:
                print(dicionarioPontos[idponto])
        elif (opcao == "Motoristas"):
            for idmotorista in dicionarioMotoristas:
                print(dicionarioMotoristas[idmotorista])
        elif (opcao == "Fiscais"):
            for idfiscal in dicionarioFiscais:
                print(dicionarioFiscais[idfiscal])
        else:
            print("Essa opção não existe!")
    elif(acao == "Relacionar"):
        opcao = input("Digite uma das seguintes opções (Motorista/Fiscal/Ponto):\n")
        if (opcao == "Motorista"):
            relacionarMotorista()
        elif (opcao == "Fiscal"):
            relacionarFiscal()
        elif (opcao == "Ponto"):
            relacionarPonto()
        else:
            print("Essa opção não existe!")
    elif(acao == "Alterar"):
        opcao = input("Digite uma das seguintes opções (Ônibus/Ponto/Motorista/Fiscal/Rota):\n")
        if (opcao == "Ônibus"):
            alterarOnibus()
        elif (opcao == "Ponto"):
            alterarPonto()
        elif (opcao == "Motorista"):
            alterarMotorista()
        elif (opcao == "Fiscal"):
            alterarFiscal()
        elif (opcao == "Rota"):
            alterarRota()
        else:
            print("Essa opção não existe!")
    elif(acao == "Deletar"):
        opcao = input("Digite uma das seguintes opções (Ônibus/Ponto/Motorista/Fiscal):\n")
        if (opcao == "Ônibus"):
            deletarOnibus()
        elif (opcao == "Ponto"):
            deletarPonto()
        elif (opcao == "Motorista"):
            deletarMotorista()
        elif (opcao == "Fiscal"):
            deletarFiscal()
        else:
            print("Essa opção não existe!")
    elif(acao == "Sair"):
        comando = acao
    else:
        print("Essa opção não existe!")