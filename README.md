# Real-Time Financial Data Pipeline

This project implements a real-time data pipeline to collect, process, and visualize financial data using Kafka, MySQL, and Grafana. Data from financial assets is collected and streamed through Kafka, stored in MySQL, and visualized in Grafana.

## Project Overview
1. **Data Scraping**: Financial data is scraped from a designated source to obtain real-time updates on financial assets.
2. **Data Ingestion**: Real-time data is collected through the Kafka producer, which streams financial data on specific assets.
3. **Data Storage**: The data is processed and stored in a MySQL database.
4. **Data Visualization**: Using Grafana, the data is visualized in real-time, enabling monitoring and analysis of key financial metrics.

## Requirements

- **Kafka**: Used as the streaming platform to collect and stream data.
- **MySQL**: Stores processed financial data.
- **Grafana**: Visualizes the financial data in real-time.

## Installation

1. Clone the repository and navigate to the project folder:
    ```bash
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

- **Kafka**: Ensure Kafka is installed and running locally. Modify `bootstrap.servers` in the consumer configuration if necessary.
- **MySQL**: Update MySQL connection settings (host, user, password, database) in the code to match your local MySQL setup.

## Usage

1. **Start zookeper**:
    ```bash
    # In one terminal
    .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
    ```
    
2. **Start Kafka-server**:
   ```bash
    # In one terminal
    .\bin\windows\kafka-server-start.bat .\config\server.properties
    ```
   
3. **create the topic**:
   ```bash
    # In one terminal
    .\bin\windows\kafka-topics.bat --create --topic financial_data --bootstrap-server localhost:9092
   ```
   
4. **view list(optional)**:
    ```bash
    # In one terminal
    .\bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092
    ```
    
5. **Run Pipeline**: execute the pipeline script to send data to the Kafka topic and then store it into mysql.
    ```bash
    python pipeline.py
    ```
    
6. **Visualize in Grafana**:
    - Start Grafana and connect to MySQL as the data source.
    - Create dashboards for real-time visualization.

## Project Structure

- `producer.py`: Collects and sends financial data to the Kafka topic.
- `consumer.py`: Consumes data from Kafka and stores it in MySQL.
- `requirements.txt`: Python dependencies required for the project.

## Example Dashboard in Grafana

In Grafana, create panels to visualize metrics like **Current Price**, **Price Change**, and **Percent Change**.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributeurs :
- [Ibnchakroune Houssam] - Développeur principal

---

**Note :** Ce projet est à des fins éducatives et de démonstration. Les résultats obtenus peuvent varier en fonction de la qualité et de la quantité des données extraites.
