# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Enterprise Challenge - Sprint 2 - Reply

## Nome do grupo

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/juliano-romeiro-rodrigues/">Juliano Romeiro Rodrigues</a>
- <a href="">Mariana Barbui dos Santos Zitelli</a>
- <a href="https://www.linkedin.com/in/nicolas--araujo/">Nicolas Antonio Silva Araujo</a> 
- <a href="https://www.linkedin.com/in/vitoria-bagatin-31ba88266/">Vitória Pereira Bagatin</a> 


## 📜 Descrição

Este projeto foi desenvolvido no contexto da metodologia PBL (Problem-Based Learning), visando criar um sistema de monitoramento industrial inteligente capaz de detectar condições anormais em máquinas e ambientes de produção. O objetivo principal é prevenir falhas, aumentar a segurança e otimizar a manutenção preditiva por meio da leitura em tempo real de três parâmetros críticos: temperatura, vibração e distância.
O sistema utiliza um microcontrolador ESP32, combinado com sensores de baixo custo, para fornecer alertas visuais e sonoros quando as condições operacionais ultrapassam limites pré-definidos. A solução é escalável e pode ser adaptada para diferentes cenários industriais, desde linhas de produção até equipamentos isolados


## 🔋 Componentes e Funcionalidades

Sensor de Temperatura (DS18B20)
Monitora a temperatura em °C.
Limites operacionais:
Normal: 0°C a 60°C
Alerta: >60°C (aciona LED amarelo)
Crítico: >80°C (aciona LED vermelho + buzzer)
Emergência: ≥90°C (desliga equipamento via relé)

Sensor de Vibração (MPU6050)
Mede aceleração em "g" (1g = 9.81 m/s²).
Limites operacionais:
Normal: 0.1g a 0.5g
Alerta: >1.0g (indica desbalanceamento)
Crítico: >2.0g (desliga máquina automaticamente)

Sensor de Distância (HC-SR04)
Detecta obstáculos ou falhas em esteiras industriais (faixa: 2cm a 4m).
Limites operacionais:
Normal: 10cm a 200cm
Alerta: <5cm (obstrução) ou >250cm (falta de peça)

Sistema de Alertas
LED Verde: Condições normais.
LED Amarelo: Alerta (parâmetro fora da faixa ideal, mas não crítico).
LED Vermelho + Buzzer (1000Hz): Emergência (ação imediata necessária).
Relé: Desliga equipamentos automaticamente em casos críticos.

## Circuito

<img = Circuito-Challenge-Esp32.png>


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>Simulação Sensores</b>: Nesta pasta se encontram os arquivos da coleta de dados de sensores com ESP32 em ambiente simulado. Em vez de dados reais, usamos dados gerados e analisados em R.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

*Acrescentar as informações necessárias sobre pré-requisitos (IDEs, serviços, bibliotecas etc.) e instalação básica do projeto, descrevendo eventuais versões utilizadas. Colocar um passo a passo de como o leitor pode baixar o seu código e executá-lo a partir de sua máquina ou seu repositório. Considere a explicação organizada em fase.*

