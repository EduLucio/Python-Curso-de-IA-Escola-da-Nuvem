import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Dados de exemplo
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([3, 4, 2, 5, 6, 7, 8, 8, 9, 12])

# Regressão Linear
modelo_linear = LinearRegression()
modelo_linear.fit(X, y)
y_pred_linear = modelo_linear.predict(X)

# Regressão Polinomial (grau 2)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
modelo_poli = LinearRegression()
modelo_poli.fit(X_poly, y)
y_pred_poli = modelo_poli.predict(X_poly)

# Plotando os resultados
plt.scatter(X, y, color='blue', label='Dados reais')
plt.plot(X, y_pred_linear, color='red', label='Regressão Linear')
plt.plot(X, y_pred_poli, color='green', label='Regressão Polinomial (grau 2)')
plt.legend()
plt.xlabel('X')
plt.ylabel('y')
plt.title('Regressão Linear e Polinomial')
plt.show()