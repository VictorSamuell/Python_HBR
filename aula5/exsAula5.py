# Exercício 1 – Menu Interativo com while (Simulando Console Admin)
#     • Enunciado:
# Crie um menu em loop com as opções '1 - Listar usuários', '2 - Sair'. Use while para manter o menu ativo até o usuário digitar 2. Esse tipo de lógica é base para ferramentas como o Django Admin Shell.

opcao = 0
while opcao != 2:
    print("--------- MENU ----------")
    print("1 - Listar Usuários")
    print("2 - Sair")
    opcao = int(input("QUAL OPÇÃO DESEJA :"))


# Exercício 2 – Loop com break para Login
#     • Enunciado:
# Simule um sistema de login via terminal que pede usuário e senha. Permita 3 tentativas e use break para sair do loop quando o login for bem-sucedido. Esse padrão pode ser adaptado para views protegidas em Django.

tentativas = 0
usuario = "User123"
senha = "senha123"
senhaCerta = False
userCerto = False

while tentativas < 3:
    tentativas += 1
    ulogin = input("Digite o Usuario : ")
    slogin = input("Digite a senha : ")

    if ulogin == usuario:
        userCerto = True
    if slogin == senha:
        senhaCerta = True

    if ulogin != usuario:
        userCerto = False
    if slogin != senha:
        userCerto = False

    if userCerto == True and senhaCerta == True:
        print("Usuario Correto")
        break
    

if tentativas >= 3:
    print("acesso negado , + de 3 tentativas")

# Exercício 3 – Filtrar com continue (Simulando verificação de permissões)
#     • Enunciado:
# Dada uma lista de usuários com permissões (admin, user, guest), use continue para ignorar os que não são 'admin'. Esse filtro é semelhante ao que faríamos em uma view com @user_passes_test.

# Exercício 4 – Coletar Dados com while (Simulando Cadastro em Formulário)
#     • Enunciado:
# Crie um loop while que permita o cadastro de nomes de produtos até o usuário digitar 'sair'. Use uma lista para armazenar os produtos. Esse tipo de coleta pode simular múltiplos envios via um formulário em Django.

# Exercício 5 – Validação com while e continue (Simulando Validador de Formulário)
#     • Enunciado:
# Solicite que o usuário digite uma senha com no mínimo 6 caracteres. Use while e continue para repetir até que uma senha válida seja digitada. Essa lógica se aproxima das validações feitas com forms.py no Django.
# #

