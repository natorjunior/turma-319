# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gpmUUa-FV6KOCjczcg3Q8xztgBhveUW0
"""

numeros = []
par = []
impar = []

for i in range(20):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print("Vetor completo:", numeros)
print("Vetor PAR:", par)
print("Vetor ímpar:", impar)3