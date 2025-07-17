import os

def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')

limpar_terminal()

def calculadora(a, b):
    
    ciclo = False

    while ciclo == False:

        operacao = input("Qual operação você deseja realizar? : ")
        operacao = operacao.lower()
        

        if b == 0 and (operacao == "divisao" or operacao == "divisão"):
            print("Na divisão o denominador não pode ser 0")
            b = int(input("Digite o Numero 2 : "))

        if operacao == "soma":
            ciclo = True
            print(f"Você escolheu {operacao}")
            return a + b
        elif operacao == "subtracao" or operacao == "subtração":
            ciclo = True
            print(f"Você escolheu {operacao}")
            return a - b
        
        elif operacao == "multiplicacao" or operacao == "multiplicação":
            ciclo = True
            print(f"Você escolheu {operacao}")
            return a * b
        
        elif operacao == "divisao" or operacao == "divisão":
            ciclo = True
            print(f"Você escolheu {operacao}")
            return a / b
        
        else:
            ciclo = False
            print("Operação Invalida")
    

def mostrarMenu():
    num1 = int(input("Numero 1 : "))
    num2 = int(input("Numero 2 : "))

    result = calculadora(num1, num2)

    print(f"Resultado : {result}")


mostrarMenu()



def eh_maior_de_idade(idade):
    if idade >= 18:
        return True
    else:
        return False
    
age = int(input("Qual a sua idade : "))
verificador = eh_maior_de_idade(age)

if verificador:
    print(f"Acesso Permitido")
else:
    print(f"Acesso Negado")
