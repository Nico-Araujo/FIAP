
# Projeto: Simulação de Sensores com ESP32 (Temperatura, Vibração, Distância)

Este projeto simula a coleta de dados de sensores com ESP32 em ambiente simulado. Em vez de dados reais, usamos dados gerados e analisados em R.

## Sensores Simulados

1. **Temperatura** (°C)
   - Normal: até 60°C
   - Alerta: > 60°C
   - Crítico: ≥ 90°C → Desligamento simulado
   https://github.com/NicoAraujo/FIAP/blob/a8f30be6e90b2edd111ec9580bb5a163cb989486/Fase%204/Enterprise%20Challenge/Simula%C3%A7%C3%A3o%20Sensores/Monitoramento%20de%20Temperatura.pdf

2. **Vibração** (g)
   - Normal: até 1.0g
   - Alerta: > 1.0g
   - Crítico: ≥ 2.0g → Parada simulada

3. **Distância (HC-SR04)** (cm)
   - Normal: 10 cm a 200 cm
   - Crítico:
     - < 5 cm → Obstrução
     - > 250 cm → Peça ausente

## Conteúdo

- `dados_sensores_simulados.csv`: dados simulados de 100 leituras.
- `simulacao_sensores.R`: script para gerar gráficos e análises em R.
- `README.md`: este documento.

## Como Rodar

1. Instale o R: https://cran.r-project.org
2. Instale o pacote `ggplot2`:
   ```r
   install.packages("ggplot2")
   ```
3. Execute o script:
   ```r
   source("simulacao_sensores.R")
   ```

Você verá três gráficos:
- Temperatura x Tempo (com alertas)
- Vibração x Tempo (com alertas)
- Distância x Tempo (com zonas críticas)

---

**Autor**: Juliano Romeiro  
**Curso**: Inteligência Artificial – FIAP  
