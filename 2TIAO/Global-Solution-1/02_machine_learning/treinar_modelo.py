"""

Objetivo: treinar modelos para detectar anomalias de voo e
classificar cada objeto em:
  - "Objeto Convencional"
  - "UAP / Anomalia"

Usamos DOIS modelos :
  1) Isolation Forest -> detecção de anomalias NÃO supervisionada
  2) Random Forest     -> classificação supervisionada (usa o rótulo)


"""

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


CSV_PATH = "../01_dataset/anomalias_uap.csv"

# Colunas usadas como entrada (features) do modelo
FEATURES = [
    "velocidade_mach",
    "mudanca_direcao_graus",
    "aceleracao_g",
    "altitude_km",
    "assinatura_termica",
    "formato_codigo",
]


def carregar_dados():
    df = pd.read_csv(CSV_PATH)
    X = df[FEATURES]
    y = df["rotulo"]  # 0 = convencional, 1 = UAP
    return X, y


def treinar_isolation_forest(X, y):
    """
    Isolation Forest: aprende o padrão dos dados e isola os 'estranhos'.
    contamination = proporção esperada de anomalias (~15% do nosso dataset).
    """
    print("\n" + "=" * 55)
    print(" MODELO 1: ISOLATION FOREST (Detecção de Anomalia)")
    print("=" * 55)

    modelo = IsolationForest(contamination=0.15, random_state=42)
    modelo.fit(X)

    # O modelo retorna -1 (anomalia) ou 1 (normal). Convertendo para 1/0.
    pred = modelo.predict(X)
    pred = [1 if p == -1 else 0 for p in pred]  # 1 = anomalia (UAP)

    relatorio = classification_report(
        y, pred, target_names=["Convencional", "UAP / Anomalia"]
    )
    print(relatorio)
    return modelo, relatorio


def treinar_random_forest(X, y):
    """
    Random Forest: classificador supervisionado. É o nosso
    'filtro de falsos positivos' principal porque aprende com os rótulos.
    """
    print("\n" + "=" * 55)
    print(" MODELO 2: RANDOM FOREST (Classificação)")
    print("=" * 55)

    X_treino, X_teste, y_treino, y_teste = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    modelo = RandomForestClassifier(n_estimators=200, random_state=42)
    modelo.fit(X_treino, y_treino)

    pred = modelo.predict(X_teste)

    acc = accuracy_score(y_teste, pred)
    relatorio = classification_report(
        y_teste, pred, target_names=["Convencional", "UAP / Anomalia"]
    )
    matriz = confusion_matrix(y_teste, pred)

    print(f"Acurácia: {acc:.2%}\n")
    print(relatorio)
    print("Matriz de Confusão:")
    print(matriz)

    
    print("\nImportância das variáveis:")
    importancias = sorted(
        zip(FEATURES, modelo.feature_importances_),
        key=lambda x: x[1],
        reverse=True,
    )
    for nome, valor in importancias:
        print(f"  {nome:25s} -> {valor:.3f}")

    return modelo, relatorio, acc, matriz, importancias


def salvar_relatorio(rel_iso, acc_rf, rel_rf, matriz_rf, importancias):
    with open("relatorio_metricas.txt", "w", encoding="utf-8") as f:
        f.write("RELATÓRIO DE MÉTRICAS - IDENTIFICADOR DE UAPs\n")
        f.write("=" * 55 + "\n\n")

        f.write(">> ISOLATION FOREST (não supervisionado)\n")
        f.write(rel_iso + "\n\n")

        f.write(">> RANDOM FOREST (supervisionado)\n")
        f.write(f"Acurácia: {acc_rf:.2%}\n\n")
        f.write(rel_rf + "\n\n")

        f.write("Matriz de Confusão:\n")
        f.write(str(matriz_rf) + "\n\n")

        f.write("Importância das variáveis:\n")
        for nome, valor in importancias:
            f.write(f"  {nome:25s} -> {valor:.3f}\n")

    print("\nRelatório salvo em 'relatorio_metricas.txt'")


def main():
    X, y = carregar_dados()

    _, rel_iso = treinar_isolation_forest(X, y)
    modelo_rf, rel_rf, acc_rf, matriz_rf, importancias = treinar_random_forest(X, y)

    # Salva o modelo treinado para reutilizar (sem precisar treinar de novo)
    joblib.dump(modelo_rf, "modelo_uap.joblib")
    print("\nModelo Random Forest salvo em 'modelo_uap.joblib'")

    salvar_relatorio(rel_iso, acc_rf, rel_rf, matriz_rf, importancias)


if __name__ == "__main__":
    main()
