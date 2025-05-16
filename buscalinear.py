lista = [10, 5, 8, 3, 7]
alvo = int(input("Digite o número a buscar na lista: "))
encontrado = False
for i in range(len(lista)):
    if lista[i] == alvo:
        print(f"Número {alvo} encontrado na posição {i}.")
        encontrado = True
        break
if not encontrado:
    print(f"Número {alvo} não encontrado na lista.")
