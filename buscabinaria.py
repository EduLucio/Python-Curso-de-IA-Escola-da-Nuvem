lista = [1, 3, 5, 7, 9, 11, 13]
alvo = int(input("Digite o número a buscar na lista: "))
inicio = 0
fim = len(lista) - 1
encontrado = False

while inicio <= fim:
    meio = (inicio + fim) // 2
    if lista[meio] == alvo:
        print(f"Número {alvo} encontrado na posição {meio}.")
        encontrado = True
        break
    elif lista[meio] < alvo:
        inicio = meio + 1
    else:
        fim = meio - 1

if not encontrado:
    print(f"Número {alvo} não encontrado na lista.")
