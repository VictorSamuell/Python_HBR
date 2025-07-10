carro = {"marca": "Ford", "modelo": "Fiesta", "ano": "2014", "cor": "Prata"}

carro['kilometragem'] = 100000

print("\nDetalhes do carro: \n ")

for chave , valor in carro.items():  
    print(f"{chave}: {valor}")

print(f"Modelo do carro: {carro['modelo']}")

print("\n")

carros = [
    {"marca": "Ford", "modelo": "Fiesta", "ano": "2014", "cor": "Prata"},
    {"marca": "Chevrolet", "modelo": "Onix", "ano": "2018", "cor": "Preto"},
    {"marca": "Volkswagen", "modelo": "Gol", "ano": "2020", "cor": "Branco"}
]

for i in range(len(carros)):
    print(f"Carro {i+1}:")
    for chave, valor in carros[i].items():

        print(f"'\033[1;36m{chave}\033[m': '\033[1;33m{valor}\033[m'")
    print("\n")


coordenadas_sp = (-23.5505, -46.6333)
print(f"Coordenadas de São Paulo: \033[1;32m{coordenadas_sp}\033[m")


catalogo = []

livro1 = {
    "titulo": "Dom Casmurro",
    "autor": "Machado de Assis",
    "ano": 1899
}
livro2 = {
    "titulo": "Memórias Póstumas de Brás Cubas",
    "autor": "Machado de Assis",
    "ano": 1881
}
livro3 = {
    "titulo": "O Guarani",
    "autor": "José de Alencar",
    "ano": 1857
}

catalogo.append(livro1)
catalogo.append(livro2)
catalogo.append(livro3)

print("\n\033[1;4mCatalogo de Livros:\033[m\n")
for i in range(len(catalogo)):
    print(f"\033[1;32mLivro {i+1}:\033[m \033[1;36m{catalogo[i]['titulo']}, por {catalogo[i]['autor']} ({catalogo[i]['ano']})\033[m")
print("\n")

# Exemplo: transformar uma lista em dicionário
lista_chaves = ["nome", "idade", "cidade"]
lista_valores = ["Ana", 25, "São Paulo"]

dicionario = dict(zip(lista_chaves, lista_valores))
print("Dicionário criado a partir de listas:", dicionario)


# Exemplo de dicionário dentro de dicionário
alunos = {
    "aluno1": {
        "nome": "Carlos",
        "idade": 20,
        "curso": "Engenharia"
    },
    "aluno2": {
        "nome": "Marina",
        "idade": 22,
        "curso": "Medicina"
    }
}
print(" alunos['aluno1']['nome']:", alunos['aluno1']['nome'])

print("\n\033[1;4mInformações dos Alunos:\033[m\n")
for chave, info in alunos.items():
    print(f"{chave}:")
    for campo, valor in info.items():
        print(f"  {campo}: {valor}")
    print()