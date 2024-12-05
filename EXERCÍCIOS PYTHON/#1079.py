#1079

N = int(input())
cont = 0
L = []
while cont < N:
    X = input()
    S = X.split()
    m = (float(S[0]) * 2 + float(S[1]) * 3 + float(S[2]) * 5) / 10
    L.append(m)
    cont += 1
for i in L:
    print(f'{(i):.1f}')