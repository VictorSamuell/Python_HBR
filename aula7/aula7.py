# aula7 
# Variáveis globais e locais
# Variáveis globais são acessíveis em todo o código, enquanto variáveis locais só são acessíveis dentro da função onde foram definidas.
nome_app = "Meu Sistema Incrivel"

def gerar_relatorio():
    #usuário é local
    usuario = "João"
    print(f"Gerando relatório para {usuario} no aplicativo {nome_app}")
    # acesso a variável global
    print(f"Aplicativo: {nome_app}")

gerar_relatorio()


def somar_tudo(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(somar_tudo(1, 2, 3, 4, 5))  
# Args passa um número variável de argumentos para a função, permitindo somar quantos números forem necessários.
# Kwargs permite passar argumentos nomeados, como dicionários, para a função.

# exemplo de uso de kwargs
def exibir_informacoes(**informacoes):
    for chave, valor in informacoes.items():
        print(f"{chave}: {valor}")

exibir_informacoes(nome="João", idade=30, cidade="São Paulo")



def gerar_cabecalho(titulo, **opcoes):
    print(f"{titulo}")
    for chave, valor in opcoes.items():
        print(f"{chave}: {valor}")


gerar_cabecalho("Relatório de Vendas",vendedor="Maria")