# ex 5
X = int(input("Digite o valor de X: "))
if X > 0:
    print("O número é positivo")
elif X == 0:
    print("O número fornecido é 0")
else:
    print("O número é negativo")

# ex 6

N = input("Informe o nome do lutador: ")
P = float(input("Informe o peso em kg do lutador: "))
C = ""
if P < 65:
    C = "Pena"
elif 65 <= P < 72:
    C = "Leve"
elif 72 <= P < 79:
    C = "Ligeiro"
elif 79 <= P < 86:
    C = "Meio médio"
elif 86 <= P < 93:
    C = "Médio"
elif 93 <= P < 100:
    C = "Meio pesado"
elif 100 <= P:
    C = "Pesado"
print("O lutador", N, "pesa", P, "e se enquadra na categoria", C)

# ex 7

A = float(input("Valor de A: "))
B = float(input("Valor de B: "))
C = float(input("Valor de C: "))
DELTA = B ** 2 - 4 * A * C
if DELTA > 0:
    X1 = (- B + DELTA ** 0.5) / (2 * A)
    X2 = (- B - DELTA ** 0.5) / (2 * A)
    print("As raízes são", X1, "e também", X2)
elif DELTA == 0:
    X = ( - B - DELTA ** 0.5) / (2 * A)
    print("A raiz é:", X)
else:
    print("Não há raízes reais da equação")

# ex 8 - ESSE AQUI TÁ ERRADO E EU NÃO SEI ARRUMAR KKKKKKKKKKKK
G = float(input("Valor de G: "))
H = float(input("Valor de H: "))
I = float(input("Valor de I: "))
if G > 0 and G == H == I:
    print("Os números fornecidos podem constituir os lados de um triângulo equilátero")
elif G + H > I or G + I > H or I + H > G:
    print("Os números fornecidos podem constituir os lados de um triângulo escaleno")
elif G + H > I or G + I > H or I + H > G and G == H or G == I or I == H:
    print("Os números fornecidos podem constituir os lados de um triângulo isósceles")
else:
    print("Os números fornecidos não constituem um triângulo")

