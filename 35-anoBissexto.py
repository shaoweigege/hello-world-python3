'''
Leia um ano qualquer e verifique se é bissexto.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('ANO BISSEXTO')

while True:
    ano = int(input('Informe o ano: '))
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print('O ano {} é bissexto.'.format(ano))
    else:
        print('O ano {} NÃO é bissexto.'.format(ano))
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()

rodape()
