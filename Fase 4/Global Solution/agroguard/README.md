
# AgroGuard - Plataforma Inteligente de Prevenção de Desastres no Solo

## Descrição
Solução desenvolvida para a Global Solutions 2025.1 - FIAP. A aplicação utiliza sensores simulados via JSON para prever a criticidade do solo e recomendar ações de mitigação com base em um modelo de Machine Learning.

## Componentes
- `app.py`: Interface principal via Streamlit
- `ml_model.py`: Treinamento e uso do modelo Random Forest
- `preprocess.py`: Leitura e classificação dos dados do sensor
- `database.py`: Interação com banco SQLite (consultas)
- `models/alerta_model.pkl`: Modelo treinado
- `data/*.json`: Simulações de sensores

## Como rodar
1. Instale dependências:
```bash
pip install -r requirements.txt
```

2. Execute o app:
```bash
streamlit run app.py
```

## Equipe
- [Nome dos integrantes aqui]

## Frase para o vídeo:
"QUERO CONCORRER"
