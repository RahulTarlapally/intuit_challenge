'''
Reads a CSV file and retuns a list of dictionaries
'''

import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, ROOT_DIR)
SRC_DIR = os.path.join(ROOT_DIR, 'data')
sys.path.insert(0, SRC_DIR)

import csv 

def read_csv(path):
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)
    return []
