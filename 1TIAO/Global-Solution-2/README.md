# 🌏 Global Solution 2°Semestre
# 🏭 Fiscal de Segurança Inteligente - Indústria 4.0
# 🦺 Sistema de Monitoramento de EPI com Visão Computacional e Privacidade

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/YOLO-v8/v5-green)](https://github.com/ultralytics/ultralytics)
[![R Shiny](https://img.shields.io/badge/R-Shiny-blueviolet)](https://shiny.rstudio.com/)
[![Cloud](https://img.shields.io/badge/Cloud-Deploy-orange)](https://aws.amazon.com/)

### 🎲[Dataset utilizado para treinar a Rede Neural](https://public.roboflow.com/object-detection/hard-hat-workers)

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/nicolas--araujo/">Nicolas Antonio Silva Araujo</a> 
- <a href="https://www.linkedin.com/in/vitoria-bagatin-31ba88266/">Vitória Pereira Bagatin</a> 
<br><br>

## 📋 Sobre o Projeto
Este projeto, desenvolvido para a **Global Solution 2025.2 - "O Futuro do Trabalho"**, implementa um **Fiscal de Segurança Inteligente** para ambientes da Indústria 4.0. 

O objetivo é utilizar Inteligência Artificial para promover um ambiente de trabalho mais seguro e humano, prevenindo acidentes através da detecção automática do uso de Equipamentos de Proteção Individual (EPIs), como capacetes e coletes. Diferente de sistemas tradicionais de vigilância, nossa solução prioriza a **ética e a privacidade**, aplicando anonimização automática nos rostos dos colaboradores e focando na prevenção de riscos, não na punição.

A solução integra Visão Computacional, Backend em Nuvem, Banco de Dados e um Dashboard analítico em R para gestão de segurança.
<br><br>

## 🎯 Integração Multidisciplinar (Global Solution)
Este projeto demonstra a aplicação prática das disciplinas do curso na construção de uma solução robusta:

- ✅ **Redes Neurais e Computer Vision**: Treinamento de modelo YOLO para identificar e classificar 'Pessoa', 'Capacete' e 'Sem Capacete' em tempo real.
- ✅ **Cybersecurity**: Implementação de "Privacy by Design" com algoritmos de desfoque (blur) facial automático antes do processamento/armazenamento das imagens, garantindo conformidade com normas de privacidade.
- ✅ **Machine Learning**: Análise preditiva dos dados de alertas para identificar horários e setores com maior risco de incidentes (proatividade).
- ✅ **Linguagem R**: Desenvolvimento de um Dashboard interativo (Shiny) para visualização de mapas de calor e estatísticas de segurança para os gestores.
- ✅ **Python e Banco de Dados**: Construção da API de backend para orquestrar o fluxo de dados e persistência dos eventos de alerta em banco de dados na nuvem.
<br><br>

## 🛠️ Tecnologias Utilizadas
* **YOLO (Ultralytics)**: Modelo de detecção de objetos de estado-da-arte.
* **OpenCV**: Biblioteca para processamento de imagem e aplicação de filtros de privacidade.
* **Python (Flask/FastAPI)**: Backend da aplicação e API de integração.
* **Linguagem R (Shiny)**: Frontend para construção do Dashboard de gestão.
* **SQL/NoSQL**: Banco de dados para armazenamento histórico dos alertas.
* **Cloud Computing**: Ambiente para deploy da API e do Banco de Dados.

<br>

## 🏗️ Arquitetura da Solução
O fluxo de dados segue o seguinte pipeline:
1. **Captura**: Câmeras enviam o feed de vídeo.
2. **Processamento (Backend)**: A IA detecta pessoas e EPIs e aplica o blur facial.
3. **Decisão**: Se uma infração (falta de EPI) é detectada, um alerta é gerado.
4. **Armazenamento**: O evento é salvo no Banco de Dados na nuvem.
5. **Visualização (Frontend)**: O Dashboard em R lê o banco e exibe os indicadores ao Supervisor.

![Diagrama da Arquitetura](https://github.com/Nico-Araujo/Global-Solution-S2/blob/82714f58589a760d081a0e18193a25f231b8dab4/docs/arquitetura_GS2.drawio.png)
<br><br>

## 🚀 Metodologia
1.  **Coleta e Rotulação**: Criação de dataset com imagens de ambientes industriais e anotação de classes (capacete, colete, pessoa) usando ferramentas como Roboflow ou Make Sense AI.
2.  **Treinamento da IA**: Fine-tuning do modelo YOLO para o contexto específico de segurança do trabalho.
3.  **Desenvolvimento do Backend**: Criação da lógica de inferência e anonimização em Python.
4.  **Análise de Dados (R)**: Construção dos scripts em R para ler o banco de dados e gerar gráficos dinâmicos.
5.  **Validação e Testes**: Simulação de cenários de risco para validar a precisão da detecção e a eficácia do desfoque de privacidade.
<br><br>

## 📊 Resultados e Métricas

### 1. Desempenho do Modelo de IA (Validação em GPU)
Métricas obtidas durante o treinamento e validação do modelo YOLOv8 no Google Colab:
* **Precisão Capacete (mAP50)**: **98.3%** (Excelente capacidade de detecção)
* **Precisão Cabeça (mAP50)**: **96.7%**
* **Velocidade de Inferência (GPU)**: **9.2 ms** por quadro (Ideal para tempo real)

### 2. Métricas Operacionais da POC (Simulação Local)
Dados extraídos da execução da Prova de Conceito em ambiente local (CPU):
* **Confiança Média em Execução**: **91.5%**
* **Eficácia do Filtro de Privacidade**: **100%** (274 rostos anonimizados)
* **Alertas Gerados**: 274 incidentes identificados e persistidos no Banco de Dados.
* **Latência Média (CPU)**: ~45ms.
 <br><br>
 
![Dashboard-R](https://github.com/Nico-Araujo/Global-Solution-S2/blob/f4b66e964799e2cd778ee2958283921739909e89/docs/dashboard-R.png)
<br><br>
![Dashboard2-R](https://github.com/Nico-Araujo/Global-Solution-S2/blob/f4b66e964799e2cd778ee2958283921739909e89/docs/dashboard2-R.png)
<br><br>

## 🔗 Links do Projeto
* [**Notebook de Treinamento (Colab)**: Rede Neural](https://colab.research.google.com/drive/1iE1DRKXj6Taf3mJ5Lb_Cfo8qaCaFKWLQ#scrollTo=848e2f87)
* [**Dashboard (R Shiny)**](https://udf24n-n0colas0ant0nio.shinyapps.io/Dashboard_GS_2025_2/)
<br><br>

## 🎥 Vídeo de Demonstração
Confira o vídeo explicativo da solução, demonstrando a detecção em tempo real, a integração entre Python e R, e as funcionalidades de privacidade:

* **[Clique aqui para assistir ao vídeo no YouTube](https://www.youtube.com/watch?v=9XlqpqEjY3s)** <br><br>

## 📋 Conclusões
O "Fiscal de Segurança Inteligente" prova que é possível utilizar a tecnologia avançada para proteger vidas sem comprometer a privacidade individual. A solução atende ao desafio "O Futuro do Trabalho" ao criar um ambiente onde a automação atua como parceira da segurança humana, permitindo uma gestão baseada em dados e ações preventivas, em vez de reativas.
