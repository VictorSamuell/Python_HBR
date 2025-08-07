# # with open("meu_arquivo.txt", "w", encoding="utf-8") as arquivo:
# #     arquivo.write("Olá Olá, mundo\n")
# #     arquivo.write("Segunda Linha\n")

# # with open("meu_arquivo.txt", "a", encoding="utf-8") as arquivo:
# #      arquivo.write("    Oá, undo\n")
# #      arquivo.write("Essa Linha\n")

# # with open("meu_arquivo.txt", "r", encoding="utf-8") as arquivo:
# #     conteudo_completo = arquivo.readlines()
# #     print(f"{conteudo_completo}")

# # with open("meu_arquivo.txt", "r", encoding="utf-8") as arquivo:
# #     for linha in arquivo:
# #         print(f"{linha.strip()}")

# # erro = True

# # while erro == True :
# #     try:
# #         idade = int(input("Digite sua idade: "))
# #         erro = False
# #         print(f"Voce tem {idade} anos!")
        
# #     except:
# #         print("Erro: Você não digitou um número válido")
# #         erro = True

# # print("O programa continua...")


# while True:
#     try:
#         num = int(input("Digite um numero para dividir 10: "))
#         resultado = 10 / num
#         print(f"O resultado é {resultado}")
#         break
#     except Exception as e:
#         print(f"Ocorreu um erro inesperado: {e}")

from datetime import datetime

erro = True
while erro == True :
    try:
        mensagem = input("Digite a mensagem para o log : ")
        erro = False
        with open("aula11/log.txt", "a", encoding="utf-8") as arquivasso:
            formatted_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            arquivasso.write(f"\n{formatted_data}: {mensagem}")
        
    except Exception as e:
        print(f"Erro: {e}")
        erro = True
    
    try:
        with open("aula11/log.txt", "r", encoding="utf-8") as arq:
            for linha in arq:
                print(f"{linha.strip()}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


    try:
        with open("config.txt", "r", encoding="utf-8") as arq:
            for linha in arq:
                print(f"{linha}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")