#!/usr/bin/python
# coding: latin-1
# 06. Defina a função recursiva '[digits]' que some os dígitos
# de um 'n' algarismo passado por parametro. Por exemplo,
# digits (125) = 1 + 2 + 5 = 8.

def digits(n):
    if n <= 9:
        return n
    else:
        return n % 10 + digits(n // 10)

print(digits (5))  #5
print(digits (25))  #7
print(digits (125))  #8
