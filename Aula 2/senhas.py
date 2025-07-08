senhas = list(map(str, input("Digite as senhas separadas por espaço : ").split()))
print(senhas)


for i in range(len(senhas)):
    continuar = True
    while continuar == True:
        print(f"Senha {i+1}")
        nova_senha = input("Digite a nova senha: ")
        confirmar_nova_senha = input("Confirme a senha : ")

        if nova_senha == senhas[i]:

            print("Senha Igual a Antiga")
            print("1 - CONTINUAR")
            print("2 - SAIR ")
            res = int(input("Escolha uma opção : "))
            if res == 2:
                continuar = False

        elif confirmar_nova_senha != nova_senha:
            print("Senha não condiz com o 'Confirmar Senha'")
            print("1 - CONTINUAR")
            print("2 - SAIR ")
            res = int(input("Escolha uma opção : "))
            if res == 2:
                continuar = False

        else:
            senhas[i] = nova_senha
            continuar = False

print(senhas)

    