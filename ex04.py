# 4) Desenvolver um programa que receba como entrada três números. Determinar qual entre
# estes três números é o maior.

x = int(input('Primeiro número: '))
x1 = int(input('Segundo número: '))
x2 = int(input('Terceiro numero: '))

if x > x1 and x > x2:
    print(f'Entre os três números {x} é o maior')
elif x1 > x and x1 > x2:
    print(f'Entre os três números {x1} é o maior')
else:
    print(f'Entre os três números {x2} é o maior')


