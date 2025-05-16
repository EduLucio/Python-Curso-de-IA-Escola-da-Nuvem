from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Dados de exemplo: porta lógica AND
entradas = np.array([[0,0], [0,1], [1,0], [1,1]])
saidas = np.array([[0], [0], [0], [1]])

# Criação do modelo
modelo = Sequential()
modelo.add(Dense(2, input_dim=2, activation='relu'))
modelo.add(Dense(1, activation='sigmoid'))

# Compilação do modelo
modelo.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Treinamento
modelo.fit(entradas, saidas, epochs=100, verbose=0)

# Teste
resultados = modelo.predict(entradas)
print("Saídas previstas:")
print(np.round(resultados))
