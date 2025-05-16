import numpy as np

# Dados de exemplo: porta lógica AND
entradas = np.array([[0,0], [0,1], [1,0], [1,1]])
saidas = np.array([[0], [0], [0], [1]])

# Inicialização dos pesos e bias
np.random.seed(42)
pesos = np.random.rand(2, 1)
bias = np.random.rand(1)

# Função de ativação sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada da sigmoide
def sigmoid_derivada(x):
    return x * (1 - x)

# Treinamento
taxa_aprendizado = 0.1
epocas = 10000

for epoca in range(epocas):
    # Forward
    entrada_liquida = np.dot(entradas, pesos) + bias
    saida = sigmoid(entrada_liquida)
    
    # Cálculo do erro
    erro = saidas - saida
    
    # Ajuste dos pesos e bias
    ajuste = erro * sigmoid_derivada(saida)
    pesos += np.dot(entradas.T, ajuste) * taxa_aprendizado
    bias += np.sum(ajuste) * taxa_aprendizado

# Teste
entrada_liquida = np.dot(entradas, pesos) + bias
saida = sigmoid(entrada_liquida)
print("Saídas previstas:")
print(np.round(saida))
