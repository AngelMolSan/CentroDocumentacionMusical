#!/usr/bin/env python
from ipaddress import summarize_address_range


def operar(a,b):
    global suma
    global resta
    suma = a + b
    resta = a - b
    print(suma,resta)

if __name__ == '__main__':
    operar(4,5)
    print(suma)
    print(resta)
