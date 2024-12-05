#1117
cont = 0
m = 0
while cont != 2:
    n = float(input())
    if n < 0 or n > 10:
        print('nota invalida')
    else:
        cont += 1
        m += n / 2
print(f'media = {m}')