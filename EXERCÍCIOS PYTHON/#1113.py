#1113
while True:
    E = [int(i) for i in input().split()]
    P, S = E
    if P == S:
        break
    elif P > S:
        print('Decrescente')
    else:
        print('Crescente')