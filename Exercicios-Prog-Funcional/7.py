#!/usr/bin/python
# coding: latin-1

# 01. Defina uma função recursiva [mirror] para determinar se um número inteiro 'n' é simétrico a outro número inteiro m.
# Construir a partir daqui a função [palindrome] que indica se um número é simétrico a respeito de si mesmo.

def reverse(n):
    return reverseAux(n, 0)

def reverseAux(n, a):
    if n == 0:
        return a
    else:
        return reverseAux((n / 10), a * 10 + n % 10)

def mirror(n, m):
    return reverse(n) == m

def palindrome(n):
    return reverse(n) == n

print(reverse(125))             # 521
print(mirror(1, 7))            # false
print(mirror(0, 0))            # true
print(mirror(123, 321))        # true
print(mirror(123, 123))        # false
print(mirror(123, 132))        # false
print(palindrome(123))         # false
print(palindrome(12321))       # true
print(palindrome(1221))        # true
