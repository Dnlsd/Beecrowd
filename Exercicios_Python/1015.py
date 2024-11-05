"""
Leia os quatro valores correspondentes aos eixos x e y de dois pontos_inicial quaisquer no plano,
p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula,
segundo a fórmula:

Distancia = ...

Entrada
O arquivo de entrada contém duas linhas de dados.
A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém
dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.

"""

from math import sqrt

p1x, p1y = map(float, input().split())
p2x, p2y = map(float, input().split())

d = sqrt((p2x-p1x)**2 + (p2y-p1y)**2)

print(f'{d:.4f}')


# Outra
X1, Y1 = input().split()
X2, Y2 = input().split()

X1 = float(X1)
X2 = float(X2)
Y1 = float(Y1)
Y2 = float(Y2)

dist = ((X2 - X1)**2 + (Y2 - Y1)**2) ** (1/2)

print(round(dist, 4))