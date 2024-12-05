#1080

cont = 0
l = []
while cont < 100:
    x = int(input())
    l.append(x)
    cont += 1
print(f'{max(l)}')
print(l.index(max(l)) + 1)