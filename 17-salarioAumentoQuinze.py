'''
Leia o salário e o aumente em 15%.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('SALÁRIO AUMENTO 15%')

while True:
    salario = float(input('Escreva o salário: R$'))
    novo_salario = salario + salario*0.15
    print('O novo salário com aumento de 15% é {:.2f}'.format(novo_salario))
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()

rodape()
