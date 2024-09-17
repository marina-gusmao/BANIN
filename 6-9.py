N = int(input("Digite o número de termos na PG: "))
P = int(input("Digite o primeiro termo: "))
R = int(input("Digite a razão: "))
Cont = 0
while Cont < N:
    print(P)
    P = P * R
    Cont = Cont + 1

# exercício 2

P = 0
N = 0
while True:
    n = int(input("Digite um valor inteiro: "))
    if n > 0:
        P = P + n
    elif n < 0:
        N = N + n
    else:
        break
    
print("A soma dos números positivos é:", P, "e a soma dos números negativos é:", N)

#ex 3

I = int(input("Digite a quatia de números para somar: "))
S = 0.0
Cont = 0
while Cont < I:
    R = float(input(f"Digite um número real {cont + 1}: "))
    S += R
    Cont += 1
print("A soma dos números é ", {S})