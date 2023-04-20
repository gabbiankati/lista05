# 2) Desenvolva um programa que leia um número inteiro. Se o número informado for positivo,
# imprimir sua raiz quadrada; se for negativo, o quadrado do número

num = int(input('Informe um número: '))

if num >= 0:
    resultado = num ** 0.5
else:
    resultado = num ** 2

print(f'O resultado é {resultado}')
