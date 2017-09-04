#!/usr/bin/python
# coding: latin-1

# início - recursão mútua
# 04. Defina dois predicados lógicos '[even]' e '[odd]' que
# indiquem se um número 'n' passado como argumento é par ou ímpar respectivamente.
# Não é permitido o uso do operador '%' (resto da divisão).

def even(n):
    if n == 0:
        return True
    else:
        return odd(n-1)

def odd(n):
    if n == 0:
        return False
    else:
        return even(n-1)

print(even(5), even(6))
print(odd(5), odd(6))
