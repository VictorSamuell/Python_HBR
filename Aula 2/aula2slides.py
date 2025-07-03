# Ex 1
nome_completo = input("Digite o nome completo : ")

nome_maiusculo = nome_completo.upper()

cidade = input("Digite a Cidade: ")
cidade.strip().capitalize()

print(f"Nome Completo Maiusculo : {nome_completo.upper()}")

print(f"Nome Completo Minusculo : {nome_completo.lower()}")

cidade_sem_espaço = cidade.replace(" ", "")
print(f"Sua cidade é {cidade}")
print(f"Numero de letras : {len(cidade_sem_espaço.strip())}")

nome_sem_espaço = nome_completo.replace(" ", "")
print(nome_sem_espaço)
print(f"quntd de caracteres do nome : {len(nome_sem_espaço.strip())}")



# Ex 2

idade = int(input("Digite sua idade : "))

if idade >= 0 and idade < 12:
    print("Criança")
elif idade >= 13 and idade < 17:
    print("Adolescência")
else:
    print("Adulto")



# Ex 3

USUARIO_CORRETO = "admin"
SENHA_CORRETA = "12345"

user = input("Digite o Usuario : ")
password = input("Digite a senha : ")

if user == USUARIO_CORRETO and password == SENHA_CORRETA:
    print(f"Login Bem Sucedido")
elif user != USUARIO_CORRETO and password == SENHA_CORRETA:
    print("Usuário Invalido")
else:
    print("Senha Incorreta")

# Ex 4

CREDITO = int(input("Credito : "))
RENDA = float(input("Renda : "))

if CREDITO > 600 and RENDA >= 2500:
    print("Aprovado")
else:
    print("Recusado")

TIPO_CONVITE = input()
IDADE = int(input())

if TIPO_CONVITE.lower() == "vip" or IDADE >= 18:
    print("Liberado")
else:
    print("Negado")

