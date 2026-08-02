# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/">
  <img src="../../assets/logo-fiap.png" 
       alt="FIAP - Faculdade de Informática e Administração Paulista" 
       width="40%">
</a>
</p>

<br>

# 🚀 FASE 2 — Arquiteto de Soluções e Dados
## 📚 Graduação ON em Inteligência Artificial

---

## 👩🏻‍💻 Sobre esta Fase

Esta fase representa uma etapa de aprofundamento na Graduação ON em Inteligência Artificial da FIAP.

Aqui estão organizados:

- 📖 Conteúdos teóricos estudados em modelagem de dados, bancos relacionais, persistência e análise exploratória estatística
- 🧠 Conceitos fundamentais de MER, DER, integração Python com Oracle DB e análise de variáveis
- 🛠 Tecnologias aplicadas em banco de dados relacional, linguagem R e automação de rotinas em Python
- 📂 Projetos desenvolvidos focados na modernização e gestão de insumos no Agronegócio
- 📊 Resultados obtidos através de modelagem relacional e relatórios estatísticos/gráficos
- 🎯 Competências técnicas e práticas adquiridas ao longo dos módulos

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

O foco principal desta fase foi dominar a arquitetura de dados relacional, a persistência de informações e a análise exploratória aplicada a cenários reais do Agronegócio.

- Projetar Modelos Entidade-Relacionamento (MER) e Diagramas Entidade-Relacionamento (DER) para sistemas de sensoriamento agrícola
- Desenvolver uma aplicação em Python conectada ao banco de dados Oracle com persistência local em JSON
- Implementar validações de entrada de dados, subalgoritmos reutilizáveis e menus interativos
- Coletar dados públicos do ecossistema do agronegócio (CONAB, IBGE, EMBRAPA) e realizar análise exploratória descritiva e gráfica utilizando a linguagem R

---

## 📖 Conteúdos Abordados

- **Modelagem Relacional (MER & DER):** Entidades, atributos (chaves primárias e estrangeiras), tipos de dados, cardinalidades (1:N e N:N) e normalização utilizando o SQL Developer Data Modeler.
- **Desenvolvimento & Persistência em Python:** Subalgoritmos (funções e procedimentos), manipulação de estruturas de dados (listas, dicionários, tuplas), manipulação de arquivos JSON e conexão com Oracle Database (`cx_Oracle`).
- **Análise Exploratória em R:** Classificação de variáveis (qualitativas nominais/ordinais e quantitativas discretas/contínuas), estatística descritiva (tendência central, dispersão, separatrizes) e visualizações gráficas.

---

## 🛠 Tecnologias Utilizadas

Durante esta fase, foram utilizadas as seguintes tecnologias:

- **Oracle Database & SQL:** Armazenamento relacional e execução de scripts DDL/DML
- **Oracle SQL Developer Data Modeler:** Criação do Diagrama Entidade-Relacionamento (DER)
- **Python 3:** Lógica da aplicação, tratamento de exceções, funções e persistência
- **R / RStudio:** Análise estatística exploratória e geração de gráficos
- **JSON:** Backup local estruturado dos dados do banco
- **Git & GitHub:** Versionamento colaborativo do repositório

---

## 📂 Projetos Desenvolvidos

### 📌 Projeto 1 — Modelagem do Banco de Dados FarmTech Solutions (MER/DER)

**Descrição:**  
Modelagem de um banco de dados relacional completo para armazenar leituras em tempo real enviadas por sensores agrícolas (umidade, pH, NPK) e registrar ações automatizadas de irrigação e adubação para diferentes culturas.

**Tecnologias utilizadas:**  
- Oracle SQL Developer Data Modeler  
- Markdown (MER)  

**Principais aprendizados:**  
- Definição precisa de entidades (`Sensor`, `Plantacao`, `Leitura`, `Ajuste`) e seus atributos.
- Resolução de relacionamentos N:N utilizando tabelas associativas/ligação (`Leitura_Plantacao`).
- Mapeamento correto de cardinalidades e definição de restrições de integridade referencial (PKs e FKs).

---

### 📌 Projeto 2 — Sistema de Gestão de Insumos Agrícolas com Oracle e Backup JSON

**Descrição:**  
Desenvolvimento de uma aplicação em Python que realiza o gerenciamento completo (CRUD) de insumos agrícolas (fertilizantes, sementes, defensivos), integrando diretamente a um banco de dados Oracle e disponibilizando rotinas automáticas de backup em arquivos JSON.

**Tecnologias utilizadas:**  
- Python 3  
- Oracle Database (`cx_Oracle`)  
- JSON  

**Principais aprendizados:**  
- Conexão e execução de instruções SQL seguras a partir do Python.
- Validação e consistência de dados digitados pelo usuário no terminal para evitar falhas de execução.
- Implementação de backups locais estruturados em formato JSON para garantia de redundância offline.

---

### 📌 Projeto 3 — Análise Estatística Exploratória de Dados Agrícolas em R

**Descrição:**  
Construção de um conjunto de dados a partir de fontes públicas do agronegócio (IBGE, CONAB, EMBRAPA) contendo variáveis qualitativas e quantitativas, acompanhada de um script R para cálculo de estatísticas descritivas e geração de gráficos de análise.

**Tecnologias utilizadas:**  
- Linguagem R  
- Microsoft Excel  

**Principais aprendizados:**  
- Identificação e classificação de variáveis (discreta, contínua, nominal e ordinal).
- Aplicação de medidas estatísticas: tendência central (média, mediana, moda), dispersão (variância, desvio padrão) e separatrizes (quartis).
- Criação e interpretação de representações gráficas para variáveis quantitativas e qualitativas em R.

---

## 🧠 Competências Desenvolvidas

Ao final desta fase, consolidei:

- ✔️ Modelagem de dados relacionais com aplicação prática de regras de negócio
- ✔️ Domínio de ferramentas industriais de modelagem (SQL Developer Data Modeler)
- ✔️ Integração avançada entre Python e bancos de dados SQL (Oracle)
- ✔️ Gestão e backup de dados em arquivos semiestruturados (JSON)
- ✔️ Capacidade de sanitizar e validar inputs do usuário via terminal
- ✔️ Realização de análises exploratórias estatísticas e visualizações gráficas com R
- ✔️ Versionamento rigoroso e organização de projetos no GitHub

---

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/SabrinaOtoni/TEMPLATE-FIAP-GRAD-ON-IA">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">FIAP</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
