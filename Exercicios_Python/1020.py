days = int(input())

ano = days // 365
meses = (days % 365) // 30
days = ((days % 365) % 30)

print(f'{ano} ano(s)')
print(f'{meses} mes(es)')
print(f'{days} dia(s)')