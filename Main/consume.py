from confluent_kafka import Consumer, KafkaException
import json
import mysql.connector
from datetime import datetime
def consume():
    # Configuration du consumer
    consumer_conf = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'my_group',
        'auto.offset.reset': 'latest'
    }

    # Création du consumer
    consumer = Consumer(consumer_conf)

    # S'abonner au topic
    consumer.subscribe(['financial_data'])

    # Boucle pour lire les messages
    try:

            msg = consumer.poll()
            
            # Vérification de msg.value() avant de décoder
            if msg.value() is not None:
                data_list = json.loads(msg.value().decode('utf-8'))
                j=0
                connection = mysql.connector.connect(
                    host='localhost',         
                    user='root',              
                    password='0000',  
                    database='mydatabase'     
                )
                cursor = connection.cursor()
                delete_query = f"""  DELETE FROM crypto"""
                cursor.execute(delete_query)
                connection.commit()
                for i in data_list :
                    date_heure_actuelle = datetime.now()
                    c = float(i['c'])
                    ti=date_heure_actuelle.strftime('%Y-%m-%d %H:%M:%S')
                    d = float(i['d'])
                    dp = float(i['dp'])
                    h = float(i['h'])
                    l = float(i['l'])
                    o = float(i['o'])
                    pc = float(i['pc'])
                    t = float(i['t'])
                    
                    symbols=['BTC','ETH','SOL','LUMIA','LINK','ADA']
                    insert_query = f"""
                        INSERT INTO crypto 
                        (name,Current_Price,time, Price_Change, Percent_Change, High, Low, Open, Previous_Close, Timestamp) 
                        VALUES (%s,%s,%s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    
                    data = (symbols[j],c, ti,d, dp,h,l,o,pc,t) # Replace with actual data

                    # Execute the insert query
                    cursor.execute(insert_query, data)

                    # Commit the transaction to save the data
                    connection.commit()
                    j=j+1
                    
                cursor.close()
                connection.close()
            else:
                print("Message reçu: None (aucune donnée)")

    except KeyboardInterrupt:
        pass
    finally:
        # Fermeture du consumer proprement
        consumer.close()
