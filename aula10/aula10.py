# class Produto:
#     def __init__(self, nome, preco, estoque):
#         self.nome = nome
#         self.preco = preco
#         self.estoque = estoque
#         print(f"-> Objeto '{self.nome}' criado.")
    
#     def __vender__(self, quantidade):
#         if quantidade <= self.estoque:
#             # print(f"Estoque Anterior : {self.estoque}")
#             self.estoque = self.estoque - quantidade
#             # print(f"Estoque Atual : {self.estoque}")
#         else:
#             print("Estoque Insuficiente")

#     def __exibir__(self):
#         print(f"Produto: {self.nome}")
#         print(f"Produto: {self.preco}")
#         print(f"Produto: {self.estoque}")
        
# notebook = Produto(nome="Notebook Pro", preco=5500.00, estoque=15)
# cadeira = Produto(nome="Cadeira Gamer", preco=1200.50, estoque=30)

# print("\n--- Produtos Disponíveis ---")
# print(f"Produto: {notebook.nome} | Preço: R${notebook.preco:.2f}")
# print(f"Produto: {cadeira.nome} | Preço: R${cadeira.preco:.2f}")

# notebook.__vender__(5)
# cadeira.__vender__(5)

# print(f"Notebook Estoque : {notebook.estoque}")
# print(f"Notebook Estoque : {cadeira.estoque}")

# notebook.__exibir__()
# cadeira.__exibir__()


# # # # # # # # # #

class Funcionario:
    def __init__(self, nome , salario):
        self.nome = nome
        self.salario = salario

    def exibir_dados(self):
        print(f"Nome : {self.nome} & Salario : {self.salario}")
    
class Gerente(Funcionario):
    def __init__(self, nome , salario , setor):
        super().__init__(nome, salario)
        self.setor = setor

    

eu = Funcionario("Eu" , 1000)
gerente = Gerente("Gerente", 1500, "Alimentício")

eu.exibir_dados()
gerente.exibir_dados()