# Exercício 1: Escrever em um Arquivo
# Objetivo: Crie um programa que pergunte o nome do usuário e o salve em um arquivo de texto chamado usuario.txt.
# Dica: Use o modo de escrita ('w'). Envolva a operação de escrita em um bloco try...except para capturar possíveis erros de I/O (Entrada/Saída).


while True:
    try:
        nome = input("Digite o Nome: ")
        with open("usuario.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write(f"{nome}")
        break

    except Exception as e:
        print(f"Erro : {e}")






# Exercício 2: Ler de um Arquivo
# Objetivo: Escreva um programa que leia o nome salvo no arquivo usuario.txt (do exercício anterior) e exiba uma mensagem de boas-vindas. O programa deve lidar com o caso em que o arquivo não existe.
# Dica: Use um bloco try...except para capturar a exceção FileNotFoundError.


while True:
    try:
        with open("usuario.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                print(f"Boas Vindas : {linha.strip()}")
        break

    except Exception as e:
        print(f"Erro : {e}")











# Exercício 3: Adicionar a um Arquivo (Append)
# Objetivo: Crie um "log de eventos". O programa deve pedir ao usuário para descrever um evento e, em seguida, adicionar (anexar) esse evento com a data e hora atuais ao final de um arquivo chamado log.txt.
# Dica: Use o modo de anexação ('a') e o módulo datetime para obter a data/hora atual.

from datetime import datetime

erro = True
while erro == True :
    try:
        mensagem = input("Digite a mensagem para o log : ")
        erro = False
        with open("log2.txt", "a", encoding="utf-8") as arquivasso:
            formatted_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            arquivasso.write(f"\n{formatted_data}: {mensagem}")
        
    except Exception as e:
        print(f"Erro: {e}")
        erro = True












# Exercício 4: Lendo e Processando Dados Numéricos
# Objetivo: Suponha que você tenha um arquivo dados.txt com vários números, um por linha. No entanto, uma das linhas contém texto em vez de um número. 
# Escreva um programa que leia cada linha, some todos os números válidos e ignore as linhas que não podem ser convertidas para número, imprimindo o total no final.
# Arquivo dados.txt para este exercício:
# 10
# 25.5
# quinze
# 7
# 3.5
# Dica: Dentro do laço que lê as linhas, use um try...except para a conversão para float(). Se a conversão falhar (ValueError), simplesmente continue para a próxima linha.

total = 0


with open("aula11/dados.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo: 
        try:  
            num = float(linha) 
            total += num

        except Exception as e:
            print(f"Erro : {e} {linha}")    

print(f"{total}")

   
















# Exercício 5: Salvando Dados Estruturados
# Objetivo: Crie um programa que pergunte ao usuário o nome de um produto, a quantidade e o preço unitário. 
# O programa deve validar se a quantidade e o preço são números válidos. Se forem, salve os dados em uma nova linha no arquivo produtos.csv, no formato nome,quantidade,preço.
# 
#  Dica: Use um try...except ValueError para validar as entradas do usuário antes mesmo de tentar abrir o arquivo.

while True :
    try:
        produto = input("Qual o nome do produto: ")
        break
        
    except Exception as e:
        print(f"Erro: {e}")


while True :
    try:
        quantidade = int(input("Qual a quantidade do produto : "))
        break
        
    except Exception as e:
        print(f"Erro: {e}")

while True :
    try:
        preço = float(input("Qual preço do produto: "))
        break
        
    except Exception as e:
        print(f"Erro: {e}")
       
with open("aula11/produtos.csv", "a", encoding="utf-8") as arquivos:

    arquivos.write(f"{produto},{quantidade},{preço}\n")

