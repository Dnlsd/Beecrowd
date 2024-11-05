seconds = int(input())
hour = 0
minutes = 0


hour = seconds // 3600 # toma a quandidade de horas

seconds %= 3600 #atualiza os segundos


minutes = seconds // 60 # toma a quandidade de minutos

seconds %= 60 #atualiza os segundos

print(f'{hour}:{minutes}:{seconds}')