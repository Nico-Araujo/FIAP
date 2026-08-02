# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/">
  <img src="../../assets/logo-fiap.png" 
       alt="FIAP - Faculdade de Informática e Administração Paulista" 
       width="40%">
</a>
</p>

<br>

# 🚀 FASE 3 — Sistemas Embarcados & Inteligência na Rega
## 📚 Graduação ON em Inteligência Artificial

---

## 👩🏻‍💻 Sobre esta Fase

Esta fase representa uma etapa de evolução prática e integração de hardware e software na Graduação ON em Inteligência Artificial da FIAP.

Aqui estão organizados:

- 📖 Conteúdos teóricos estudados em microcontroladores (ESP32), eletrônica digital, programação C/C++ para sistemas embarcados e bancos de dados relacionais
- 🧠 Conceitos consolidados de automação com sensores, acionamento via relé e tomada de decisão automatizada com dados em tempo real
- 🛠 Tecnologias aplicadas em simulação de hardware (Wokwi), bancos SQL (SQLite), desenvolvimento de dashboards (Streamlit) e APIs meteorológicas
- 📂 Projetos desenvolvidos para prototipagem de sistema físico-virtual de irrigação agrícola e pipeline de dados integrados
- 📊 Resultados e relatórios interativos obtidos por meio de monitoramento serial e visualizações gráficas em tempo real
- 🎯 Competências técnicas e práticas adquiridas na convergência entre IoT, dados e Inteligência Artificial aplicada ao agronegócio

Esta documentação tem como objetivo demonstrar, de forma estruturada, o que foi aprendido e aplicado durante esta etapa do curso.

---

## 👥 Integrantes do Grupo

- Nícolas Antonio Silva Araujo
- Mariana Barbui dos Santos Zitelli
- Thiago Gomes
- Vitoria Pereira Bagatin
- Juliano Romeiro Rodrigues

---

## 🎯 Objetivo da Fase

O foco principal desta fase foi criar um protótipo físico-simulado completo para acionamento de irrigação agrícola inteligente e integrar as leituras a um ecossistema de dados persistentes, análise visual e tomada de decisão preditiva baseada no clima.

- Desenvolver um circuito no ESP32 (simulado via Wokwi) capaz de ler sensores de umidade, pH e presença de nutrientes (Fósforo e Potássio) e controlar uma bomba de irrigação acionada por relé
- Implementar a lógica de controle embarcada escrita em C/C++ no PlatformIO/VS Code
- Criar uma aplicação Python conectada a um banco de dados SQL (SQLite) com operações CRUD completas para persistência dos dados de telemetria do monitor serial
- Desenvolver um painel interativo (Dashboard em Streamlit) para monitoramento e análise de padrões dos sensores e status da bomba
- Integrar a lógica de acionamento do sistema com uma API meteorológica pública (OpenWeather) para tomada de decisão preventiva de irrigação

---

## 📖 Conteúdos Abordados

- **Sistemas Embarcados & IoT:** Programação de microcontroladores ESP32 em C/C++, leitura analógica/digital de sensores (DHT22, LDR, push-buttons) e acionamento de atuadores (módulo relé).
- **Persistência SQL & CRUD em Python:** Estruturação de banco relacional local em SQLite, mapeamento de tabelas de monitoramento, execução de queries (Create, Read, Update, Delete) e manipulação de fluxos de entrada/saída.
- **Visualização de Dados & Dashboarding:** Criação de aplicações web interativas com Streamlit, geração de gráficos temporais para variáveis físicas e filtragem dinâmica de logs de telemetria.
- **Integração com APIs REST:** Requisições HTTP em Python para consumo de dados climáticos em tempo real, tratamento de payload JSON e regras de decisão baseadas na previsão de chuva.

---

## 🛠 Tecnologias Utilizadas

Durante esta fase, foram utilizadas as seguintes tecnologias:

- **ESP32 Microcontroller:** Unidade central de processamento do sistema embarcado
- **C / C++ (PlatformIO / Wokwi):** Linguagem utilizada para desenvolvimento do firmware de controle do ESP32
- **Python 3:** Lógica de persistência, integração com banco SQL e requisições HTTP
- **SQLite:** Banco de dados relacional leve para armazenamento local das leituras dos sensores
- **Streamlit:** Framework para criação do painel/dashboard interativo de visualização
- **OpenWeather API:** API pública para consulta e integração de dados meteorológicos
- **VS Code & GitHub:** Ambientes de desenvolvimento e controle de versionamento colaborativo

---

## 📂 Projetos Desenvolvidos

### 📌 Projeto 1 — Sistema Embarcado de Irrigação Inteligente com ESP32 (Wokwi)

**Descrição:**  
Desenvolvimento de um circuito simulado no Wokwi utilizando um microcontrolador ESP32 integrado a múltiplos sensores (DHT22 para umidade do solo, LDR simulando variação de pH, e botões físicos para presença binária dos nutrientes Fósforo e Potássio). O sistema analisa continuamente as condições e aciona a bomba d'água (módulo relé) quando a umidade atinge níveis baixos e os nutrientes estão presentes.

**Tecnologias utilizadas:**  
- C/C++ (PlatformIO)
- Wokwi Simulator
- ESP32, DHT22, LDR, Botões, Relé

**Principais aprendizados:**  
- Leitura analógica e conversão/mapeamento de sinais (escalonamento do LDR para escala de pH 0–14).
- Leitura digital com resistores internos de pull-up (`INPUT_PULLUP`) para detecção de estado de nutrientes.
- Construção de regras lógicas de acionamento preventivo de atuadores de carga (relé).

---

### 📌 Projeto 2 — Banco de Dados Relacional e Script CRUD em Python

**Descrição:**  
Desenvolvimento de uma camada de persistência em Python que recebe ou simula os logs transmitidos pelo monitor serial do ESP32 e realiza o armazenamento estruturado em um banco de dados relacional SQLite (`leituras_sensores`). O módulo conta com funções preparadas para Create, Read, Update, Delete e exportação para arquivos CSV.

**Tecnologias utilizadas:**  
- Python 3
- SQLite3
- Biblioteca Pandas / CSV

**Principais aprendizados:**  
- Mapeamento direto entre o MER da Fase 2 e o esquema de tabelas em SQLite.
- Implementação de rotinas robustas de CRUD para manipulação de registros de telemetria.
- Estruturação de um pipeline seguro de dados coletados do monitor serial para banco SQL.

---

### 📌 Projeto 3 (Ir Além 1) — Dashboard em Python para Visualização dos Dados (Streamlit)

**Descrição:**  
Desenvolvimento de uma dashboard interativa utilizando o framework Streamlit, permitindo aos produtores e gestores agrícolas visualizarem em tempo real e de forma simples o comportamento das variáveis ambientais (umidade, pH, NPK) e o histórico de acionamentos da bomba de irrigação.

**Tecnologias utilizadas:**  
- Python 3
- Streamlit
- Matplotlib / Plotly

**Principais aprendizados:**  
- Transformação de dados brutos de tabelas SQL em painéis visuais interativos e acessíveis para leigos.
- Aplicação de filtros temporais e análise gráfica de séries históricas de irrigação.

---

### 📌 Projeto 4 (Ir Além 2) — Integração com API Pública Meteorológica (OpenWeather)

**Descrição:**  
Construção de uma camada de inteligência preditiva que realiza requisições HTTP para a API pública do OpenWeather. O sistema avalia dados climáticos em tempo real e a previsão de chuvas para as próximas horas; caso haja probabilidade de precipitação, o sistema sobrescreve o acionamento da irrigação para evitar o desperdício de água.

**Tecnologias utilizadas:**  
- Python 3 (`requests`)
- OpenWeather API REST
- JSON Parser

**Principais aprendizados:**  
- Consumo e parsing de dados JSON oriundos de web APIs em tempo real.
- Implementação de regras de decisão cruzadas (sensores locais + previsão externa).

---

## 🧠 Competências Desenvolvidas

Ao final desta fase, consolidei:

- ✔️ Prototipagem e programação de sistemas embarcados para automação agrícola com ESP32
- ✔️ Leitura, calibração e interpretação de dados de sensores analógicos e digitais
- ✔️ Estruturação de banco de dados SQL e manipulação das operações CRUD via Python
- ✔️ Desenvolvimento de dashboards visuais e intuitivos para apresentação de dados de IoT
- ✔️ Consumo de APIs REST e criação de lógicas condicionais baseadas em clima externo
- ✔️ Integração completa de hardware, banco de dados, frontend e inteligência preditiva
- ✔️ Organização, versionamento e documentação técnica detalhada no GitHub

---

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/SabrinaOtoni/TEMPLATE-FIAP-GRAD-ON-IA">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">FIAP</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
