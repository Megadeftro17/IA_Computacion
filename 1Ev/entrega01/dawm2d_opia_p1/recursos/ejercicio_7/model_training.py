import joblib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, plot_tree

TARGET = "MedHouseVal"
RANDOM_STATE = 42
TEST_SIZE = 0.2
MAX_DEPTH = 5
MODEL_PATH = "modelo_california.pkl"

def check_nulls(df: pd.DataFrame):
    print("--- Valores nulos por columna ---")
    print(df.isnull().sum())
    print("---------------------------------")

def handle_nulls(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna()

def plot_decision_tree(model):
    if getattr(model, "max_depth", None) is None or model.max_depth > 5:
        profundidad = 3
    else:
        profundidad = model.max_depth

    plt.figure(figsize=(20, 10), dpi=300)
    plot_tree(model, filled=True, max_depth=profundidad, rounded=True)
    plt.savefig("../ejercicio_4/arbol_decision.png")
    plt.close()
    print("Árbol guardado como 'arbol_decision.png'.")

def compute_errors(y_true, y_pred, print_errors: bool = True) -> tuple[float, float]:
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    if print_errors:
        print(f"MAE: {mae:.4f}")
        print(f"MSE: {mse:.4f}")
    return mae, mse

def save_model(model, path: str = MODEL_PATH):
    joblib.dump(model, path)
    print(f"Modelo guardado en: {path}")

def validate_data():
    df = fetch_california_housing(as_frame=True).frame
    check_nulls(df)
    df = handle_nulls(df)

def build_model():
    df = fetch_california_housing(as_frame=True).frame
    X = df.drop(columns=[TARGET])
    y = df[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE
    )
    model = DecisionTreeRegressor(max_depth=MAX_DEPTH, random_state=RANDOM_STATE)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    compute_errors(y_test, y_pred)
    return model

def plot_data():
    model = build_model()
    plot_decision_tree(model)

def main():
    model = build_model()
    save_model(model)

if __name__ == "__main__":
    validate_data()
    plot_data()
    main()