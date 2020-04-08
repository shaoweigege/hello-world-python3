#!/usr/bin/env python3.8

'''
Leia o valor e desconte 5%.
'''

#adicionando minha pasta de módulos
import sys
sys.path.append('/home/danielle8farias/exercicios-python-3/meus_modulos')
#importando parte do código
from mensagem import cabecalho, rodape

#função que calcula o desconto de 5%
def desconto(preco):
    desconto = preco - (preco*0.05)
    return desconto

#programa principal
cabecalho('DESCONTO 5%')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    preco = float(input('Digite o preço: R$'))
    valor_desconto = desconto(preco)
    #:.2f limita o número de duas casas decimais
    print(f'O novo preço com desconto de 5% é R${valor_desconto:.2f}')
    print()
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #upper: joga a string para maiúsculo
        #strip: remove os espaços no começo e no fim
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        #quebrando o 1º laço
        break
rodape()
