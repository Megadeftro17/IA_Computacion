from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

housing = fetch_california_housing(as_frame=True)
X_train, X_test, y_train, y_test = train_test_split(housing.data, housing.target, test_size=0.2, random_state=42)

lin_reg = LinearRegression().fit(X_train, y_train)
tree_reg = DecisionTreeRegressor(max_depth=5, random_state=42).fit(X_train, y_train)

print(f"Precisión Regresión Lineal: {lin_reg.score(X_test, y_test):.4f}")
print(f"Precisión Árbol de Decisión: {tree_reg.score(X_test, y_test):.4f}")