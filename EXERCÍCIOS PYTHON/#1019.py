#1019
s = int(input())
se = int(s % 60)
m = int(s % 3600 / 60)
h = int(s / 3600)
print(f'{h}:{m}:{se}')