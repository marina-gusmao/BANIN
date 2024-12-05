#1060               
cont = 0
p = 0
n = 0
while cont < 6:
    n = int(input('digite um valor inteiro: '))
    if n == 0:
        cont = cont
    elif n > 0:
            p += 1
            cont += 1
    else: 
            cont += 1
print(f'{p} valores positivos')
