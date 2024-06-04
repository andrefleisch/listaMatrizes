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

def somaColuna(matriz):
    sColuna = []
    for i in range(0, nLinha):
        for j in range(escolhaColuna - 1, escolhaColuna):
            sColuna.append(matriz[i][j])
    return sColuna

def maiorLinha(matriz):
    mLinha = []
    maior = int(0)
    for i in range(escolhaLinha - 1, escolhaLinha):
        for j in range(0, nColuna):
            if maior < matriz[i][j]:
                maior = matriz[i][j]
    mLinha.append(maior)
    return mLinha
            
    
armazenarMatriz = criarMatriz(nLinha, nColuna)
imprimirMatriz(armazenarMatriz)
print(somaPar(armazenarMatriz))

while True:
    escolhaColuna = int(input("Escolha a coluna da matriz que quer somar: "))
    if escolhaColuna > nColuna or escolhaColuna == 0:
        print("Número inválido")
        continue
    else:
        break

print(f"A soma da coluna {escolhaColuna} é de: {sum(somaColuna(armazenarMatriz))}")

while True:
    escolhaLinha = int(input("Escolha a linha da matriz que quer achar o maior valor: "))
    if escolhaLinha > nLinha or escolhaLinha == 0:
        print("Número inválido")
        continue
    else:
        break
    
print(f"O maior número da linha {escolhaLinha} é o: {maiorLinha(armazenarMatriz)}")


