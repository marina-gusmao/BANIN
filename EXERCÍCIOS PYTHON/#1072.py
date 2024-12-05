#1072

N = int(input())
cont = 0
i = 0
o = 0
while cont < N:
    X = int(input())
    if X >= 10 and X <= 20:
        i += 1
    else:
        o += 1
    cont += 1
print(f'{i} in\n{o} out')