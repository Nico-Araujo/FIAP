# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">

# FarmTech Solutions - Projeto de Irrigação Automatizada com ESP32

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/juliano-romeiro-rodrigues/">Juliano Romeiro Rodrigues</a>
- <a href="https://www.linkedin.com/in/nicolas--araujo/">Nicolas Antonio Silva Araujo</a> 
- <a href="https://www.linkedin.com/in/vitoria-bagatin-31ba88266/">Vitória Pereira Bagatin</a> 


## 📜 Descrição

Este projeto implementa um sistema inteligente de irrigação utilizando o microcontrolador ESP32, que monitora condições do solo e ativa uma bomba de água automaticamente quando necessários. O sistema integra sensores para umidade, pH simulado e nutrientes (fósforo e potássio), além de um display LCD 20x4 para visualização em tempo real.


## 🔧 Como executar o código

## Pré-requisitos

### Hardware
- Placa ESP32 (ex: ESP32-WROOM-32)
  - DHT22 (sensor de umidade)
  - LDR (simulando sensor de pH)
  - 2 Slide Switch (simulando sensor para detectar a presença de Fósforo e Potássio)
  - Display LCD 20x4 barramento I2C (pinos SDA e SCL) ou Display LCD 16x2 I2C (porém necessita de um pequeno ajuste no código em C++ para arrumar as linhas e colunas)
  - Módulo Relé 5V
  - 2 Resistor 10kΩ
  - Protoboard e jumpers

### Software
- [Arduino IDE 1.8+](https://www.arduino.cc/en/software)
- Pacote ESP32

### Bibliotecas (instale via `Sketch > Incluir Biblioteca > Gerenciar Bibliotecas`)
- DHT sensor library
- LiquidCrystal I2C
- Wire (já vem instalada)

## Instalação

1. **Conecte os componentes** seguindo o diagrama:

 | Sensor       | Pino ESP32 |
 |--------------|-----------|
 | DHT22 (SDA) | GPIO4     |
 | LDR (AO) | GPIO34    |
 | Slide Switch (P) | GPIO5   |
 | Slide Switch (K) | GPIO18    |
 | Módulo Relé | GPIO16    |
 | LCD (SDA) | GPIO21    |
 | LCD (SCL) | GPIO22    |

![Circuito.png](https://github.com/Nico-Araujo/FIAP/blob/daa0bd65277efbab70b7c723deafc749e1cc6246/1TIAO/FASE4/Assets/Circuito.png)

 > **Importante:** Use os Resistores de 10kΩ entre a entrada do pino ESP32 e VCC no Slide Switch (P) e (K) (Fazendo um pull up)

2. **Configure a IDE Arduino**:
 - Selecione `Ferramentas > Placa > ESP32 Dev Module`
 - Escolha a porta COM correta

## 🚀 Execução

1. Copie o código deste repositório: [aqui](https://github.com/Nico-Araujo/FIAP/blob/daa0bd65277efbab70b7c723deafc749e1cc6246/1TIAO/FASE4/Projetos/Codigo-Circuito-FarmTech-ESP32.cpp)
2. Cole e execute no software escolhido (IDE Arduino, VS Code, Wokwi...)

## 🔋 Funcionalidades

Para verificar a funcionalidade do circuito, basta clicar [aqui](https://youtu.be/cWbJXAkzFV0) e você será redirecionado para o vídeo no Youtube. Se desejar fazer sua própria simulação, clique [aqui](https://wokwi.com/projects/434222558839003137)

- Inicialização do circuito:

![Plotter-variaveis-zeradas.png](https://github.com/Nico-Araujo/FIAP/blob/daa0bd65277efbab70b7c723deafc749e1cc6246/1TIAO/FASE4/Assets/Plotter-variaveis-zeradas.png)
Circuito iniciado e variáveis zeradas

- Ativação da bomba

![Plotter-var-bomba.png](https://github.com/Nico-Araujo/FIAP/blob/daa0bd65277efbab70b7c723deafc749e1cc6246/1TIAO/FASE4/Assets/Plotter-var-bomba.png)

- Leitura da variação de pH

![Plotter-var-pH.png](https://github.com/Nico-Araujo/FIAP/blob/daa0bd65277efbab70b7c723deafc749e1cc6246/1TIAO/FASE4/Assets/Plotter-var-pH.png)

- Leitura da variação de umidade

![Plotter-var-umidade.png](https://github.com/Nico-Araujo/FIAP/blob/daa0bd65277efbab70b7c723deafc749e1cc6246/1TIAO/FASE4/Assets/Plotter-var-umidade.png)

- Ativação do circuito

![Plotter-var-geral.png](https://github.com/Nico-Araujo/FIAP/blob/daa0bd65277efbab70b7c723deafc749e1cc6246/1TIAO/FASE4/Assets/Plotter-var-geral.png)
Nesta imagem do Serial Plotter, é possível observar o circuito em operação durante a simulação. Inicialmente, o solo apresentava níveis baixos de umidade, pH e nutrientes. Após o ajuste dos nutrientes (fósforo e potássio) e a ativação automática da bomba de irrigação, o sistema estabiliza-se progressivamente, atingindo condições ideais de cultivo e demonstrando perfeito equilíbrio.

## Principais Otimizações Aplicadas

1. Tipos de Dados Específicos
  - `uint8_t` para pinos (1 byte cada)
  - `int16_t` para leituras analógicas (2 bytes)
  - `bool` para estados lógicos (1 byte)

2.  Estrutura de Dados Organizada
  - `Struct SensorData` agrupa todas as variáveis relacionadas
  - Reduz fragmentação de memória

3. Otimização de Strings com F()
  - `Strings` constantes armazenadas na flash (PROGMEM)
  - Libera RAM (ex: lcd.print(F("Texto")))

4. Separação Clara de Funções
  - Cada função tem uma responsabilidade única
  - Código mais legível e manutenível

5. Formato Serial Plotter
  - Saída padronizada para visualização gráfica
  - `Labels` consistentes para cada variável

6. Operações Matemáticas Eficientes
  - Uso de `10.0f` para cálculos `float` otimizados
  - `map()` seguido de divisão para melhor precisão

## Benefícios das Otimizações

1. Economia de Memória RAM
  - Redução de ~35% no uso de memória em relação à versão original
  - Evita overflow em projetos maiores

2. Maior Velocidade de Execução
  - Tipos menores = processamento mais rápido
  - Operações matemáticas mais eficientes

3. Código Mais Profissional
  - Melhor organização e boas práticas
  - Facilidade para adicionar novos recursos

4. Compatibilidade Mantida
  - Todas as funcionalidades originais preservadas
  - Melhorias transparentes para o usuário final
