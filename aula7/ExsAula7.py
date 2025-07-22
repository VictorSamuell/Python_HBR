def limpar_terminal():
    import os
    import platform

    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


# Exercícios Práticos - Python: Escopo, Argumentos, *args e **kwargs
# Exercício 1 – Escopo Global vs. Local
# Enunciado:
# Observe o código abaixo e responda:

# mensagem = "Olá, mundo!"

# def modificar_mensagem():
#     mensagem = "Olá do escopo local!"
#     print("Dentro da função:", mensagem)

# modificar_mensagem()
# print("Fora da função:", mensagem)


# Pergunta: Por que o valor da variável mensagem fora da função não foi alterado?


# -- --  Resposta: Porque dentro da função foi criada uma nova variável mensagem, que é local à função. A variável global não foi alterada. -- -- 




# Exercício 2 – Modificando Variável Global
# Enunciado:
# Altere o código abaixo para que a função realmente altere o valor da variável global contador:
limpar_terminal()

print("Exercício 2")

def incrementar(contador):
    contador += 1
    return contador


cont = incrementar(0)
print(cont)














# Exercício 3 – Argumentos Nomeados
# Enunciado:
# Escreva uma função chamada exibir_informacoes que receba os argumentos nome, idade e cidade,
# e imprima:

# Nome: João
# Idade: 30
# Cidade: São Paulo

# Chame a função usando argumentos nomeados, fora da ordem definida.
print("\n")
print("Exercício 3")

def exibir_informacoes(nome, idade, cidade):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Cidade: {cidade}")

print("Usando argumentos ordenados:")
exibir_informacoes("João", 30 , "São Paulo")
print("Usando argumentos nomeados:")
exibir_informacoes(cidade="São Paulo", nome="João", idade=30)













# Exercício 4 – Uso de *args
# Enunciado:
# Crie uma função chamada somar_todos que aceita qualquer quantidade de números como argumento e retorna a soma de todos eles.

print("\n")
print("Exercício 4")

def somar(*numeros):
    total = 0

    for numero in numeros:
        total += numero

    return total

print(somar(1,2,3,4,5,6))











# Exercício 5 – Uso de **kwargs
# Enunciado:
# Crie uma função chamada exibir_usuario que aceita qualquer quantidade de informações sobre um usuário,
# e imprime no formato:

# nome: Alice
# idade: 25
# profissão: Engenheira

# Use **kwargs.
print("\n")
print("Exercício 5")

def exibir_usuario(**info):
    for chave, valor in info.items():
        print(f"{chave}: {valor}")

exibir_usuario(nome="Alice", idade=25, profissao="Engenharia")