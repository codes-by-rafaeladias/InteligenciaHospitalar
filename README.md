# Projeto de Inteligência Hospitalar

## Objetivo

Este projeto tem como objetivo desenvolver um estudo de caso utilizando o conjunto de dados [Diabetes 130-US Hospitals for Years 1999-2008](https://www.kaggle.com/datasets/sulphatet/diabetes-130us-hospitals-for-years-19992008), disponibilizado no Kaggle.

A proposta consiste em explorar os dados hospitalares relacionados a pacientes com diabetes, identificar padrões e extrair informações relevantes sobre internações e readmissões hospitalares.

O projeto está dividido em seis etapas:

1. ETL (Extração, Transformação e Carga) dos dados;
2. Análise exploratória utilizando Pandas e Matplotlib;
3. Consultas e extração de informações com SQL e PostgreSQL;
4. Modelagem de dados em estruturas relacionais e dimensionais;
5. Desenvolvimento de um pipeline de integração e alimentação de um sistema inteligente;
6. Elaboração de um dashboard para visualização dos indicadores identificados.

## Metodologia

### 1. ETL dos dados

Extração, transformação e limpeza do conjunto de dados, incluindo o tratamento de valores ausentes, duplicidades e inconsistências.
Após a preparação, os dados foram carregados em uma tabela denominada `readmissoes_diabetes`, armazenada no banco de dados `inteligencia_hospitalar`, utilizando PostgreSQL.

Mais informações:
- [Notebook de análise exploratória](notebooks/analise_exploratoria.ipynb)
- [Scripts do projeto](src/)

### 2. Análise exploratória

Obtenção de informações registradas na base de dados, criação de gráficos e outros visuais e manipulação de indicadores, utilizando as bibliotecas Pandas e Matplotlib.

- [Notebook de análise exploratória](notebooks/analise_exploratoria.ipynb)
- [Scripts do projeto](src/analysis)

### 3. Consultas SQL

Realização de consultas SQL utilizando funções (COUNT, AVG, MAX, COALESCE, ROUND, WHERE, GROUP BY, ORDER BY, LIMIT, FILTER), CTEs, sub-consultas para encontrar informações como:

- Quantidade total de internações;
- Quantidade de pacientes;
- Tempo médio de internação;
- Taxa geral de readmissão;
- Histórico hospitalar de um paciente.

- [Consultas SQL realizadas com auxílio das bibliotecas Pandas e SQLAlchemy](sql/queries.py)

### 4. Modelagem de dados

<!-- Descrever a modelagem relacional e dimensional. -->

### 5. Pipeline de dados

<!-- Descrever a integração e alimentação do sistema inteligente. -->

### 6. Dashboard

<!-- Descrever os indicadores e visualizações desenvolvidos. -->

## Tecnologias Aplicadas

<!-- Listar as tecnologias e bibliotecas utilizadas. -->

## Estrutura do Projeto

<!-- Apresentar a organização dos diretórios e arquivos. -->

## Como Executar

<!-- Apresentar as instruções de instalação e execução. -->
