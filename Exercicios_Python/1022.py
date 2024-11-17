################################### VEJA A SOLUÇÃO 5! ###################################

"""
Sum: (N1*D2 + N2*D1) / (D1*D2)
Subtraction: (N1*D2 - N2*D1) / (D1*D2)
Multiplication: (N1*N2) / (D1*D2)
Division: (N1/D1) / (N2/D2), that means (N1*D2)/(N2*D1)

"n1 / n2 (/, *, +, -) d1 / d2"
"""

# # solução (961 Bytes):

# n_de_expressoes = int(input())

# for n in range(n_de_expressoes):

#     expressao = input()
#     elementos = expressao.split()

#     for char in elementos:
        
#         n1 = int(elementos[0])
#         n2 = int(elementos[4])

#         operador = elementos[3]

#         d1 = int(elementos[2])
#         d2 = int(elementos[6])

#     operadores = ['+', '-', '*', '/']
#     operacoes = [((n1*d2)+(n2*d1), d1*d2), 
#                 ((n1*d2)-(n2*d1), d1*d2), 
#                 (n1*n2, d1*d2), 
#                 (n1*d2, n2*d1)]

#     operacoes_dict = {sim: op for sim, op in zip(operadores,operacoes)}

#     for operacao in operacoes_dict.items():

#         if operador == operacao[0]:

#             # é necessário aplicar a operação para que o MDC seja dos números transformados
#             # assim, a simplificação desejada acontecerá. Caso contrário o MDC será dos números
#             # Originais imputados, o que não faz sentido para a simplificação do números finais (após sofrerem a operação).
#             den1, den2 = operacao[1] 

#             while den2 != 0:
#                 den1, den2 = den2, den1 % den2
                
#             print(f'{operacao[1][0]}/{operacao[1][1]} = {int(operacao[1][0]/den1)}/{int(operacao[1][1]/den1)}')
#             break


# # solução 2 (rascunho):

# n_de_expressoes = int(input())

# for n in range(n_de_expressoes):

#     expressao = input()
#     elementos = expressao.split()

#     for char in elementos:
        
#         n1 = int(elementos[0])
#         n2 = int(elementos[4])

#         operador = elementos[3]

#         d1 = int(elementos[2])
#         d2 = int(elementos[6])

#     operadores = ['+', '-', '*', '/']
    
#     # soma_sub = [(eval(f'{(n1*d2)}' f'{n}' f'{(n2*d1)}'), (int(f'{d1*d2}'))) for i, n in enumerate(operadores) if i < 2]
#     soma_sub = [(n, (eval(f'{(n1*d2)}' f'{n}' f'{(n2*d1)}'), (int(f'{d1*d2}')))) for i, n in enumerate(operadores) if i < 2]
#     # mult_div = [(n1*n2, d1*d2) if n == '*' else (n1*d2, n2*d1) for n in operadores if n == '*' or n == '/']
#     # mult_div = [(n, (n1*n2, d1*d2)) if n == '*' else (n, (n1*d2, n2*d1)) for n in operadores if n == '*' or n == '/']
#     mult_div = [(n, (n1*n2, d1*d2) if n == '*' else (n1*d2, n2*d1)) for n in operadores if n == '*' or n == '/']
    
#     oper = [(n, (eval(f'{(n1*d2)}' f'{n}' f'{(n2*d1)}'), (int(f'{d1*d2}')))) for i, n in enumerate(operadores) if i < 2] + [(n, (n1*n2, d1*d2) if n == '*' else (n1*d2, n2*d1)) for n in operadores if n == '*' or n == '/']

#     # soma_sub.extend(mult_div)

#     # operacoes_dict = {sim: op for sim, op in zip(operadores, soma_sub)}
    
#     # operacoes_dict = {sim: op for sim, op in zip(operadores, soma_sub + mult_div)}

#     # oper = soma_sub+mult_div
#     operacoes_dict = {sim: op for sim, op in oper}

#     for operacao in operacoes_dict.items():

#         if operador == operacao[0]:

#             den1, den2 = operacao[1] 

#             while den2 != 0:
#                 den1, den2 = den2, den1 % den2
                
#             print(f'{operacao[1][0]}/{operacao[1][1]} = {int(operacao[1][0]/den1)}/{int(operacao[1][1]/den1)}')
#             break


# solução 3 (simplificado) 948 Bytes (sem os comentários):

# n_de_expressoes = int(input())
# operadores = ['+', '-', '*', '/']

# for n in range(n_de_expressoes):

#     expressao = input()
#     elementos = expressao.split()

#     for char in elementos:
        
#         n1 = int(elementos[0])
#         n2 = int(elementos[4])

#         operador = elementos[3]

#         d1 = int(elementos[2])
#         d2 = int(elementos[6])

# # Nesta próxima linha foi usado do conceito de comprehensions em python para construir o dicionário:
# # Como o list comprehension resulta em uma lista e é possível concatenar listas usando o operador "+", ao invés de
# # criar duas listas (uma para operações de soma e subtração outra para as demais) é possível criar uma só (na mesma linha)
# # e concatená-las. Da mesma sorte, aplicando esse conceito com o dict-comprehension é possível usa essa nova lista como 
# # fonte para criação do dicionário.

#     operacoes_dict = {sim: op for sim, op in 
#                       [(n, (eval(f'{(n1*d2)}' f'{n}' f'{(n2*d1)}'), (int(f'{d1*d2}')))) for i, n in enumerate(operadores) if i < 2] 
#                       + [(n, (n1*n2, d1*d2) if n == '' else (n1*d2, n2*d1))for n in operadores if n == '' or n == '/']}

#     for operacao in operacoes_dict.items():

#         if operador == operacao[0]:
#             # é necessário aplicar a operação para que o MDC seja dos números transformados
#             # assim, a simplificação desejada acontecerá. Caso contrário o MDC será dos números
#             # Originais imputados, o que não faz sentido para a simplificação do números finais (após sofrerem a operação).

#             den1, den2 = operacao[1]
#             while den2 != 0:
#                 den1, den2 = den2, den1 % den2
  
#             print(f'{operacao[1][0]}/{operacao[1][1]} = {int(operacao[1][0]/den1)}/{int(operacao[1][1]/den1)}')
            
# solução 4 1,003  Bytes (sem os comentários):

# n_de_expressoes = int(input())
# operadores = ['+', '-', '*', '/']

# for n in range(n_de_expressoes):

#     expressao = input()
#     elementos = expressao.split()

#     for char in elementos:
        
#         n1 = int(elementos[0])
#         n2 = int(elementos[4])

#         operador = elementos[3]

#         d1 = int(elementos[2])
#         d2 = int(elementos[6])

# # Nesta próxima linha foi usado do conceito de comprehensions em python para construir o dicionário:
# # Como o list comprehension resulta em uma lista e é possível concatenar listas usando o operador "+", ao invés de
# # criar duas listas (uma para operações de soma e subtração outra para as demais) é possível criar uma só (na mesma linha)
# # e concatená-las. Da mesma sorte, aplicando esse conceito com o dict-comprehension é possível usa essa nova lista como 
# # fonte para criação do dicionário.

#     operacoes_dict = {sim: op for sim, op in [(n, (eval(f'{(n1*d2)}' f'{n}' f'{(n2*d1)}'), (int(f'{d1*d2}')))) if i < 2 
#                                               else (n, (n1*n2, d1*d2) if n == '*' else (n1*d2, n2*d1)) 
#                                               for i, n in enumerate(operadores)]}

#     for operacao in operacoes_dict.items():

#         if operador == operacao[0]:
#             # é necessário aplicar a operação para que o MDC seja dos números transformados
#             # assim, a simplificação desejada acontecerá. Caso contrário o MDC será dos números
#             # Originais imputados, o que não faz sentido para a simplificação do números finais (após sofrerem a operação).

#             den1, den2 = operacao[1]
#             while den2 != 0:
#                 den1, den2 = den2, den1 % den2
  
#             print(f'{operacao[1][0]}/{operacao[1][1]} = {int(operacao[1][0]/den1)}/{int(operacao[1][1]/den1)}')

# solução 5 899 Bytes (sem os comentários e espaços):

n_de_expressoes = int(input())
operadores = ['+', '-', '*', '/']

for n in range(n_de_expressoes):

    expressao = input()
    elementos = expressao.split()

    for char in elementos:
        
        n1 = int(elementos[0])
        n2 = int(elementos[4])

        operador = elementos[3]

        d1 = int(elementos[2])
        d2 = int(elementos[6])

# Nesta próxima linha foi usado do conceito de comprehensions em python para construir a lista:
# Como o list comprehension resulta em uma lista e é possível concatenar listas usando o operador "+", ao invés de
# criar duas listas (uma para operações de soma e subtração outra para as demais) é possível criar uma só (na mesma linha)
# e concatená-las. Da mesma sorte, aplicando esse conceito mais uma vez é possível usa essa nova lista como fonte.

    operacoes_list = [(sim, op) for sim, op in [(n, (eval(f'{(n1*d2)}' f'{n}' f'{(n2*d1)}'), (int(f'{d1*d2}')))) if i < 2 
                                              else (n, (n1*n2, d1*d2) if n == '*' else (n1*d2, n2*d1)) 
                                              for i, n in enumerate(operadores)]]

    for operacao in operacoes_list:

        if operador == operacao[0]:
            # é necessário aplicar a operação para que o MDC seja dos números transformados
            # assim, a simplificação desejada acontecerá. Caso contrário o MDC será dos números
            # Originais imputados, o que não faz sentido para a simplificação do números finais (após sofrerem a operação).

            den1, den2 = operacao[1]
            while den2 != 0:
                den1, den2 = den2, den1 % den2
  
            print(f'{operacao[1][0]}/{operacao[1][1]} = {int(operacao[1][0]/den1)}/{int(operacao[1][1]/den1)}')