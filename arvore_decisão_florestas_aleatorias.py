from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Carregar o dataset Iris
iris = load_iris()
X = iris.data
y = iris.target

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Árvore de Decisão
arvore = DecisionTreeClassifier()
arvore.fit(X_train, y_train)
y_pred_arvore = arvore.predict(X_test)
acc_arvore = accuracy_score(y_test, y_pred_arvore)
print(f"Acurácia da Árvore de Decisão: {acc_arvore:.2f}")

# Floresta Aleatória
floresta = RandomForestClassifier(n_estimators=100)
floresta.fit(X_train, y_train)
y_pred_floresta = floresta.predict(X_test)
acc_floresta = accuracy_score(y_test, y_pred_floresta)
print(f"Acurácia da Floresta Aleatória: {acc_floresta:.2f}")