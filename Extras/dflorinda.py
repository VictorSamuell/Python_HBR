n = int(input())
figurinhas = list(map(int,input().split()))
repetidos = 0
album = []
repetidos_lista = []
especiais = 0
ref = 0
repetidos_especiais = 0
bool = True

for i in range(len(figurinhas)):
    if figurinhas[i] > n:
        print("ERRO")
        bool = False
        break

while bool == True:
    for i in range(len(figurinhas)):
        figurinhas.sort()
        if figurinhas[i] not in album:
            album.append(figurinhas[i])
        else:
            repetidos += 1
            repetidos_lista.append(figurinhas[i])

            album.sort()

    for i in range(len(album)):
        ref = str(album[i])
        if int(ref[-1]) == 3:
            especiais += 1

    for i in range(len(repetidos_lista)):
        res = str(repetidos_lista[i])
        if int (res[-1]) == 3:
            repetidos_especiais += 1

    print(len(album))
    print(especiais)
    print(repetidos)
    print(repetidos_especiais)  
    break




