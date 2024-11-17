"""
Sum: (N1*D2 + N2*D1) / (D1*D2)
Subtraction: (N1*D2 - N2*D1) / (D1*D2)
Multiplication: (N1*N2) / (D1*D2)
Division: (N1/D1) / (N2/D2), that means (N1*D2)/(N2*D1)

"n1 / n2 (/, *, +, -) d1 / d2"
"""
# solução (961 Bytes):

n_de_expressoes = int(input())

for n in range(n_de_expressoes):

    expressao = input()
    elementos = expressao.split()

    for char in elementos:
        
        n1 = int(elementos[0])
        n2 = int(elementos[4])

        operador = elementos[3]

        d1 = int(elementos[2])
        d2 = int(elementos[6])

    operadores = ['+', '-', '*', '/']
    operacoes = [((n1*d2)+(n2*d1), d1*d2), 
                ((n1*d2)-(n2*d1), d1*d2), 
                (n1*n2, d1*d2), 
                (n1*d2, n2*d1)]

    operacoes_dict = {sim: op for sim, op in zip(operadores,operacoes)}

    for operacao in operacoes_dict.items():

        if operador == operacao[0]:

            # é necessário aplicar a operação para que o MDC seja dos números transformados
            # assim, a simplificação desejada acontecerá. Caso contrário o MDC será dos números
            # Originais imputados, o que não faz sentido para a simplificação do números finais (após sofrerem a operação).
            den1, den2 = operacao[1] 

            while den2 != 0:
                den1, den2 = den2, den1 % den2
                
            print(f'{operacao[1][0]}/{operacao[1][1]} = {int(operacao[1][0]/den1)}/{int(operacao[1][1]/den1)}')
            break
