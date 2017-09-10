#!/usr/bin/python
# -*- coding: utf-8 -*-

# 08. Defina uma função recursiva [addV] que dado um vetor v calcule a soma de todos os seus elementos.
# Por exemplo, addV([1,2,3]) = 1 + 2 + 3 = 6.

def addVA(v):
    def addVAFrom(v, p):
        if p > (len(v) - 1):
            return 0
        else:
            return addVAFrom (v, p + 1) + v [p]
    return addVAFrom(v, 0)

def addVB(v):
    def addVBUp(v, p):
        if p == 0:
            return v [p]
        else:
            return addVBUp(v, p - 1) + v [p]
    return addVBUp(v, len(v) - 1)


print(addVA([1,2,3,4,5])) # 15
print(addVB([1,2,3,4,6])) # 16
