funcao = int(input(f'Informe sua função na empresa: '))

if funcao > 5:
    print(f'Função inexistente!')
else:
    horas = float(input(f'Informe a horas trabalhadas: '))
    if funcao == 1:
        salario = (horas * 20)
        print(f'Seu salário será de R$ {salario:.2f}')
    elif funcao == 2:
        salario = (horas * 35)
        print(f'Seu salário será de R$ {salario:.2f}')
    elif funcao == 3:
        salario = (horas * 45)
        print(f'Seu salário será de R$ {salario:.2f}')
    elif funcao == 4:
        salario = (horas * 40)
        print(f'Seu salário será de R$ {salario:.2f}')
    elif funcao == 5:
        salario = (horas * 50)
        print(f'Seu salário será de R$ {salario:.2f}')


















