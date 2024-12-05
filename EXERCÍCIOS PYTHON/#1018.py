#1018
v = int(input())
valor = v
cem = int(v / 100)
v = v % 100
cinquenta = int(v / 50)
v = v % 50
vinte = int(v / 20)
v = v % 20
dez = int(v / 10)
v = v % 10
cinco = int(v / 5)
v = v % 5
dois = int(v / 2)
v = v % 2
um = int(v / 1)
print(f'{valor}\n{cem} nota(s) de R$ 100,00\n{cinquenta} nota(s) de R$ 50,00\n{vinte} nota(s) de R$ 20,00\n{dez} nota(s) de R$ 10,00\n{cinco} nota(s) de R$ 5,00\n{dois} nota(s) de R$ 2,00\n{um} nota(s) de R$ 1,00')