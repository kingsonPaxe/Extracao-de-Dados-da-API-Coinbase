import requests 
from pymongo import MongoClient
from datetime import datetime
from time import sleep

# Extracao de API coinbase
# A API coinbase fornece dados de preços de criptomoedas
def extract_dados_bitCoin(url:str):
    response = requests.get(url)
    return response.json()['data']

def transform_dados_bitCoin(dados):
    #mudar o nome dos valores
    moeda = dados['currency']
    criptomoeda = dados['base']
    valor = dados['amount']
    timestamp  = datetime.now().timestamp()
    dados_transformandos = {
        'Valor': valor,
        'Criptomoeda': criptomoeda,
        'Moeda': moeda,
        'Timestamp': timestamp
    }
    return dados_transformandos


#Salvando em banco de dados csv e nowsql
def load_dados_bitcoin(dados_json):
    client = MongoClient("mongodb://localhost:27017/") # Conexão com o MongoDB
    db = client['CoinBase']
    colecao = db['Dados_CoinBase']
    colecao.insert_one(dados_json)

    with open(r'Data/dados_bitcoin.csv', 'a') as f:
        f.write(f"{dados_json['Valor']},{dados_json['Criptomoeda']},{dados_json['Moeda']}, {dados_json['Timestamp']}\n")

    print('Dados salvos com sucesso no MongoDB e no arquivo CSV!')
# Salvando no os dados no mongoDb
if __name__ == "__main__":
    while True:
        dados_json = extract_dados_bitCoin('https://api.coinbase.com/v2/prices/spot')
        dados_tratados = transform_dados_bitCoin(dados_json)
     
        # print('Dados originais: ',dados_json)
        # print('Dados transformados: ',dados_tratados)
        load_dados_bitcoin(dados_tratados)
        sleep(15)