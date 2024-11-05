"""
Faça um programa que leia três valores e apresente o maior dos três valores
lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b).
Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
"""

# 1
a, b, c = map(int, input().split())

mAB = (a + b + abs(a - b)) / 2
mABC = (mAB + c + abs(mAB - c)) / 2

print(f'{mABC} eh o maior')

# 2

a, b, c = map(int, input().split())

maior_ab = (a + b + abs(a - b)) / 2
maior_abc = (maior_ab + c + abs(maior_ab - c)) / 2

print(f'{maior_abc:.0f} eh o maior')

# 3

a, b, c = map(int, input().split())

mAB = (a + b + abs(a - b)) / 2
mABC = (mAB + c + abs(mAB - c)) / 2

print(f'{mABC:.0f} eh o maior')


# Outra
A, B, C = input().split(" ")

A = int(A)
B = int(B)
C = int(C)

maiorAB = (A+B+abs(A-B))/2
maiorMAIORC = (maiorAB+C+abs(maiorAB-C))/2

MAIOR = int(maiorMAIORC)

print(f'{MAIOR} eh o maior')

