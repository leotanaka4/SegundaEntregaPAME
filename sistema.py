print("Bem vindo a rede de transportes!")

print("O que você deseja fazer?")

comando=""

while (comando != "Sair"):
    a = input("Digite Criar/Mostrar/Relacionar/Alterar/Deletar/Sair\n")
    b=""
    if (a == "Criar"):
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
    elif(a == "Mostrar"):
        b = input("Digite Ônibus/Rota/Motoristas/Fiscais\n")
        if (b == "Ônibus"):
            pass
        elif (b == "Rota"):
            pass
        elif (b == "Motoristas"):
            pass
        elif (b == "Fiscal"):
            pass
        else:
            print("Essa opção não existe!")
    elif(a == "Relacionar"):
        b = input("Digite Motorista/Fiscal/Ponto\n")
        if (b == "Motorista"):
            pass
        elif (b == "Fiscal"):
            pass
        elif (b == "Ponto"):
            pass
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