# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/">
  <img src="../../assets/logo-fiap.png" 
       alt="FIAP - Faculdade de Informática e Administração Paulista" 
       width="40%">
</a>
</p>

<br>

# 🚀 FASE 4 — Inteligência Artificial, Dashboards e Otimização IoT
## 📚 Graduação ON em Inteligência Artificial

---

## 👩🏻‍💻 Sobre esta Fase

Esta fase representa uma etapa de maturação técnica e sofisticação da infraestrutura do projeto FarmTech Solutions na Graduação ON em Inteligência Artificial da FIAP.

Aqui estão organizados:

- 📖 Conteúdos teóricos estudados em otimização de memória em C/C++, modelos preditivos de Machine Learning, interfaces interativas e análise temporal de sinais
- 🧠 Conceitos consolidados de Machine Learning supervisionado (Scikit-Learn), exibição em hardware (LCD I2C), monitoramento via Serial Plotter e boas práticas de gestão de RAM no ESP32
- 🛠 Tecnologias aplicadas em sistemas embarcados (ESP32/Wokwi), Machine Learning (Scikit-Learn), visualização de dados (Streamlit) e persistência relacional
- 📂 Projetos desenvolvidos focando na evolução do sistema inteligente de irrigação com previsões automáticas e interface interativa
- 📊 Resultados e relatórios gráficos obtidos pelo monitoramento contínuo dos dados de telemetria e predição de acionamentos
- 🎯 Competências técnicas e práticas adquiridas na convergência entre hardware eficiente, análise preditiva de dados e usabilidade

Esta documentação tem como objetivo demonstrar, de forma estruturada, o que foi aprendido e aplicado durante esta etapa do curso.

---

## 👥 Integrantes do Grupo

- <a href="https://www.linkedin.com/in/juliano-romeiro-rodrigues/">Juliano Romeiro Rodrigues</a>
- <a href="https://www.linkedin.com/in/nicolas--araujo/">Nicolas Antonio Silva Araujo</a> 
- <a href="https://www.linkedin.com/in/vitoria-bagatin-31ba88266/">Vitória Pereira Bagatin</a> 

---

## 🎯 Objetivo da Fase

O foco principal desta fase foi elevar o projeto FarmTech Solutions a um nível industrial de inteligência e eficiência, otimizando o uso de recursos de hardware no ESP32 e integrando Machine Learning e Dashboards em tempo real.

- Otimizar o código em C/C++ do ESP32 para redução do consumo de memória RAM e melhoria de desempenho
- Adicionar e configurar um display LCD 20x4 (via barramento I2C) no Wokwi para exibição direta das métricas do solo
- Implementar e demonstrar o monitoramento visual de sinais temporais via Serial Plotter
- Construir um modelo preditivo com Scikit-Learn para prever a necessidade futura de irrigação com base no histórico
- Aprimorar a interface visual do sistema utilizando o framework Streamlit para exibição interativa das leituras e insights do modelo de IA

---

## 📖 Conteúdos Abordados

- **Otimização de Sistemas Embarcados:** Uso de tipos primitivos de menor tamanho (`uint8_t`, `int16_t`), structs organizadas e alocação de constantes na memória flash via macro `F()`.
- **Machine Learning Preditivo (Scikit-Learn):** Treinamento de modelos de classificação e regressão baseados no histórico de umidade, pH e nutrientes para recomendação de rega.
- **Visualização de Dados Interativa (Streamlit):** Criação de dashboards em tempo real com gráficos dinâmicos de telemetria e predições do modelo.
- **Comunicação I2C e Sinais no Wokwi:** Integração de hardware LCD 20x4 I2C e plotagem gráfica de variáveis do sistema no Serial Plotter.

---

## 🛠 Tecnologias Utilizadas

Durante esta fase, foram utilizadas as seguintes tecnologias:

- **ESP32 & C/C++ Otimizado:** Firmware eficiente para leitura e decisão local
- **LiquidCrystal_I2C & Wire:** Bibliotecas para controle do display LCD via I2C (SDA/SCL)
- **Scikit-Learn:** Modelagem preditiva de irrigação em Python
- **Streamlit:** Construção da interface interativa e dashboard em tempo real
- **SQLite / Oracle DB:** Armazenamento e consulta dos dados históricos
- **Serial Plotter (Wokwi):** Análise gráfica contínua dos dados transmitidos pela porta serial
- **Arduino IDE / VS Code:** Ambientes de desenvolvimento e compilação

---

## 📂 Projetos Desenvolvidos

### 📌 Projeto 1 — Firmware Otimizado ESP32 com Display LCD I2C e Serial Plotter

**Descrição:**  
Revisão e reestruturação do firmware em C/C++ no ESP32. Foi adicionado um display LCD 20x4 no barramento I2C (GPIO21/GPIO22) para exibir estado do solo, leituras e status da bomba em tempo real, acompanhado da padronização dos dados para o Serial Plotter.

Análise gráfica e monitoramento contínuo das variáveis do sistema (Umidade, pH, NPK e Status da Bomba) durante o ciclo de operação no Wokwi.

**Principais Otimizações de Memória Aplicadas:**
- **Tipos Específicos:** Substituição de `int` por `uint8_t` nos pinos e `int16_t` nas leituras analógicas.
- **Macro `F()`:** Armazenamento de textos constantes do LCD na memória Flash (PROGMEM), liberando RAM.
- **Agrupamento com `Struct`:** Definição da `struct SensorData` para evitar fragmentação de memória.
- **Redução de Consumo:** Economia de ~35% no uso da memória RAM comparado à versão anterior.

  
**Comportamento Observado no Serial Plotter:**
1. **Inicialização:** Sistema inicia com solo seco e variáveis zeradas.
2. **Ativação:** Ao detectar umidade baixa e presença dos nutrientes (P e K), a bomba é acionada.
3. **Estabilização:** A elevação dos níveis de umidade estabiliza o sistema e desliga automaticamente a irrigação assim que atinge a faixa ideal.

**Tecnologias utilizadas:**  
- C/C++
- Wokwi Simulator
- LiquidCrystal_I2C / Wire

---

### 📌 Projeto 2 — Modelo Preditivo com Scikit-Learn e Dashboard Streamlit

**Descrição:**  
Desenvolvimento de uma pipeline em Python utilizando Scikit-Learn para prever ações de irrigação automatizada com base em padrões de umidade, nível de nutrientes e pH. Os dados e predições são apresentados em um dashboard visual desenvolvido em Streamlit.

**Tecnologias utilizadas:**  
- Python 3
- Scikit-Learn
- Streamlit
- Pandas / NumPy

**Principais aprendizados:**  
- Treinamento e validação de algoritmos de Machine Learning com dados do solo.
- Criação de interfaces gráficas para tomada de decisão no agronegócio.
- Integração dos resultados do modelo preditivo com a interface do usuário.

---

## 🎥 Demonstração e Links do Projeto

- 📺 **Vídeo de Demonstração no YouTube:** [Assista ao funcionamento do circuito](https://youtu.be/cWbJXAkzFV0)
- ⚡ **Simulação Interativa no Wokwi:** [Acesse o projeto no Wokwi](https://wokwi.com/projects/434222558839003137)

---

## 🧠 Competências Desenvolvidas

Ao final desta fase, consolidei:

- ✔️ Otimização avançada de código em C/C++ e gestão eficiente de memória em microcontroladores
- ✔️ Integração e manipulação de displays LCD via barramento de comunicação I2C
- ✔️ Análise visual de sinais e telemetria em tempo real via Serial Plotter
- ✔️ Aplicação de Machine Learning (Scikit-Learn) para inteligência preditiva no campo
- ✔️ Construção de dashboards modernos e interativos com Streamlit
- ✔️ Integração completa de sistemas embarcados, banco de dados e inteligência artificial

---

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/SabrinaOtoni/TEMPLATE-FIAP-GRAD-ON-IA">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">FIAP</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
