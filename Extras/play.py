valores = list(map(int,input("Digite os valores separados por um espaço : ").split()))
target = int(input("Digite o valor alvo : "))

valor1 = 0
valor2 = 0

index1 = 0
index2 = 0

for i in range(len(valores)):
    for j in range(i+1, len(valores)):
        if valores[i] + valores[j] == target:
            valor1 = valores[i]
            valor2 = valores[j]
            index1 = i
            index2 = j

if valor1 == 0 and valor2 == 0:
    print("Nenhum valor corresponde ao alvo")
else:
    print(f"Os valores seriam : [valor1, valor2]")
    print(f"Os index seriam : [index1, index2]")