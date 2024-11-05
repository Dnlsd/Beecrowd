"""
Leia um valor inteiro.
A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido.
Não esqueça de imprimir o fim de linha após cada linha,
caso contrário seu programa apresentará a mensagem: “Presentation Error”.
"""

# A última solução é a melhor

# Não foi aceita

valor_em_dinheiro = int(input('Insira o valor aqui'))
lista_de_cedulas = (100, 50, 20, 10, 5, 2, 1)

if 0 < valor_em_dinheiro < 1000000:
    print(f'O valor é {valor_em_dinheiro}')
    for a in lista_de_cedulas:
        quantidade = valor_em_dinheiro // a       # O operador // realiza uma divisão inteira,
        print(f'{quantidade} nota(s) de {a},00')  # ou seja, retorna apenas a parte inteira do resultado da divisão.
        valor_em_dinheiro %= a
print(f'O valor {valor_em_dinheiro} é auto demais.')

# 1

valor = int(input())

notas = [100, 50, 20, 10, 5, 2, 1]

print(valor)
for nota in notas:
    quantidade_notas = valor // nota
    print(f"{quantidade_notas} nota(s) de R$ {nota},00")
    valor %= nota

# outra solução (não aceita, pq a os valores das notas era inteiros)
valor = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]
lista = []

for nota in notas:

    #valor menor que a nota:
    if (valor < nota):
        lista.append((0, nota))

    # valor igual OU maior que a nota
    else:
        if valor == nota:
            qtd_notas = int(valor / nota) 
            lista.append((qtd_notas, nota))
            valor = valor % nota

        else: #valor maior que a nota
            qtd_notas = int(valor / nota)
            lista.append((qtd_notas, nota))
            valor = valor % nota

for i in lista:
    print(f'{valor}')
    print(f"{i[0]} notas(s) de R$ {i[1]}")

# outra solução (aceita pelo Beecrown)
valor = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]
lista = []

print(valor)

for nota in notas:

    #valor menor que a nota:
    if (valor < nota):
        lista.append((0, nota))

    # valor igual OU maior que a nota
    else:
        if valor == nota:
            qtd_notas = int(valor / nota) 
            lista.append((qtd_notas, nota))
            valor = valor % nota

        else: #valor maior que a nota
            qtd_notas = int(valor / nota)
            lista.append((qtd_notas, nota))
            valor = valor % nota

print(f'{lista[0][0]} nota(s) de R$ 100,00')
print(f'{lista[1][0]} nota(s) de R$ 50,00')
print(f'{lista[2][0]} nota(s) de R$ 20,00')
print(f'{lista[3][0]} nota(s) de R$ 10,00')
print(f'{lista[4][0]} nota(s) de R$ 5,00')
print(f'{lista[5][0]} nota(s) de R$ 2,00')
print(f'{lista[6][0]} nota(s) de R$ 1,00')



# melhorando.....
valor = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]
lista = []

print(valor)

for nota in notas:

    #valor menor que a nota:
    if (valor < nota):
        lista.append((0, nota))

    # valor igual OU maior que a nota
    else:
        if valor == nota:
            qtd_notas = int(valor / nota) 
            lista.append((qtd_notas, nota))
            valor = valor % nota

        else: #valor maior que a nota
            qtd_notas = int(valor / nota)
            lista.append((qtd_notas, nota))
            valor = valor % nota

for i, nota in lista:
    print(f'{i} nota(s) de R$ {nota},00')