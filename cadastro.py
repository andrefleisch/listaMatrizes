lista = []
matriz = []
somaIdade = []
somaRendaMensal = []
contador = 0

def cadastro():
    nome = input("Digite seu nome: ")
    lista.append(nome)
    cpf = input("Digite seu CPF: ")
    lista.append(cpf)
    idade = int(input("Digite sua idade: "))
    lista.append(idade)
    somaIdade.append(idade)
    renda_mensal = float(input("Digite sua renda mensal: "))
    lista.append(renda_mensal)
    somaRendaMensal.append(renda_mensal)
    matriz.append(lista)

def arrumarMatriz(matriz):
    for pessoa in matriz:
        print(pessoa)

cadastro()
contador += 1

while True:
    opcao = int(input("Você quer cadastrar mais uma pessoa ou quer sair do programa?: 1 - Sim 2- Sair\n"))
    if opcao < 1 or opcao > 2:
        print("Opção inválida")
        continue
    if opcao == 1:
        cadastro()
        contador += 1
        continue
    if opcao == 2:
        arrumarMatriz(matriz)
        break

print(f"Média de idade: {sum(somaIdade)/contador}\nMédia de renda mensal: {sum(somaRendaMensal)/contador} ")

    