from funcoes import *

print("Bem vindo a rede de transportes!\nO que você deseja fazer?")

comando=""

while (comando != "Sair"):
    a = input("Digite Criar/Mostrar/Relacionar/Alterar/Deletar/Sair\n")
    b=""
    if (a == "Criar"):
        b = input("Digite Ônibus/Ponto/Motorista/Fiscal\n")
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
        b = input("Digite Ônibus/Rotas/Motoristas/Fiscais\n")
        if (b == "Ônibus"):
            print(dicionarioOnibus)
        elif (b == "Rotas"):
            print(dicionarioPontos)
        elif (b == "Motoristas"):
            print(dicionarioMotoristas)
        elif (b == "Fiscal"):
            print(dicionarioFiscais)
        else:
            print("Essa opção não existe!")
    elif(a == "Relacionar"):
        b = input("Digite Motorista/Fiscal/Ponto\n")
        if (b == "Motorista"):
            relacionarMotorista()
        elif (b == "Fiscal"):
            relacionarFiscal()
        elif (b == "Ponto"):
            relacionarPonto()
        else:
            print("Essa opção não existe!")
    elif(a == "Alterar"):
        b = input("Digite Ônibus/Ponto/Motorista/Fiscal/Rota\n")
        if (b == "Ônibus"):
            pass
        elif (b == "Ponto"):
            pass
        elif (b == "Motorista"):
            pass
        elif (b == "Fiscal"):
            pass
        elif (b == "Rota"):
            pass
        else:
            print("Essa opção não existe!")
    elif(a == "Deletar"):
        b = input("Digite Ônibus/Ponto/Motorista/Fiscal\n")
        if (b == "Ônibus"):
            pass
        elif (b == "Ponto"):
            pass
        elif (b == "Motorista"):
            pass
        elif (b == "Fiscal"):
            pass
        else:
            print("Essa opção não existe!")
    elif(a == "Sair"):
        comando = a
    else:
        print("Essa opção não existe!")