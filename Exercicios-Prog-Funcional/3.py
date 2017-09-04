#!/usr/bin/python
# coding: latin-1

#03. Defina uma função recursiva para calcular a potência de um numero 'b' elevado ao expoente 'e'.
# O calculo de 'b' elevado a 'e' se obtem com o produto de 'b' com sigo mesmo 'e' vezes."
# o expoente é < 2

def my_pow(b, e):
  if e < 2:
    return b
  else:
    pow = b * my_pow(b, e - 1)

print(pow(2, 5))
