'''
This module defines a thread-safe queue using a condition variable.
It provides blocking put() and get() methods for implementing the 
producer-consumer pattern with proper thread synchronization.
'''

import threading

class shared_queue:
    def __init__(self, max_size):
        self.queue = [] 
        self.max_size = max_size 
        self.condition = threading.Condition()

    def put(self, item):
        with self.condition:
            while len(self.queue) >= self.max_size:
                self.condition.wait()

            self.queue.append(item)
            self.condition.notify()


    def get(self):
        with self.condition:
            while len(self.queue) == 0:
                self.condition.wait()

            item = self.queue.pop(0)
            self.condition.notify()
            return item
