# 9) O departamento que controla o índice de poluição do meio ambiente mantém 3 grupos de
# indústrias que são altamente poluentes do meio ambiente. O índice de poluição aceitável varia
# de 0,05 até 0,25. Se o índice ficar entre 0,25 e 0,3 as indústrias do 1º grupo são intimadas a
# suspenderem suas atividades, se ficar entre 0,31 e 0,4 as do 1º e 2º grupo são intimadas a
# suspenderem suas atividades e se o índice for maior que 0,41 os três grupos devem ser
# notificados a paralisarem suas atividades. Escrever um algoritmo que lê o índice de poluição
# medido e emite a notificação adequada aos diferentes grupos de empresas.

poluicao = float(input(f'Informe o índice de poluição: '))

if 0.05 <= poluicao <= 0.25:
    print(f'O índice de poluição está aceitavel.')
elif 0.25 <= poluicao <= 0.3:
    print(f'A empresa do primeiro grupo deverá suspender suas atividades...')
elif 0.31 <= poluicao <= 0.4:
    print(f'As empresas do primeiro e do segundo grupo deverão suspender suas atividades...')
else:
    print(f'As três empresas deverão suspender suas atividades!')


