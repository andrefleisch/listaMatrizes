import random
nLinha = int(input("Digite o número de linhas: "))
nColuna = int(input("Digite o número de colunas: "))
def criarMatriz(nLinha, nColuna):
    matriz = []
    for i in range(nLinha):
        linha = []
        for j in range(nColuna):
            linha.append(random.randint(1,20))
        matriz.append(linha)
    return matriz

def imprimirMatriz(matriz):
    for i in range(0, nLinha):
        print(matriz[i])

def somaPar(matriz):
    par = []
    for i in range(0,nLinha):
        for j in range(0, nColuna):
            if matriz [i][j] % 2 == 0:
                par.append(matriz[i][j])
    return sum(par)


armazenarMatriz = criarMatriz(nLinha, nColuna)
imprimirMatriz(armazenarMatriz)
print(somaPar(armazenarMatriz))




