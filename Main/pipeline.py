import time
import datetime
import threading
from produce import produce
from consume import consume
def producer_thread():
    while True:
        produce()
        time.sleep(5)
def consumer_thread():
    while True:
        consume()
# Create separate threads for producer and consumer
producer_thread = threading.Thread(target=producer_thread)
consumer_thread = threading.Thread(target=consumer_thread)

# Start the threads
producer_thread.start()
consumer_thread.start()

# Wait for the threads to finish (which will never happen in this case as they run infinitely)
producer_thread.join()
consumer_thread.join()