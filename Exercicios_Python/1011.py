"""
Não aceitaram desse jeito:

raio = float(input('Escreva o valor do raio')) #aparentemente não pode colocar texto no input
print(f'VOLUME = {(4 * 3.14159 * raio**3)/3:.3f}')

e nem desse:

r = float(input())
print(f'VOLUME = {(3.0 * 4.0 * 3.14159 * r ** 3)/3.0:.3f}')  # aparentemente a exponenciação tem q vir antes da multiplicação
"""
# exemplo 1:

raio = float(input())
r = (raio ** 3.0 * 4.0 * 3.14159)/3.0
print(f'VOLUME = {r:.3f}')

# exemplo 2
raio = float(input())
print(f'VOLUME = {(raio ** 3.0 * 4.0 * 3.14159)/3.0:.3f}')


# outra solução
RADIUS = float(input())

formula = (4.0/3)*3.14159 * (RADIUS**3)

print(f'VOLUME = {formula:.3f}')