import requests
from confluent_kafka import Producer
import json
import time
def produce() :
    def get_ethusd_price():
        url = "https://finnhub.io/api/v1/quote"
        symbols=['BINANCE:BTCUSDT','BINANCE:ETHUSDT','BINANCE:SOLUSDT','BINANCE:LUMIAUSDT','BINANCE:LINKUSDT','BINANCE:ADAUSDT']
        data = []
        for i in symbols :
            params = {
                'symbol': i,
                'token': 'csb2n2hr01qobflkgv2gcsb2n2hr01qobflkgv30'
            }
            response = requests.get(url, params=params)
            data1 = response.json()
            data.append(data1)
        return data
    # Configuration du producteur Kafka
    producer_config = {
        'bootstrap.servers': 'localhost:9092',  # Le serveur Kafka
    }

    producer = Producer(producer_config)

    def acked(err, msg):
        """ Fonction de callback pour confirmation de l'envoi """
        if err is not None:
            print(f"Failed to deliver message: {err}")
        else:
            print(f"Message delivered to {msg.topic()} [{msg.partition()}]")




    data = get_ethusd_price()
    producer.produce('financial_data', value=json.dumps(data))
    producer.flush()
    print(f"Data sent: {data}")
