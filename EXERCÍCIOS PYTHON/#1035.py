#1035
E = input('')
L = E.split()
A = int(L[0])
B = int(L[1])
C = int(L[2])
D = int(L[3])
if A% 2 == 0 and C > 0 and D > 0 and B > C and D > A and (C + D) > (A + B):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')