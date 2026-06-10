"""

Este script gera um arquivo .csv SIMULADO misturando:
  - Objetos conhecidos (aviões comerciais, balões, satélites Starlink)
  - Objetos anômalos (UAPs)

Variáveis mapeadas para o modelo:
  - velocidade_mach        -> velocidade em número de Mach
  - mudanca_direcao_graus  -> mudança brusca de direção (0 a 180 graus)
  - aceleracao_g           -> aceleração em "g" (força G)
  - altitude_km            -> altitude em quilômetros
  - assinatura_termica     -> calor emitido (0 = frio, 1 = muito quente)
  - formato_codigo         -> 0=alongado(avião), 1=esférico, 2=disco/tic-tac

A coluna "rotulo" é o alvo (target):
  - 0 = Objeto Convencional
  - 1 = UAP / Anomalia

"""

import numpy as np
import pandas as pd


np.random.seed(42)


def gerar_objetos_convencionais(n):
    """Gera objetos conhecidos: aviões, balões e satélites Starlink."""
    dados = []
    for _ in range(n):
        tipo = np.random.choice(["aviao", "balao", "starlink"])

        if tipo == "aviao":
            dados.append({
                "velocidade_mach": np.random.uniform(0.7, 0.92),     # subsônico
                "mudanca_direcao_graus": np.random.uniform(0, 15),   # curvas suaves
                "aceleracao_g": np.random.uniform(0.1, 1.5),
                "altitude_km": np.random.uniform(9, 12),
                "assinatura_termica": np.random.uniform(0.6, 0.9),   # motores quentes
                "formato_codigo": 0,                                 # alongado
            })
        elif tipo == "balao":
            dados.append({
                "velocidade_mach": np.random.uniform(0.0, 0.05),     # quase parado
                "mudanca_direcao_graus": np.random.uniform(0, 5),
                "aceleracao_g": np.random.uniform(0.0, 0.2),
                "altitude_km": np.random.uniform(20, 35),
                "assinatura_termica": np.random.uniform(0.0, 0.2),   # frio
                "formato_codigo": 1,                                 # esférico
            })
        else:  # starlink
            dados.append({
                "velocidade_mach": np.random.uniform(20, 23),        # órbita (mas previsível)
                "mudanca_direcao_graus": np.random.uniform(0, 2),    # trajetória reta
                "aceleracao_g": np.random.uniform(0.0, 0.3),
                "altitude_km": np.random.uniform(500, 560),
                "assinatura_termica": np.random.uniform(0.1, 0.3),
                "formato_codigo": 1,
            })

        dados[-1]["rotulo"] = 0  # convencional
    return dados


def gerar_uaps(n):
    """Gera objetos anômalos (UAPs) com características 'impossíveis'."""
    dados = []
    for _ in range(n):
        dados.append({
            "velocidade_mach": np.random.uniform(5, 25),             # hipersônico
            "mudanca_direcao_graus": np.random.uniform(90, 180),     # virada brusca de 90°+
            "aceleracao_g": np.random.uniform(100, 700),             # aceleração impossível p/ humanos
            "altitude_km": np.random.uniform(0.5, 30),               # altitude variada
            "assinatura_termica": np.random.uniform(0.0, 0.15),      # SEM rastro de calor
            "formato_codigo": 2,                                     # disco / tic-tac
            "rotulo": 1,                                             # UAP
        })
    return dados


def main():
    # 850 convencionais + 150 UAPs = base desbalanceada (realista)
    convencionais = gerar_objetos_convencionais(850)
    uaps = gerar_uaps(150)

    df = pd.DataFrame(convencionais + uaps)

    # Embaralha as linhas
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    df.to_csv("anomalias_uap.csv", index=False)

    print("Arquivo 'anomalias_uap.csv' gerado com sucesso!")
    print(f"Total de registros: {len(df)}")
    print(f"  - Convencionais (0): {(df['rotulo'] == 0).sum()}")
    print(f"  - UAPs / Anomalias (1): {(df['rotulo'] == 1).sum()}")
    print("\nPrimeiras linhas:")
    print(df.head())


if __name__ == "__main__":
    main()
