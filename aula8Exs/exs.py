# Exercício 1: Explorando a Biblioteca Padrão
# Objetivo: Praticar importações simples de módulos da biblioteca padrão.

# Enunciado:
# Crie um script chamado datas.py que importe o módulo datetime e imprima:
# - A data e hora atual
# - A data de ontem
# - A diferença entre duas datas

import datetime

print("Data e hora atual:", datetime.datetime.now())
ontem = datetime.datetime.now() - datetime.timedelta(days=1)
print("Data de ontem:", ontem)
#sintaxe datetime(ano, mes, dia)
data1 = datetime.datetime(2023, 10, 1)
data2 = datetime.datetime.now()
diferenca = data2 - data1
print("", diferenca)
tomorrow = datetime.datetime.now() - datetime.datetime.timedelta(days=1)
print("Diferença entre as datas:", diferenca.days, "dias")



# Exercício 2: Instalando e Usando um Pacote com pip
# Objetivo: Usar pip para instalar pacotes e aplicá-los.

# Enunciado:
# 1. Ative seu ambiente virtual.
# 2. Instale o pacote emoji usando o comando pip.
# 3. Crie um script diversao.py que exibe uma mensagem usando emojis.


# python -m venv nome_do_ambiente (ex: python -m venv venv)
# para ativar o ambiente virtual : .\venv\Scripts\activate

print("🎉😄")






# Exercício 3: Criando e Ativando um Ambiente Virtual
# Objetivo: Criar e ativar um ambiente virtual local.

# Enunciado:
# 1. Crie uma pasta chamada projeto_teste.
# 2. Dentro dessa pasta, crie um ambiente virtual chamado venv.
# 3. Ative o ambiente virtual e use pip list para verificar os pacotes instalados.


# O venv ja esta criado na pasta do projeto, para ativar o ambiente virtual use o comando:
# .\venv\Scripts\activate













# Exercício 4: Usando requests com API Pública
# Objetivo: Instalar requests e consumir uma API.

# Enunciado:
# Crie um script github_user.py que utilize o módulo requests para exibir os dados de um usuário do GitHub.



import requests

response = requests.get('https://api.github.com/users/VictorSamuell')
print(response.json())


username = input("Digite o nome de usuário do GitHub: ")
response = requests.get(f"https://api.github.com/users/{username}")


user_data = response.json()
print(f"\n{user_data}\n")
print("\nDados do usuário do GitHub:")
print("Nome:", user_data.get("name"))
print("Localização:", user_data.get("location"))















# Exercício 5: requirements.txt na Prática
# Objetivo: Gerar e instalar dependências a partir de um arquivo requirements.txt.

# Enunciado:
# 1. Após instalar os pacotes necessários no seu ambiente virtual, gere o arquivo requirements.txt.
# 2. Simule uma nova instalação em outro ambiente com o comando adequado.

#coloquei no .gitignore para não subir o venv