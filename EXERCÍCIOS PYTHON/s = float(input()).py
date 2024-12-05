s = float(input())
P = 0 #imposto

if s >= 0 and s <= 2000:
    print('Isento')
if s > 2000 and s <= 3000:
    P = (s - 2000) * 8 / 100
elif s <= 4500:
    P = ((s - 3000) * 18 / 100) + 1000 * 8 / 100
else:
    P = ((s - 4500) * 28 / 100) + 1500 * 18 / 100 + 1000 * 8 / 100
    print(f'R$ {P:.2f}')