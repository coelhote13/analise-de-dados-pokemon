# analise de dados pokemon

Projeto de análise de dados desenvolvido em Python utilizando dados da PokéAPI.

O objetivo da primeira versão é praticar um fluxo completo de análise de dados, desde a coleta das informações através de uma API até o tratamento, análise estatística e visualização dos dados.

# Sobre o projeto

Nesta V1 foram coletados dados dos 151 primeiros Pokémon utilizando a PokéAPI.

Os dados foram obtidos através de requisições HTTP com Python e posteriormente organizados em um arquivo CSV para realização da análise utilizando Pandas.

# Pipeline do projeto

PokéAPI
↓
Python
↓
Requests
↓
Pandas
↓
CSV
↓
Análise exploratória
↓
Matplotlib

## Tecnologias utilizadas

- Python
- Requests
- Pandas
- Matplotlib
- Git
- GitHub
- PokéAPI

## Dados utilizados

Foram coletados os seguintes dados:

- ID do Pokémon
- Nome
- Peso
- Altura

Os valores de peso e altura fornecidos pela API foram convertidos para:

- Peso → quilogramas (kg)
- Altura → metros (m)

## Análises realizadas

O projeto realiza uma análise exploratória dos dados, incluindo:

- Visualização inicial da base
- Verificação da quantidade de registros e colunas
- Verificação dos tipos de dados
- Identificação dos Pokémon mais pesados
- Identificação dos Pokémon mais altos
- Cálculo do peso médio
- Cálculo da mediana do peso
- Cálculo da altura média
- Cálculo da mediana da altura
- Cálculo da correlação entre peso e altura
- Visualização da relação entre altura e peso
