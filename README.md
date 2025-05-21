#  Extração de Dados da API Coinbase

Este projeto tem como objetivo realizar a extração de dados de criptomoedas utilizando a API pública da [Coinbase](https://www.coinbase.com/), com foco na obtenção de informações em tempo real sobre preços, moedas suportadas e histórico de transações.

## Objetivos

- Conectar-se à API pública da Coinbase.
- Obter dados atualizados sobre as principais criptomoedas.
- Salvar os dados extraídos em arquivos ou banco de dados (dependendo da necessidade).
- Analisar e/ou visualizar os dados extraídos.

##  Tecnologias Utilizadas

- **Linguagem:** Python 3.x  
- **Bibliotecas:**
  - `requests` – para fazer requisições HTTP à API
  - `pandas` – para manipulação de dados (opcional)
  - `json` – para manipular respostas em formato JSON
  - `datetime` – para lidar com datas e horários

## API Utilizada

- **Base URL da API Coinbase:**  
  `https://api.coinbase.com/v2/`

- **Endpoints mais utilizados:**
  - `/currencies` – Lista de todas as moedas suportadas
  - `/exchange-rates` – Taxas de câmbio
  - `/prices/{crypto}-USD/spot` – Preço atual de uma criptomoeda
  - `/time` – Hora atual do servidor

## Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/kingsonPaxe/Extracao-de-uma-API-Coin-Base-.git
   cd Extracao-de-uma-API-Coin-Base