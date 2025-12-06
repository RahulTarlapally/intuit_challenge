'''
This module defines the producer, which generates items and 
inserts them into the sahred queue. The producer waits if the queue is full
and resumes when space becomes available.
'''

import threading
import time 

class Producer(threading.Thread):
    def __init__(self, shared_queue, items, delay=0.1):
        super().__init__()
        self.shared_queue = shared_queue
        self.items = items 
        self.delay = delay 

    def run(self):
        for item in self.items:
            self.shared_queue.put(item)
            time.sleep(self.delay)
