#Eu, porém o site não aceitou essa versão
p1, a, b = [int(input()), int(input()), float(input())]
p2, c, d = [int(input()), int(input()), float(input())]

e = a * b  + c * d
print(f'VALOR A PAGAR R$ = {e:.2f}')

#1

codigo1, quantidade1, valor_unitario1 = map(float, input().split())
codigo2, quantidade2, valor_unitario2 = map(float, input().split())

total = (quantidade1 * valor_unitario1) + (quantidade2 * valor_unitario2)

print(f"VALOR A PAGAR: R$ {total:.2f}")

#2
# Read the inputs for product 1
cod_product_1, product_1_qty, product_1_price = input().split(" ")
cod_product_1 = int(cod_product_1)
product_1_qty = int(product_1_qty)
product_1_price = float(product_1_price)

# Read the inputs for product 2
cod_product_2, product_2_qty, product_2_price = input().split(" ")
cod_product_2 = int(cod_product_2)
product_2_qty = int(product_2_qty)
product_2_price = float(product_2_price)

# Calculate the total amount to pay
summ_1 = product_1_qty * product_1_price
summ_2 = product_2_qty * product_2_price
valor_a_pagar = summ_1 + summ_2

# Print the result
print(f'VALOR A PAGAR: R$ {valor_a_pagar:.2f}')

