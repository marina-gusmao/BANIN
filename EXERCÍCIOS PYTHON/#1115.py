#1115
while True:
    E = [int(i) for i in input().split()]
    X, Y = E
    if X == 0 or Y == 0:
        break
    elif X > 0 and Y > 0:
        print('primeiro')
    elif X < 0 and Y > 0:
        print('segundo')
    elif X < 0 and Y < 0:
        print('terceiro')
    else:
        print('quarto')
