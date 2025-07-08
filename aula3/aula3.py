lista = []

print("AULA 3")
print("Listas")

for i in range(1, 11):
    lista.append(i)

print(lista)

if len(lista) > 0:
    print("A lista não está vazia")

if 3 in lista:
    print("O número 3 está na lista")


    lista_de_listas = []

    for i in range(3):
        sublista = []
        for j in range(3):
            sublista.append(i * 3 + j + 1)
        lista_de_listas.append(sublista)

    print("Lista de listas:")
    print(lista_de_listas)
     
maluco = [3, [3 , 4] , 4 , 4 , 5,[ 3, 9, 6], [5 ,[6, 6,[5 , 4,[3 , 4 , 5 , 6 , 7, 8] , 3]], 6]]

# Encontrar o número 7 e mostrar seu caminho
# maluco[6][1][0][4] == 7

print("O número 7 está em: maluco[6][1][1][4] =", maluco[6][1][2][2][4])
