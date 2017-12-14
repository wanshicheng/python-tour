#!/usr/bin/python
# -*- coding: UTF-8 -*-

def fib(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L


for n in fib(5):
    print(n)