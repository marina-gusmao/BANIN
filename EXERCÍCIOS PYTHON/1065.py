#1065

cont = 0
p = 0
while cont < 5:
    n = int(input('digite um valor inteiro: '))
    cont += 1
    if n % 2 == 0:
            p += 1
print(f'{p} valores pares')