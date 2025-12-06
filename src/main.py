'''
Main entry point for the producer-consumer system.

This script initializes the shared queu, starts the producer and 
consumer threads, waits for them to complete, and returns the consumed items.
'''

from shared_queue import shared_queue
from producer import Producer
from consumer import Consumer
from config import CONFIG

def run_system():
    max_size = CONFIG['queue_max_size']
    items = list(range(CONFIG['items_to_produce']))
    queue = shared_queue(max_size=max_size)
    consumed = [] 

    producer = Producer(queue, items + ['STOP'])
    consumer = Consumer(queue, consumed)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    return consumed 

if __name__ == '__main__':
    output = run_system()
    print(f"Consumed : {output}")
