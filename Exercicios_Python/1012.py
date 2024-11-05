"""
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C.
Em seguida, calcule e mostre:

a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.

Entrada
O arquivo de entrada contém três valores com um dígito após o ponto decimal.

Saída
O arquivo de saída deverá conter 5 linhas de dados.
Cada linha corresponde a uma das áreas descritas acima, sempre com mensagem correspondente e um espaço entre
os dois pontos_inicial e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.


# Não aceitou:
A, B, C = float(input()), float(input()), float(input())

area_triangulo_ret = (A * C) / 2
area_circulo = C ** 2 * 3.14159
area_t = ((A + B) * C) / 2
quad = B * 2
ret = A * B

print(f'TRIANGULO: {area_triangulo_ret:.3f}')
print(f'CIRCULO: {area_circulo:.3f}')
print(f'TRAPEZIO: {area_t:.3f}')
print(f'QUADRADO: {quad:.3f}')
print(f'TRIANGULO: {ret:.3f}')
"""

# 1
a, b, c = map(float, input().split())

triangulo = a * c / 2
circulo = 3.14159 * c ** 2
trapezio = (a + b) * c / 2
quadrado = b ** 2
retangulo = a * b

print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")


# 2
# A, B C = map(float(), input().split(" "))
A, B, C = input().split(" ")
A = float(A)
B = float(B)
C = float(C)


area_tri = (A * C)/2
area_circ = C**2 * 3.14159
area_trap = (A + B)*C/2
area_sq = B*B
are_rect = A * B

print(f'TRIANGULO: {area_tri:.3f}\nCIRCULO: {area_circ:.3f}\nTRAPEZIO: {area_trap:.3f}\nQUADRADO: {area_sq:.3f}\nRETANGULO: {are_rect:.3f}')
