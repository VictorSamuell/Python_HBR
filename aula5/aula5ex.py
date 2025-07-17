# Exercício 1 – Menu Interativo com while (Simulando Console Admin)
# •	Enunciado:
# Crie um menu em loop com as opções '1 - Listar usuários', '2 - Sair'. Use while para manter o menu ativo até o usuário digitar 2. Esse tipo de lógica é base para ferramentas como o Django Admin Shell.

while True:
    print("\nMenu:")
    print("1 - Listar usuários")
    print("2 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print("Lista de Usuarios")
    elif opcao == '2':
        print("Saindo do sistema")
        break
    else:
        print("Opção inválida. Tente novamente.")



# Exercício 2 – Loop com break para Login
# •	Enunciado:
# Simule um sistema de login via terminal que pede usuário e senha. Permita 3 tentativas e use break para sair do loop quando o login for bem-sucedido. Esse padrão pode ser adaptado para views protegidas em Django.

usuario_correto = "admin"
senha_correta = "123456"

tentativas = 0

while tentativas < 3:
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Login feito")
        break
    else:
        print("Login incorreto. Tente novamente.")
        tentativas += 1
        print(f"Tentativa Numero : {tentativas}")

if tentativas == 3:
    print("Número máximo de tentativas atingido.")


# Exercício 3 – Filtrar com continue (Simulando verificação de permissões)
# •	Enunciado:
# Dada uma lista de usuários com permissões (admin, user, guest), use continue para ignorar os que não são 'admin'. Esse filtro é semelhante ao que faríamos em uma view com @user_passes_test.

usuarios = [
    {"nome": "A", "permissao": "admin"},
    {"nome": "B", "permissao": "user"},
    {"nome": "C", "permissao": "guest"},
    {"nome": "D", "permissao": "admin"},
]

print("Usuários com permissão 'admin':")
for usuario in usuarios:
    if usuario["permissao"] != "admin":
        continue
    print(f"- {usuario['nome']}")



# Exercício 4 – Coletar Dados com while (Simulando Cadastro em Formulário)
# •	Enunciado:
# Crie um loop while que permita o cadastro de nomes de produtos até o usuário digitar 'sair'. Use uma lista para armazenar os produtos. Esse tipo de coleta pode simular múltiplos envios via um formulário em Django.

produtos = []

while True:
    nome = input("Digite o nome do produto (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    produtos.append(nome)

print("\nProdutos cadastrados:")
for produto in produtos:
    print(f"- {produto}")



# Exercício 5 – Validação com while e continue (Simulando Validador de Formulário)
# •	Enunciado:
# Solicite que o usuário digite uma senha com no mínimo 6 caracteres. Use while e continue para repetir até que uma senha válida seja digitada. Essa lógica se aproxima das validações feitas com forms.py no Django.

while True:
    senha = input("Digite uma senha (mínimo 6 caracteres): ")
    if len(senha) < 6:
        print("Senha muito curta. Tente novamente.")
        continue
    print("Senha válida!")
    break
