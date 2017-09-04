#!/usr/bin/python
# coding: latin-1

# 02. Defina uma  função recursiva que calcule o enesimo término da sucessão de Fibonacci.
# O dito término se obtem com a soma dos dois terminos anteriores da sucessão.

def fibonacciA(n):
    if n <= 2:
        return 1
    else:
        return fibonacciA(n - 1) + fibonacciA(n - 2)

def fibonacciB(n):
    a = 1
    b = 1
    i = 2
    while i < n:
        b = a + b
        a = b - a
        i = i + 1
    return b


print(fibonacciA(10))
print(fibonacciB(10))
