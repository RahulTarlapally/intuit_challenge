'''
Unit test for the producer-consumer system.
'''

import sys
import os 

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, ROOT_DIR)
SRC_DIR = os.path.join(ROOT_DIR, 'src')
sys.path.insert(0, SRC_DIR)

import time 
from src.shared_queue import shared_queue
from src.producer import Producer
from src.consumer import Consumer

def test_producer_consumer():
    queue = shared_queue(max_size=3)
    items = [1,2,3,4]
    consumed = [] 

    producer = Producer(queue, items + ['STOP'], delay=0)
    consumer = Consumer(queue, consumed, delay=0)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    assert consumed == items

    print('Yahoo! Test Passed')
    
  
if __name__ == '__main__':
    test_producer_consumer()
