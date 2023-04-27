# 5) Desenvolva um programa que receba três valores inteiros, e determine se o menor valor é
# par.

a = int(input('Informe o primeiro valor: '))
b = int(input('Informe o primeiro valor: '))
c = int(input('Informe o primeiro valor: '))

if a < b and a < c:
    print(f'O menor valor é {a}')
    if a % 2 == 0:
        print('Ele é par!')
    else:
        print('Ele é impar!')
elif b < a and b < c:
    print(f'O menor valor é {b}')
    if b % 2 == 0:
        print('Ele é par!')
    else:
        print('Ele é impar!')
else:
    print(f'O menor valor é {c}')
    if c % 2 == 0:
        print('Ele é par!')
    else:
        print('Ele é impar!')




