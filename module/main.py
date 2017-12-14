import sys
import os
BASE_DIR = os.path.abspath(__file__)
sys.path.append(BASE_DIR)



from calculator import *
import pack.test as test

def add(x, y):
    return x + y + 1

print(add(1, 2))
print(test.delete(3, 2))

print(__file__)