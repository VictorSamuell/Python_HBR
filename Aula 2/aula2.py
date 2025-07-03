senhas = ["12345"]
novas_senhas = []
continuar = True

senha = input("Digite a Nova Senha : ")
confirmar = input("Confirme a Nova Senha : ")


if senha != confirmar:
     print("Senha e Confirmar senha não se assemelham")
elif senha == senhas[0]:
    print("Não é permitido utilizar senhas antigas")
else:
    print("Senha alterada")
    senhas[0] = senha


while continuar == True:

    senha_nova = input("Digite a Nova Senha : ")
    confirmar_senha = input("Confirme a Nova Senha : ")


    if senha_nova != confirmar_senha:
        print("Senha e Confirmar senha não se assemelham")
    else:
        print("Nova Senha")
        novas_senhas.append(senha_nova)

    print("1 - CONTINUAR")
    print("2 - SAIR ")
    res = int(input("Escolha uma opção : "))
    if res == 2:
        continuar = False

print(senhas)
print(novas_senhas)