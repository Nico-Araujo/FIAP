import streamlit as st
import pandas as pd
import json
import joblib
import sqlite3
import plotly.express as px
from preprocess import classificar_alerta

# Carregar modelo treinado e label encoder
model = joblib.load("models/alerta_model.pkl")
le = joblib.load("models/label_encoder.pkl")

# Configuração da página
st.set_page_config(page_title="AgroGuard", layout="wide")
st.title("AgroGuard 🌱")
st.markdown("Sistema inteligente de alerta para condições críticas do solo")

# Menu lateral
menu = st.sidebar.radio("Menu", ["Análise de Sensores", "Casos de Sucesso", "Gráficos"])

# Função para buscar casos críticos
def buscar_casos_criticos():
    with open("data/casos_sucesso.json", encoding="utf-8") as f:
        casos = json.load(f)["casos"]
    return [c for c in casos if c["resultados"]["taxa_sucesso_percent"] >= 80]

# Função para carregar desastres por estado
def carregar_desastres_por_estado():
    with open("data/desastres_brasil.json", encoding="utf-8") as f:
        desastres = json.load(f)["dados"]
    df = pd.DataFrame(desastres)
    return df

# ANÁLISE DE SENSORES
if menu == "Análise de Sensores":
    st.subheader("🔬 Análise de Entrada dos Sensores")

    json_input = st.text_area("Cole os dados JSON simulados do sensor:", '''{
  "umidade": 45,
  "temperatura": 30,
  "ph": 6.5,
  "condutividade": 1.5
}''')

    if st.button("Analisar"):
        try:
            sensor_data = json.loads(json_input)
            df = pd.DataFrame([sensor_data])
            prediction = model.predict(df)[0]
            nivel_alerta = le.inverse_transform([prediction])[0]
            interpretacao = classificar_alerta(sensor_data)

            st.markdown("### Resultado da Análise")
            st.write("**Classificação por ML:**", nivel_alerta.upper())
            st.write("**Classificação por regras:**", interpretacao.upper())

            if nivel_alerta == "critico":
                st.error("⚠️ ALERTA CRÍTICO DETECTADO!")
                st.markdown("### Exemplos de Casos de Sucesso em Situação Semelhante")
                casos = buscar_casos_criticos()
                for caso in casos:
                    st.markdown(f"🔎 **{caso['titulo']}** - {caso['localizacao']['municipio']}/{caso['localizacao']['estado']}")
                    st.write(f"✅ Sucesso: {caso['resultados']['taxa_sucesso_percent']}% - Duração: {caso['resultados']['tempo_recuperacao_meses']} meses")
                    st.write(f"💰 Custo Total: R$ {caso['resultados']['custo_total_reais']:,}")
                    st.markdown("---")
            elif nivel_alerta == "atencao":
                st.warning("⚠️ Nível de atenção. Monitore e considere intervenção.")
            else:
                st.success("✅ Solo em boas condições!")

        except Exception as e:
            st.error(f"Erro ao processar JSON: {e}")

# CASOS DE SUCESSO
elif menu == "Casos de Sucesso":
    st.subheader("📘 Casos Reais de Recuperação")
    with open("data/casos_sucesso.json", encoding="utf-8") as f:
        casos = json.load(f)["casos"]

    for caso in casos:
        st.markdown(f"### {caso['titulo']}")
        st.write(f"📍 Local: {caso['localizacao']['municipio']} - {caso['localizacao']['estado']}")
        st.write(f"🧪 Tipo de desastre: {caso['desastre_original']['tipo']}")
        st.write(f"💰 Custo: R$ {caso['resultados']['custo_total_reais']:,}")
        st.write(f"⏱️ Tempo de recuperação: {caso['resultados']['tempo_recuperacao_meses']} meses")
        st.write(f"✅ Sucesso: {caso['resultados']['taxa_sucesso_percent']}%")
        st.markdown("---")

# GRÁFICOS
elif menu == "Gráficos":
    st.subheader("📊 Análise de Desastres por Estado")
    df_desastres = carregar_desastres_por_estado()

    fig = px.histogram(df_desastres, x="estado", color="tipo_desastre", barmode="group",
                       title="Distribuição de Desastres Naturais por Estado")
    st.plotly_chart(fig, use_container_width=True)

    fig2 = px.pie(df_desastres, names="tipo_desastre", title="Tipos de Desastres Registrados")
    st.plotly_chart(fig2, use_container_width=True)
