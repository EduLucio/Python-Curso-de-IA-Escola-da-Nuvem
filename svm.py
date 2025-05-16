import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# Dados de exemplo (duas classes)
X = np.array([[1, 2], [2, 3], [3, 3], [6, 5], [7, 8], [8, 8]])
y = np.array([0, 0, 0, 1, 1, 1])

# Criação e treinamento do modelo SVM
modelo = svm.SVC(kernel='linear')
modelo.fit(X, y)

# Plotando os pontos
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr', label='Dados')

# Plotando a linha de decisão
w = modelo.coef_[0]
b = modelo.intercept_[0]
x_plot = np.linspace(0, 10)
y_plot = -(w[0] * x_plot + b) / w[1]
plt.plot(x_plot, y_plot, 'k--', label='Fronteira de decisão')

plt.xlabel('X1')
plt.ylabel('X2')
plt.title('SVM - Máquina de Vetores de Suporte')
plt.legend()
plt.show()