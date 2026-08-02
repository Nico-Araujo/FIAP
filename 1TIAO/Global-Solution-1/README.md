# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/">
  <img src="../../../assets/logo-fiap.png" 
       alt="FIAP - Faculdade de Informática e Administração Paulista" 
       width="40%">
</a>
</p>

<br>

# AgroGuard - Plataforma Inteligente de Prevenção de Desastres no Solo
## Global Solution 2025.1

## 👨‍🎓 Integrantes: 

- <a href="https://www.linkedin.com/in/juliano-romeiro-rodrigues/">Juliano Romeiro Rodrigues</a>
-  Mariana Barbui dos Santos Zitelli
- <a href="https://www.linkedin.com/in/nicolas--araujo/">Nicolas Antonio Silva Araujo</a> 
- <a href="https://www.linkedin.com/in/vitoria-bagatin-31ba88266/">Vitória Pereira Bagatin</a> 

## 👩‍🏫 Professores:
### Tutor(a) 
- Lucas
### Coordenador(a)
- André Godoi Chiovato


## 📜 Descrição

O **AgroGuard** é uma plataforma inteligente e preditiva desenvolvida no contexto do ecossistema agrícola da Global Solution 2025.1 na FIAP. Diante dos crescentes desafios climáticos, instabilidade na umidade do solo e riscos de degradação e erosão em áreas agrícolas, a solução atua na monitoração ativa e prevenção de desastres ambientais no solo.

A aplicação consome dados simulados de sensores agrícolas transmitidos no formato JSON, representando parâmetros físicos essenciais como umidade, pH e níveis de nutrientes. A partir desses dados, um algoritmo de Machine Learning baseado na arquitetura **Random Forest** classifica em tempo real a criticidade do solo (normal, atenção ou crítico) e gera recomendações automatizadas de ações de mitigação preventivas (como ajustes na irrigação, dosagem de fertilizantes e mitigação de erosão).

O sistema conta com um banco de dados relacional (SQLite) para armazenamento e histórico de telemetria e alertas, e disponibiliza uma interface interativa via **Streamlit** que permite a gestores e produtores rurais acompanharem a saúde do solo, analisarem gráficos de tendência e tomarem decisões embasadas em dados preditivos.


## 📁 Estrutura de pastas

Global Solution/
├── agroguard/
│   ├── data/
│   │   ├── casos_sucesso.json
│   │   ├── clima_brasil.json
│   │   ├── desastres_brasil.json
│   │   ├── gs_database.db
│   │   ├── parametros_sensores.json
│   │   └── recuperacao_solo.json
│   ├── models/
│   ├── app.py
│   ├── preprocess.py
│   └── requirements.txt
├── banco_de_dados/
│   ├── BancoDeDados.py
│   ├── casos_sucesso.json
│   ├── clima_brasil.json
│   ├── desastres_brasil.json
│   ├── parametros_sensores.json
│   └── recuperacao_solo.json
├── Circuito-Esp.png
├── Codigo-Circuito-Esp.cpp
├── Global Solution - 1º Semestre.mp4
├── Global Solution - 2025.1.pdf
└── Teste-Circuito.mp4


## 📎 Observações

- <b>Explicação de decisões técnicas</b>: 
  - A escolha do modelo **Random Forest** fundamenta-se em sua robustez para lidar com dados tabulares de sensores físicos e sua baixa tendência a *overfitting*.
  - A persistência via **SQLite** garante leveza e viabilidade para execuções locais e simuladas sem complexidade de infraestrutura.
  - O uso do formato **JSON** para simulação dos sensores reflete a estrutura padrão utilizada em protocolos IoT de mercado.


## 🔧 Como executar o código

### Pré-requisitos
- **Python 3.8+** instalado
- **Git** instalado (para clonar o repositório)

### Instalação e Execução

1. Instale dependências:
```bash
pip install -r requirements.txt
```

2. Execute o app:
```bash
streamlit run app.py
```
