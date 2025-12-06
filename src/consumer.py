'''
This module defines the consumer thread, which retriveds items from the 
shared queue. The consumer waits if the queue is empty and stops
when it receives the special STOP signal
'''

import threading
import time 

class Consumer(threading.Thread):
    def __init__(self, shared_queue, consumed_output, delay=0.15):
        super().__init__()
        self.shared_queue = shared_queue
        self.delay = delay 
        self.consumed_output = consumed_output

    def run(self):
        while True:
            item = self.shared_queue.get()
            if item == 'STOP':
                break 
            self.consumed_output.append(item)
            time.sleep(self.delay)
