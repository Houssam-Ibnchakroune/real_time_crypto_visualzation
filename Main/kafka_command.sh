.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties


.\bin\windows\kafka-server-start.bat .\config\server.properties


.\bin\windows\kafka-topics.bat --create --topic financial_data --bootstrap-server localhost:9092


.\bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092


.\bin\windows\kafka-console-producer.bat --topic financial_data --bootstrap-server localhost:9092


.\bin\windows\kafka-console-consumer.bat --topic financial_data --from-beginning --bootstrap-server localhost:9092
