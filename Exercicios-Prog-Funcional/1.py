#!/usr/bin/python
# coding: latin-1

# 01. Defina uma função recursiva que calcule 'n!'
# 'n!' é o produto de todos os inteiros positivos menores ou iguais a 'n'.

def fatorialA(n):
    if n <= 1:
        return 1
    else:
        return n * fatorialA(n - 1)

def fatorialB(n):
    r, i = 1, 1
    while i <= n:
        r = r * i
        i = i + 1
    return r


print(fatorialA(5))
print(fatorialB(5))
