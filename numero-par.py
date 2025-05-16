numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# Algoritmo de busca linear
lista = [3, 7, 1, 9, 4]
alvo = int(input("Digite o número a buscar na lista: "))
encontrado = False
for i in range(len(lista)):
    if lista[i] == alvo:
        print(f"Número {alvo} encontrado na posição {i}.")
        encontrado = True
        break
if not encontrado:
    print(f"Número {alvo} não encontrado na lista.")