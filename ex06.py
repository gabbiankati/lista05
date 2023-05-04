# 6) Desenvolva um programa que receba como entrada do usuário as medidas de três lados de
# um triângulo. O programa deverá retornar como saída qual o tipo do triângulo, de acordo com
# as regras:
# • Triângulo Equilátero possui os três lados com as mesmas medidas.
# • Triângulo Escaleno possui os três lados diferentes
# • Triângulo Isósceles possui dois lados iguais
# Deve-se ainda verificar se as medidas formam um triângulo. Três medidas formam um triângulo
# quando a soma de dois lados for maior do que um terceiro lado

num1 = float(input('Informe a primeira medida: '))
num2 = float(input('Informe a segunda medida: '))
num3 = float(input('Informe a terceira medida: '))

if num1 + num2 > num3 and num2 + num3 > num1 and num1 + num3 > num2:
    if num1 == num2 == num3:
        print("O triângulo é equilátero! ")
    elif num1 != num2 != num3:
        print("O triângulo é escaleno! ")
    else:
        print("O triângulo é isósceles! ")
else:
    print("As medidas não formam um triângulo... ")

