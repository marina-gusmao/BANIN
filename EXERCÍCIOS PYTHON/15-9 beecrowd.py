#ex 1 
f = float(input())
i = 'Intervalo '
if f >= 0 and f <= 25:
    print(f'{i}[0,25]')
elif f > 25 and f <= 50:
    print(f'{i}(25,50]')
elif f > 50 and f <= 75:
    print(f'{i}(50,75]')
elif f > 75 and f <= 100:
    print(f'{i}(75,100]')
else:
    print('Fora de intervalo')

#ex 2
s = float(input())
n = 'Novo salario: '
r = 'Reajuste ganho: '
p = 'Em percentual: '
P = 0

if s >= 0 and s <= 400:
    P = 15
elif s > 400 and s <= 800:
    P = 12
elif s > 800 and s <= 1200:
    P = 10
elif s > 1200 and s <= 2000:
    P = 7
else:
    P = 4
N = s * (100 + P) / 100
R = N - s

print(f'{n}{N:.2f}\n{r}{R:.2f}\n{p}{P} %')

#ex 3

f = int(input())
if f == 61:
    print('Brasilia')
elif f == 71:
    print('Salvador')
elif f == 11:
    print('Sao Paulo')
elif f == 21:
    print('Rio de Janeiro')
elif f == 32:
    print('Juiz de Fora')
elif f == 19:
    print('Campinas')
elif f == 27:
    print('Vitoria')
elif f == 31:
    print('Belo Horizonte')
else:
    print('DDD nao cadastrado')

#ex 4
s = float(input())
P = 0 #imposto

if s >= 0 and s <= 2000:
    print('Isento')
elif s > 2000 and s <= 3000:
    P = (s - 2000) * 8 / 100
    print(f'R$ {P:.2f}')
elif s > 3000 and s <= 4500:
    P = ((s - 3000) * 18 / 100) + 1000 * 8 / 100
    print(f'R$ {P:.2f}')
else:
    P = ((s - 4500) * 28 / 100) + 1500 * 18 / 100 + 1000 * 8 / 100
    print(f'R$ {P:.2f}')

#ex 5
m = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
i = int(input())
i -= 1
print(m[i])