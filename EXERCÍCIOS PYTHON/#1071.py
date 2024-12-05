#fiz de um jeito bem estúpido, era mais fácil ter usado o range e criado uma lista.
#1071
X = int(input())
Y = int(input())
s = 0
if X > Y:
    X -= 1
    while X > Y:
        if X % 2 != 0:
             s += X
        X -= 1
elif Y > X:
    Y -= 1
    while Y > X:
        if Y % 2 != 0:
            s += Y
print(s)