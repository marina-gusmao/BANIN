#1066
cont = 0
p = 0
i = 0
po = 0
ne = 0
while cont < 5:
    n = int(input())
    cont += 1
    if n % 2 == 0:
            p += 1
    elif n % 2 != 0: 
            i += 1
    if n > 0:
            po += 1
    elif n < 0:
            ne += 1
     
print(f'{p} valor(es) par(es)\n{i} valor(es) impar(es)\n{po} valor(es) positivo(s)\n{ne} valor(es) negativo(s)')