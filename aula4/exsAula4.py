# Ex1
# Crie um dicionário chamado `aluno` com as seguintes chaves: `nome`, `idade`, `curso`. Depois, adicione a chave `matriculado` com valor `True`. Por fim, imprima o nome do aluno e se ele está matriculado.
print("\nEx 1\n")
aluno = {
    "nome": "Lucas",
    "idade": 20,
    "curso": "TI"
}
aluno["matriculado"] = True

if aluno["matriculado"] == True:
    print(f"O aluno {aluno['nome']} está matriculado")
else:
    print(f"O aluno {aluno['nome']} não está matriculado")


# Ex2
# Utilize um dicionário `livro` com as chaves `titulo`, `autor` e `ano`. Use um laço `for` com `.items()` para imprimir cada chave e valor de forma organizada.
print("\nEx 2\n")
livro = {
    "titulo": "Harry Potter",
    "autor": "J.K Rowling",
    "ano": 1992
}

for chave , valor in livro.items():
    print(f"{chave}: {valor}")



# Ex3
# Crie uma lista chamada `estoque` com 2 dicionários, representando produtos com `nome` e `preco`. Depois, percorra a lista e imprima os dados de cada produto.
print("\nEx 3\n")

estoque = [
    {
        "nome": "Nescau",
        "preco": 2.50
    },
    {
        "nome": "Toddy",
        "preco": 3.00
    }
]

for i in range(len(estoque)):
    for chave , valor in estoque[i].items():
        print(f"{chave}: {valor}")
    print("\n")
    

# Ex4
# Crie uma tupla chamada `coordenadas` com duas posições: latitude e longitude. Imprima cada valor separadamente.
print("\nEx 4\n")

coordenadas = ("latitude", "longitude")
print(f"Latitude : {coordenadas[0]}")
print(f"Longitude : {coordenadas[1]}")



# Ex5
# Crie um dicionário chamado `localizacao` com as chaves `cidade` e `coordenadas`. A chave `coordenadas` deve conter uma tupla com latitude e longitude. Imprima a cidade e sua latitude.
print("\nEx 5\n")

localizacao = {
    "cidade": "Campinas",
    "coordenadas": (23.7777 , 65.9984),

}

print(f"Cidade : {localizacao['cidade']}")
print(f"Coordenadas : {localizacao['coordenadas']}")
