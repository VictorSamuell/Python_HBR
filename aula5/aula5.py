# senha_salva = "python123"   
# senha_certa = False

# while senha_certa == False:
#     senha = input("Digite a senha : ")  
#     if senha == senha_salva:
#         senha_certa = True
#         print("Acesso permitido")
#     else:
#         print("Senha incorreta")
    



tentativas = 0
numero_secreto = 25
chute = 0

while chute != numero_secreto:
    print(f"\033[1;32mTente adviinhar qual o numero secreto\033[m ")
    chute = int(input(f"\033[1;34mTentativa {tentativas+1}:\033[m"))
#\033[1;32m}\033[m
    if chute > numero_secreto:
        print("\033[1;31mChute é maior que o numero secreto\033[m")
    elif chute < numero_secreto:
        print("\033[1;31mChute é menor que o numero secreto \033[m")
    tentativas += 1

    if tentativas == 3:
        print("\033[1;33mUm feriado muito aclamado acontece nesse dia\033[m")
    
    if tentativas == 5:
        print("\033[1;33mÉ um quadrado perfeito\033[m")

print(f"\033[1;33mParabéns você acertou\033[m")
print(f"\033[1;33mForam necessárias {tentativas} tentativas\033[m")
















