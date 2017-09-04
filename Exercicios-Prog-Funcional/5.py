#!/usr/bin/python
# coding: latin-1

# 05. Defina uma função recursiva [addUp] que retorne
# a soma dos 'n' primeros números naturais. Por exemplo // addUp (3) = 1 + 2 + 3 = 6.

def addUp(n):
    if n == 1:
        return 1
    else:
        return n + addUp(n - 1)

print(addUp(3))
