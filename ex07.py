# 7) Uma faculdade classifica as notas dos alunos conforme a faixa de média que tenha atingido
# de acordo com a seguinte tabela:
# Média                   Classificação
# 9,0 a 10                Superior
# 7,0 a 8,9               Médio Superior
# 5, 0 a 6,9              Médio
# 3,0 a 4,9               Médio Inferior
# 0,1 a 2,9               Inferior
# 0                       Sem Rendimento
#
# Faça um algoritmo que lê a nota de um aluno e informa a sua classificação

nota = float(input(f'Informe sua média final: '))

if nota > 0:
    if nota >= 0.1 and nota < 2.9:
        print(f'Classificação: inferior')
    elif nota >= 3 and nota < 4.9:
        print(f'Classificação: médio inferior')
    elif nota >= 5 and nota < 6.9:
        print(f'Classificação: médio')
    elif nota >= 7 and nota < 8.9:
        print(f'Classificação: médio superior')
    else:
        print(f'Classificação: superior')
else:
    print(f'Cla')