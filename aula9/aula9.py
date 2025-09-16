class Carro:
    def __init__ (self , ano , cor, modelo):
        self.ano = ano
        self.cor = cor
        self.modelo = modelo
    
    def falar(self , frase):
        print(f"{frase}")

    def alterarAno(self, novoAno):
        self.ano = novoAno
    def distPercorrida(self, velocidade, tempo):
        self.distancia = (velocidade * tempo)
        print(self.distancia)

C1 = Carro(2007, "Preto" ,"Prisma")
C2 = Carro(2010, "Branco" ,"Fiat Uno")
C3 = Carro(2014, "Prata" ,"HRV")


print(f"Modelo do Carro 1 : {C1.modelo}")
print(f"Modelo do Carro 2 : {C2.modelo}")
print(f"Modelo do Carro 3 : {C3.modelo}")

print(f"Cor do Carro 1 : {C1.cor}")
print(f"Cor do Carro 2 : {C2.cor}")
print(f"Cor do Carro 3 : {C3.cor}")

print(f"Ano do Carro 1 : {C1.ano}")
print(f"Ano do Carro 2 : {C2.ano}")
print(f"Ano do Carro 3 : {C3.ano}")


C1.falar("Alguma coisa")
2
v = int(input("Digite a velocidade : "))
t = int(input("Digite o tempo : "))
print(f"{v}, {t}")

C1.distPercorrida(v , t)

print(f"Dist Percorrida : {C1.distancia}")