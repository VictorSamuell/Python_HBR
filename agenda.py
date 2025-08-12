#agenda de contatos
#class Contato POO - Nome , Telefone, Email
# lista_contatos = [] para guardar os objetos contato em memoria
#menu com while
#try except pra erros
# json.load(arquivo) e json.dump(dados_para_salvar, arquivo, indent=4 , ensure_ascii=False)
#if __name__ == "__main__": menu_principal()

import json
import os


class Contato:    
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f'Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}'


def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')


def adicionar_contato(contato):
    
    contatos_json = []

    try:
        listar_contato = []
        with open("agenda.json", "r", encoding="utf-8") as arquivo:
            contatos_json = json.load(arquivo)
            print(f"{contatos_json}")
            for cont in contatos_json:
                con = Contato(cont["nome"], cont["telefone"], cont["email"])
                listar_contato.append(con)
    except (FileNotFoundError, json.JSONDecodeError):
        pass


    with open("agenda.json", "w", encoding="utf-8") as arquivo:
        if listar_contato:
            contatos_json = [c.__dict__ for c in listar_contato]
        contatos_json.append(contato.__dict__)
        print(f"Teste de Dict {contato.__dict__}")
        json.dump(contatos_json, arquivo, indent=2, ensure_ascii=False)


def buscar_contato():
    print("========================")
    print("===  Buscar Contato  ===")
    print("========================")
    print(" Você deseja buscar por :")
    print(" 1 - Nome ")
    print(" 2 - Telefone ")
    print(" 3 - Email ")
    d = input("Escolha uma opção :")
            
    if d == "1":
        nome = input("Digite o nome do contato a ser buscado : ")
        buscar_contato_nome(nome)
    elif d == "2":
        telefone = input("Digite o telefone do contato a ser buscado : ")
        buscar_contato_telefone(telefone)
    elif d == "3":
        email = input("Digite o email do contato a ser buscado : ")
        buscar_contato_email(email)

def deletar_contato():
    print("========================")
    print("===  Deletar Contato ===")
    print("========================")
    print(" Você deseja deletar por :")
    print(" 1 - Nome ")
    print(" 2 - Telefone ")
    print(" 3 - Email ")
    d = input("Escolha uma opção :")
            
    if d == "1":
        nome = input("Digite o nome do contato a ser deletado : ")
        deletar_contato_nome(nome)
    elif d == "2":
        telefone = input("Digite o telefone do contato a ser deletado : ")
        deletar_contato_telefone(telefone)
    elif d == "3":
        email = input("Digite o email do contato a ser deletado : ")
        deletar_contato_email(email)


def deletar_contato_nome(nome):
    contatos_json = []

    try:
        listar_contato = []
        with open("agenda.json", "r", encoding="utf-8") as arquivo:
            contatos_json = json.load(arquivo)
            print(f"{contatos_json}")
            for cont in contatos_json:
                con = Contato(cont["nome"], cont["telefone"], cont["email"])
                listar_contato.append(con)
    except (FileNotFoundError, json.JSONDecodeError):
        pass


    with open("agenda.json", "w", encoding="utf-8") as arquivo:
        if listar_contato:
            contatos_json = [c.__dict__ for c in listar_contato]
        print(f"len contatos json = {len(contatos_json)}")
        contatos_json = [cont for cont in contatos_json if cont["nome"] != nome]

        json.dump(contatos_json, arquivo, indent=2, ensure_ascii=False)
    



def deletar_contato_telefone(telefone):
    contatos_json = []

    try:
        listar_contato = []
        with open("agenda.json", "r", encoding="utf-8") as arquivo:
            contatos_json = json.load(arquivo)
            print(f"{contatos_json}")
            for cont in contatos_json:
                con = Contato(cont["nome"], cont["telefone"], cont["email"])
                listar_contato.append(con)
    except (FileNotFoundError, json.JSONDecodeError):
        pass


    with open("agenda.json", "w", encoding="utf-8") as arquivo:
        if listar_contato:
            contatos_json = [c.__dict__ for c in listar_contato]
        print(f"len contatos json = {len(contatos_json)}")
        contatos_json = [cont for cont in contatos_json if cont["telefone"] != telefone]

        json.dump(contatos_json, arquivo, indent=2, ensure_ascii=False)

def deletar_contato_email(email):

    contatos_json = []

    try:
        listar_contato = []
        with open("agenda.json", "r", encoding="utf-8") as arquivo:
            contatos_json = json.load(arquivo)
            print(f"{contatos_json}")
            for cont in contatos_json:
                con = Contato(cont["nome"], cont["telefone"], cont["email"])
                listar_contato.append(con)
    except (FileNotFoundError, json.JSONDecodeError):
        pass


    with open("agenda.json", "w", encoding="utf-8") as arquivo:
        if listar_contato:
            contatos_json = [c.__dict__ for c in listar_contato]
        print(f"len contatos json = {len(contatos_json)}")
        contatos_json = [cont for cont in contatos_json if cont["email"] != email]

        json.dump(contatos_json, arquivo, indent=2, ensure_ascii=False)
    

def listar_contato():
    
    contatos_json = []
    while True:
        try:
            listar_contato = []
            with open("agenda.json", "r", encoding="utf-8") as arquivo:
                contatos_json = json.load(arquivo)
                for cont in contatos_json:
                    con = Contato(cont["nome"], cont["telefone"], cont["email"])
                    listar_contato.append(con)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        if listar_contato:
            contatos_json = [c.__dict__ for c in listar_contato]
        print(f"len contatos json = {len(contatos_json)}")
        for contato in contatos_json:
            print(f"\nNome: {contato['nome']} \nTelefone: {contato['telefone']} \nEmail: {contato['email']}")

        sair = input("Digite N para sair : ")
        if sair == "N" or sair =="n":
            break

    

    


def buscar_contato_nome(nome):
    
    contatos_json = []

    try:
        listar_contato = []
        with open("agenda.json", "r", encoding="utf-8") as arquivo:
            contatos_json = json.load(arquivo)
            print(f"{contatos_json}")
            for cont in contatos_json:
                con = Contato(cont["nome"], cont["telefone"], cont["email"])
                listar_contato.append(con)
    except (FileNotFoundError, json.JSONDecodeError):
        pass


   
    if listar_contato:
        contatos_json = [c.__dict__ for c in listar_contato]
    print(f"len contatos json = {len(contatos_json)}")
    for contato in contatos_json:
        if contato['nome'] == nome:
            print(f"\nNome: {contato['nome']} \nTelefone: {contato['telefone']} \nEmail: {contato['email']}")

      


def buscar_contato_telefone(telefone):
    
    contatos_json = []

    try:
        listar_contato = []
        with open("agenda.json", "r", encoding="utf-8") as arquivo:
            contatos_json = json.load(arquivo)
            for cont in contatos_json:
                con = Contato(cont["nome"], cont["telefone"], cont["email"])
                listar_contato.append(con)
    except (FileNotFoundError, json.JSONDecodeError):
        pass

        if listar_contato:
            contatos_json = [c.__dict__ for c in listar_contato]
        print(f"len contatos json = {len(contatos_json)}")
        for contato in contatos_json:
            if contato['telefone'] == telefone:
                print(f"\nNome: {contato['nome']} \nTelefone: {contato['telefone']} \nEmail: {contato['email']}")

        


def buscar_contato_email(email):
    
    contatos_json = []

    try:
        listar_contato = []
        with open("agenda.json", "r", encoding="utf-8") as arquivo:
            contatos_json = json.load(arquivo)
            print(f"{contatos_json}")
            for cont in contatos_json:
                con = Contato(cont["nome"], cont["telefone"], cont["email"])
                listar_contato.append(con)
    except (FileNotFoundError, json.JSONDecodeError):
        pass
 
    if listar_contato:
        contatos_json = [c.__dict__ for c in listar_contato]
    print(f"len contatos json = {len(contatos_json)}")
    for contato in contatos_json:
        if contato['email'] == email:
            print(f"\nNome: {contato['nome']} \nTelefone: {contato['telefone']} \nEmail: {contato['email']}")

        





def menu_principal():
    while True:
        limpar_terminal()
        print("============================")
        print("== 1 - Adicionar Contato  ==")
        print("== 2 - Deletar Contato    ==")
        print("== 3 - Listar Contatos    ==")
        print("== 4 - Buscar Contato     ==")
        print("== 5 - Sair               ==")
        print("============================")
        op = int(input("Digite uma opção :"))

        if op == 1:
            limpar_terminal()
            print("========================")
            print("=== Dados do Contato ===")
            print("========================")

            nome = input("Digite o nome : ")
            telefone = input("Digite o Telefone : ")
            email = input("Digite o email : ")
            

            contato = Contato(nome, telefone, email)
            print(f"\nNome :{contato.nome}\nTelefone : {contato.telefone}\nEmail : {contato.email}")
            print(f"{contato}")

            adicionar_contato(contato)

        if op == 2:
            limpar_terminal()
            deletar_contato()
            
            
        if op == 3:
            limpar_terminal()
            print("========================")
            print("=== Listar Contatos ====")
            print("========================")
            listar_contato()
            

        if op == 4:
            limpar_terminal()
            buscar_contato()
            
            
        if op == 5:
            limpar_terminal()
            break


  

if __name__ == "__main__": menu_principal()
    
