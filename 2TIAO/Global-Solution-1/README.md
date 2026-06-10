# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# 🎓 Graduação ON em Inteligência Artificial  

# SkyGuard Defense System

## Nome do grupo: [INSIRA O NOME DO GRUPO AQUI]

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/nicolas--araujo/">Nicolas Antonio Silva Araujo</a> 
- <a href="https://www.linkedin.com/in/vitoria-bagatin-31ba88266/">Vitória Pereira Bagatin</a> 

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="LINK_LINKEDIN">Nome do Tutor</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/andregodoichiovato/">André Godoi Chiovato</a>


## 📜 Descrição
O espaço deixou de ser apenas um território científico e passou a representar uma das maiores fronteiras tecnológicas e estratégicas da atualidade. Com o aumento exponencial de dispositivos, satélites e tráfego aeroespacial, a segurança e o monitoramento autônomo tornaram-se pilares fundamentais da nova economia espacial. O **SkyGuard Defense System** surge como uma Prova de Conceito (POC) inovadora, desenvolvida para responder ao desafio de como a Inteligência Artificial e a automação podem impulsionar soluções de monitoramento remoto e segurança em ambientes críticos.

O SkyGuard atua como um sistema de defesa aeroespacial inteligente, capaz de detectar, rastrear e analisar Fenômenos Aéreos Não Identificados (UAPs) em tempo real. A solução elimina a dependência de processos manuais de vigilância, integrando quatro camadas tecnológicas distintas para garantir uma resposta autônoma:

* **Percepção (Visão Computacional):** Utilizando algoritmos de subtração de fundo e detecção de movimento com OpenCV, o sistema monitora o céu em tempo real. Ele extrai propriedades cinemáticas e morfológicas (como velocidade em Mach, aceleração em G, formato e assinatura térmica) de qualquer objeto detectado.
* **Triagem e Filtragem (Edge Computing):** O sistema cruza as coordenadas detectadas com a API da OpenSky Network, filtrando tráfego aéreo comercial conhecido e processando apenas o que é, de fato, uma anomalia.
* **Inteligência Preditiva (Machine Learning):** Dados filtrados são submetidos a um pipeline de Machine Learning (Isolation Forest e Random Forest). O modelo, treinado com base sintética e histórica, distingue com alta precisão objetos convencionais de anomalias físicas.
* **IA Generativa e RAG:** Ao identificar uma anomalia, o SkyGuard aciona um agente inteligente baseado em RAG (Llama 3 local). O sistema processa documentos técnicos e relatórios aeroespaciais oficiais da NASA e AARO para gerar um parecer técnico fundamentado para o operador.

A solução é consolidada através de um Dashboard Inteligente e integração IoT (simulação via ESP32) para alertas físicos. O SkyGuard representa a integração prática de conhecimentos de IA, provando que a convergência tecnológica é o caminho para resolver problemas da nova fronteira espacial.

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>docs</b>: Pasta destinada à documentação, incluindo relatórios de métricas (`relatorio_metricas.txt`) e diagramas de arquitetura.
- <b>src</b>: Todo o código fonte desenvolvido.
    - `01_dataset/`: Script de geração de dados e o dataset gerado (`anomalias_uap.csv`).
    - `02_machine_learning/`: Treinamento e salvamento do modelo (`modelo_uap.joblib`).
    - `03_visao_computacional/`: Script de detecção via OpenCV.
    - `agente_rag.py`: Cérebro analítico que cruza dados com relatórios da NASA.
    - `index.html`: Dashboard de monitoramento em tempo real.
- <b>README.md</b>: Arquivo guia do projeto.

## 📎 Links e Observações

- <b>Vídeo de Apresentação</b>: [INSERIR LINK DO YOUTUBE AQUI]
- <b>Explicação de decisões técnicas</b>: Optamos por uma arquitetura de processamento local (Edge Computing) com Ollama para garantir que o sistema de defesa seja independente de latência de rede e mantenha a privacidade de dados aeroespaciais sensíveis.
- <b>Observações Gerais</b>: O projeto é uma POC (Prova de Conceito). Aceitamos participar da competição do pódio.

## 🔧 Como executar o código

### Pré-requisitos
Instale as bibliotecas necessárias:
pip install numpy pandas scikit-learn joblib opencv-python langchain langchain-community langchain-huggingface chromadb pypdf

Passo a passo
Gerar Base de Dados:

```Bash
python src/01_dataset/gerar_dataset.py
```

Treinar Modelo de IA:

```Bash
python src/02_machine_learning/treinar_modelo.py
```
Executar Detecção:

```Bash
python src/03_visao_computacional/detectar_objetos.py --webcam
```

Rodar Agente de Inteligência (RAG):
```Bash
python src/agente_rag.py
```

Dashboard:
Basta abrir o arquivo src/index.html em qualquer navegador.

🗃 Histórico de lançamentos
1.0.0 - 10/06/2026

Entrega da POC completa: Integração de visão, ML, RAG e Dashboard.
