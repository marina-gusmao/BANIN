# revisão banin

#LISTA
# X = [] cria uma lista
# X.append(1) adiciona na última posição o elemento '1'
# X.clear() limpa a lista, ou seja, exclui todos os seus elementos
# Y = X.copy() cria uma nova lista Y, cópia da lista X
# X.count(1) conta quantas são as ocorrências do elemento '1' na lista X
# Z = X.count(1) cria a variável Z e atribui ao seu valor o númro de ocorrências
# que o elemento '1' tem na lista X
# X.extend(Y) acrescenta ao final da lista X os elementos da lista Y
# X.index(1) mostra qual a posição ocupada pelo elemento '1' na lista X
# 2 in X retorna ao valor True ou False, indicando se o elemento '2' está(True)
# ou não está(False) na lista X
# X.index(1,1) retorna qual a posição ocupada pelo elemento '1' na lista X,
# a partir da posição 1 (quando a posição não é indicada, ele retorna a
# posição da PRIMEIRA ocorrência do elemento '1' a partir da posição 0)
# X.insert(2,1) insere o elemento '1' na lista na posição 2
# len(X) retorna a quantidade de elementos presentes na lista X
# A = X.pop(0) retira (ou seja, ele não mais fará parte) o elemento de posição 0
# da lista X e atribui esse elemento como valor da variável A
# B = X.pop() retira o último elemento da lista X, artibuindo-o como valor
# da variável B (essa variável é criada com o comando, não precisa criar antes)
# X.remove(1) remove a primeira ocorrência do elemento de valor 1 ('1') da lista X
# del X[1] remove o elemento de posição 1 da lista X
# X.reverse() inverte a ordem dos valores da lista (o último se torna o primeira,
# o penúltimo se torna o segundo e por aí vai)
# X.sort() ordena os elementos da lista X segundo seu valor
# X.sort(reverse=True) ordena os elementos da lista X segundo seus valores,
# em ordem decrescente

#FOR
# for valor in X: para cada valor na lista X ele executa algo dentro do laço
# for valor in X:
#    print(valor)
# irá mostrar, um por linha, cada um dos elementos da lista segundo sua ordem4
# de aparição

#RANGE
# produz sequências numéricas a partir de 1, 2 ou 3 parâmetros
# para ver o range, é preciso convertê-lo em lista
# list(range(5,10)) produz uma lista que vai, progressivamente, do primeiro 
# termo ao último antes do valor especificado - [5, 6, 7, 8, 9]
# utilizando dois termos (5,10) para range, o primeiro termo é o start 
# e o último é o stop. Ao fornecer apenas um valor, ele entende que o valor fornecido é
# o stop, começando em 0. Ao fornecer três valores, o primeiro refere-se ao start,
# o segundo é o stop e o terceiro é o passo.
# Por exemplo: list(range(5,10,3)) retorna a lista [5, 8]

# MATCH CASE
# Comando condicional múltiplo. Ele enquadra o objeto dentro dos case com
# as diversas possibilidades. O 'case _:' é opcional e serve para colocar o objeto
# em opções não previstas. Esse 'case _:' deve ser o último das cláusulas case.

#INLINE IF
# O comando if inline funciona apenas quando as condições são simples. O else
# é obrigatório. Você escreve primeiro a condição verdadeira e depois a falsa.
# print(X) if X >= Y else print(Y). Para usar o if inline sem o else, basta
# cumprir seu requisito de sintaxe adicionando ao fin do comando um 'else 0' 
# 

#EXERCÍCIOS
#Escreva um programa que leia três números inteiros: o primeiro termo P, a razão R
#e a quantidade Q de termos de uma progressão aritmétia. O programa deve 
#calcular os Q termos da progressão, colocando-os em uma lista e, no final,
#exibindo-a na tela

P = int(input('Digite o primeiro termo P: '))
R = int(input('Digite a razão R: '))
Q = int(input('Digite a quantidade de termos Q: '))
a = 0
Termos = []
while a < Q:
    Termos.append(P)
    P = P + R
    a += 1
print(Termos)

#EXERCÍCIOS
#Escreva um programa que leia três números inteiros: o primeiro termo P, a razão R
#e a quantidade Q de termos de uma progressão aritmétia. O programa deve 
#calcular os Q termos da progressão, colocando-os em uma lista e, no final,
#exibindo-a na tela - agora usando range

P = int(input('Digite o primeiro termo P: '))
R = int(input('Digite a razão R: '))
Q = int(input('Digite a quantidade de termos Q: '))
últimotermo = P + R * (Q - 1)
Termos = list(range(P, últimotermo + 1, R))
print(Termos)

#EXERCÍCIOS
# Escreva um programa que leia um número inteiro N.
# Em seguida, leia N números reais, carregando-os em uma lista. Ao final,
# exiba os elementos da lista na tela, sendo um em cada linha.

N = int(input('Digite a quantidade: '))
L = []
for i in range(N):
    x = float(input(f'elemento {i}: '))
    L.append(x)
print('\nResultado')
for valor in L:
    print(f' {valor:.2f}')

#EXERCÍCIOS
# Escreva um programa que leia um número inteiro N.
# Em seguida, leia N números inteiros, carregando-os em duas listas: uma para
# positivos e outra para negativos. Ao final,
# exiba na tela cada lista juntamente com o seu tamanho. (o valor 0 deve ser positivo)

N = int(input('Digite a quantidade: '))
Ln = []
Lp = []
for i in range(N):
    x = int(input(f' elemento {i} >> '))
    if x >= 0:
        Lp.append(x)
    else:
        Ln.append(x)
print(f'\nLista de positivos:{Lp}, contém {len(Lp)} elementos')
print(f'\nLista de negativos:{Ln}, contém {len(Ln)} elementos')

#EXERCÍCIO
# Escreva um programa que permaneça em laço lendo números inteiros. O laço
# termina quando for digitado 0. Cada valor diferente de zero deve ser colocado
# em uma lista. Ao final, exiba a lista e a quantidade de elementos.

L = []
valor = int(input('Digite um inteiro: '))
while valor != 0:
    L.append(valor)
    valor = int(input('Digite um inteiro: '))
print('\nResultado:')
print(L)
print(f'A lista contém {len(L)} elementos')

#EXERCÍCIO
# Escreva um programa que permaneça em laço lendo números inteiros. O laço
# termina quando for digitado zero. Cada valor  diferente de zero deve ser colocado
# em uma lista, desde que ele já não esteja lá. Ao final, exiba a lista e a quantidade de elementos.
# Se um valor repetido for digitado, o programa deve exibir uma mensagem na tela.

L = []
valor = int(input('Digite um inteiro: '))
while valor != 0:
    if valor not in L:
        L.append(valor)
    else:
        print('o valor já foi digitado')
    valor = int(input('Digite um inteiro: '))
print('\nResultado:')
print(L)
print(f'A lista contém {len(L)} elementos')

#EXERCÍCIO
# Escreva um programa que leia um número inteiro Qtde e carregue uma lista com
# essa quantidade de números inteiros aleatórios. Exiba a lista na tela. Em
# seguida, inicie um laço que deve permanecer em execução enquanto um valor inteiro
# X for maior que 0. Para cada valor de X, verifique se ele está ou não na
# lista gerada. Caso esteja é preciso exibir a quantidade de ocorrências

from random import randint
L = []
Qtde = int(input('Digite um inteiro: '))
for i in range(Qtde):
    L.append(randint(1, 20))
print('Lista gerada')
print(L)

X = 1
while X > 0:
    X = int(input('Digite X '))
    if X in L:
        print(f' há {L.count(X)} ocorrência(s) de {X} na lista')
    else:
        print(f' {X} não está na lista')

