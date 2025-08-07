# xercício 1: Criando uma hierarquia de classes
# Crie uma classe base Animal com um método falar(). Depois, crie duas subclasses: Cachorro e Gato, que sobrescrevam o método falar() para retornar "Au au!" e "Miau", respectivamente. Crie objetos de cada uma e chame o método falar().

class Animal:
    def falar(self):
        return ".........."

class Cachorro(Animal):
    def falar(self):
        return "Au Au"

class Gato(Animal):
    def falar(self):
        return "Miau"


cachorro = Cachorro()
gato = Gato()
animal = Animal()

print(animal.falar())
print(cachorro.falar()) 
print(gato.falar()) 



# Exercício 2: Usando super()
# Crie uma classe Pessoa com o método __init__ que recebe nome. Crie uma subclasse Professor que herda de Pessoa e também recebe disciplina. Use super() para chamar o construtor da classe pai.

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Professor(Pessoa):
    def __init__(self, nome, disciplina):
        super().__init__(nome)
        self.disciplina = disciplina

prof = Professor("Teste", "Geo")
print(prof.nome)        
print(prof.disciplina) 


# Exercício 3: Polimorfismo com método comum
# Crie uma função apresentar(animal) que aceita qualquer objeto com um método falar() e imprime a fala dele. Teste com as classes Cachorro e Gato do exercício 1.

def apresentar(animal):
    print(f"{animal.falar()}")

apresentar(Cachorro())  
apresentar(Gato())     

# Exercício 5: Herança múltipla simples
# Crie duas classes Falante e Andador, cada uma com um método acao(). Depois, crie uma classe Pessoa que herda das duas e sobrescreve acao() para combinar os comportamentos.


class Falante:
    def acao(self):
        return "falando"

class Andador:
    def acao(self):
        return "andando"

class Pessoa(Falante, Andador):
    def acao(self):
        return f"{Falante.acao(self)} & {Andador.acao(self)}"


pessoa = Pessoa()
print(pessoa.acao())  
