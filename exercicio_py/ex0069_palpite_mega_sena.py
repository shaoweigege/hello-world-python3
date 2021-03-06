'''
Usuário escolhe quantas apostas deseja fazer no jogo da mega-sena. 
Programa retorna as sugestões de apostas; 6 números de 1 a 60. 
Não pode haver números repetidos.
'''

from random import randint
from time import sleep

jogo = int(input('Quantos jogos deseja fazer? '))
print()

i = 1
while i <= jogo:
    palpite = list()

    for n in range(6):
        num = randint(1, 60)
        
        while num in palpite:
            num = randint(1, 60)
        
        palpite.append(num)          
    
    print(f'{i}º jogo: {palpite}')
    sleep(0.5)
    i += 1
print()
