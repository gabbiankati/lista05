# 1) Construa um programa que receba dois números do usuário, e retorne como saída a diferença
# entre o maior e o menor.

x = int(input('Informe um número: '))
y = int(input('Informe outro número: '))

if x > y:
    resultado = x - y
else:
    resultado = y - x

print(f'A diferença dos números é de: {resultado}!')






