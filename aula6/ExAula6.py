# # Exercício 1 – Saudação Personalizada
# #     • Enunciado:
# # Crie uma função chamada saudacao() que imprime uma mensagem de boas-vindas. Depois, chame essa função duas vezes no programa.

def saudacao():
    print("Salve meu parça")

saudacao()
saudacao()


# # Exercício 2 – Calculadora com Funções
# #     • Enunciado:
# # Crie quatro funções: somar(a, b), subtrair(a, b), multiplicar(a, b) e dividir(a, b). Cada uma deve receber dois números e retornar o resultado da operação.

def somar(a,b):
    return a + b
def subtrair(a, b):
    return a - b
def dividir(a, b):
    return a / b
def multiplicar(a, b):
    return a * b

num1 = int(input("Numero 1 : "))
num2 = int(input("Numero 2 : "))

soma = somar(num1, num2)
sub = subtrair(num1, num2)
div = dividir(num1, num2)
mult = multiplicar(num1, num2)

print(f"Soma : {soma}")
print(f"Subtração : {sub}")
print(f"Divisão : {div}")
print(f"Multiplicação : {mult}")

# # Exercício 3 – Verificador de Maioridade
# #     • Enunciado:
# # Crie uma função chamada eh_maior_de_idade(idade) que retorne True se idade >= 18 e False caso contrário. Peça a idade do usuário, chame a função e imprima 'Acesso permitido' ou 'Acesso negado'.

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



# # Exercício 4 – Calculadora de Área com Função
# #     • Enunciado:
# # Crie uma função chamada calcular_area(largura, altura) que retorne a área de um retângulo. Use a função para calcular a área de dois cômodos e imprima os resultados.

def calcular_area(largura, altura):
    area = largura * altura
    return area

alt1 = float(input("Digite a altura do comodo 1 : ")) 
larg1 = float(input("Digite a largura do comodo 1 : ")) 
alt2 = float(input("Digite a altura do comodo 2 : ")) 
larg2 = float(input("Digite a largura do comodo 2 : ")) 

comodo1 = calcular_area(larg1, alt1)
comodo2 = calcular_area(larg2, alt2)

print(f"A area do comodo 1 é {comodo1} m²")
print(f"A area do comodo 2 é {comodo2} m²")




# Exercício 5 – View Simples em Django
#     • Enunciado:
# Crie uma função view chamada pagina_inicial(request) que retorna um HTML com o título 'Página Inicial'. Utilize a função render e um dicionário chamado context.

from django.shortcuts import render

def pagina_inicial(request): 
    context = {"titulo": "Página Inicial"}
    return render(request,'index.html',context)



