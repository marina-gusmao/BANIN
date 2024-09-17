
# os seguintes exercícios não valem nota mas definitivamente
# preecisam ser feitos
# ok parece que é pra fazer e entregar do 6 ao 10, vambora

#ex 1

n = int(input("Insira um número inteiro "))
t = 0
while t < 10:
    t += 1
    print(f'{n} x {t} =', n*t)

#ex 2

m = int(input("Insira o menor valor do intervalo "))
M = int(input("Insira o maior valor do intervalo "))
r = 0
if m >= M:
    print("O intervalo fornecido é inadequado")
else:
    r = M % 5
    M -= r
while m <= M:
    print(M)
    M -= 5

#ex 3

m = int(input("Insira a quantidade de termos: "))
r = 0
maior = 0
while m != 0:
    menor = 0
    r = float(input(f"Insira um número real, utilizando '.' ao invés de ',' no caso de número decimal ")) 
    maior = r
    m -= 1 
    if maior > r:
        maior = maior
        r = menor
        m -= 1
    elif maior < r:
        menor = maior
        maior = r
        m -= 1
print(f"O maior número dentre os fornecidos é {maior} e o menor número dentre os fornecidos é {menor}")

   
