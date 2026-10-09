import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor, plot_tree


def plot_decision_tree(X, y, max_depth=None):
    if max_depth is None or max_depth > 5:
        print("Límite superado. Usando max_depth=3 por defecto.")
        max_depth = 3

    model = DecisionTreeRegressor(max_depth=max_depth, random_state=42)
    model.fit(X, y)

    plt.figure(figsize=(20, 10), dpi=300)
    plot_tree(model, filled=True, max_depth=max_depth, rounded=True, feature_names=list(X.columns))
    plt.savefig("arbol_decision.png")
    plt.close()