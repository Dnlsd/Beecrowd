# As primeiras tentativas caem no erro da aproximação do float 0.01 

# A última solução é a melhor


# Não aceitou o resultado!
value = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.10, 0.05, 0.01]

troco_notas = []
troco_moedas = []

for nota in notas:

    if value >= nota:

        inteiro = value // nota
        value %= nota

        troco_notas.append(int(inteiro))

    else:
        continue



for moeda in moedas:

    if value >= moeda:

        inteiro = value // moeda
        value %= moeda

        troco_moedas.append(int(inteiro))

    else:
        continue



print("NOTAS:")
for indice, troco in enumerate(troco_notas):

    print(f"{troco} nota(s) de R$ {notas[indice]:.2f}" )

print("MOEDAS:")
for indice, troco in enumerate(troco_moedas):

    print(f"{troco} moeda(s) de R$ {moedas[indice]:.2f}" )


# Não aceitou o resultado!

value = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.10, 0.05, 0.01]

troco_notas = []
troco_moedas = []

print("NOTAS:")
for nota in notas:

    if value >= nota:

        inteiro = value // nota
        value %= nota

        troco_notas.append(int(inteiro))

    else:
        inteiro = 0
        troco_notas.append(inteiro)
    
    print(f"{inteiro:.0f} nota(s) de R$ {nota:.2f}" )


print("MOEDAS:")
for moeda in moedas:

    if value >= moeda:

        inteiro = value // moeda
        value %= moeda

        troco_moedas.append(int(inteiro))

    else:
        inteiro = 0
        troco_moedas.append(0)


    print(f"{inteiro:.0f} moeda(s) de R$ {moeda:.2f}" )


# Não aceitou o resultado!

value = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for nota in notas:

    inteiro = value // nota
    value %= nota
    
    print(f"{inteiro:.0f} nota(s) de R$ {nota:.2f}" )


print("MOEDAS:")
for moeda in moedas:

    inteiro = value // moeda
    value %= moeda


    print(f"{inteiro:.0f} moeda(s) de R$ {moeda:.2f}" )


############################################# resultados aceitos ##############################


# 1
value = float(input())

# Converta o valor para centavos para evitar problemas com ponto flutuante
value = int(round(value * 100))

notas = [10000, 5000, 2000, 1000, 500, 200]  # Notas em centavos
moedas = [100, 50, 25, 10, 5, 1]  # Moedas em centavos

print("NOTAS:")
for nota in notas:
    inteiro = value // nota  # Quantidade de notas
    value %= nota  # Resto
    print(f"{inteiro} nota(s) de R$ {nota / 100:.2f}")

print("MOEDAS:")
for moeda in moedas:
    inteiro = value // moeda  # Quantidade de moedas
    value %= moeda  # Resto
    print(f"{inteiro} moeda(s) de R$ {moeda / 100:.2f}")


# 2 -> esse é bão (628 bytes)

value = float(input())

value = int(round(value * 100))

dinheiros = [[10000, 5000, 2000, 1000, 500, 200], 
             [100, 50, 25, 10, 5, 1]]

for dinheiro in dinheiros:

    if dinheiro == dinheiros[0]:
        
        print("NOTAS:")

        for nota in dinheiro:

            inteiro = value // nota  
            value %= nota  

            print(f"{inteiro} nota(s) de R$ {nota / 100:.2f}")

    else:
        
        print("MOEDAS:")

        for moeda in dinheiro:

            inteiro = value // moeda 
            value %= moeda 

            print(f"{inteiro} moeda(s) de R$ {moeda / 100:.2f}")


# 3 -> ESSE É O MELHOR (616 Bytes)

value = float(input())
value = int(round(value * 100))

carteira = [[(10000, 'nota'), (5000, 'nota'), (2000, 'nota'), (1000, 'nota'), (500, 'nota'), (200, 'nota')], 
             [(100, 'moeda'), (50, 'moeda'), (25, 'moeda'), (10, 'moeda'),(5, 'moeda'), (1, 'moeda')]]

for compartimento in carteira:

    if compartimento == carteira[0]:
        print("NOTAS:")
        
    else:
        print('MOEDAS:')
        
    for dinheiro, texto in compartimento:

        inteiro = value // dinheiro  
        value %= dinheiro  

        print(f"{inteiro} {texto}(s) de R$ {dinheiro / 100:.2f}")
