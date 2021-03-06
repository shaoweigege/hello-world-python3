'''
Usuário lê nomes e duas notas de vários alunos. O programa guarda os dados numa lista composta. 
Retorna o boletim com, o nome, o número e a média de cada aluno. Ao final é permitido escolher 
o aluno pelo número para ver as notas individualmente.
'''

boletim = list()

while True:
    estudante = list()
    notas = list()

    nome = input('Nome da(o) aluna(o): ')
    nota1 = float(input('1ª nota: '))
    nota2 = float(input('2ª nota: '))
    print()

    notas.append(nota1)
    notas.append(nota2)

    media = (nota1 + nota2)/2

    estudante.append(nome)
    estudante.append(notas[:])
    estudante.append(media)

    boletim.append(estudante[:])

    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resp == 'N':
        break
    print()
print()

print(f'{"No.":<4}{"NOME":>5}{"MÉDIA":>15}')
print('-'*30)

for i in range(len(boletim)):
    #número do auno
    print(f'{i:<4}', end='')
    #nome do aluno
    print(f'{boletim[i][0]:<10}', end='')
    #média do aluno
    print(f'{boletim[i][2]:>9.1f}')

while True:
    print('\n99 interrompe')
    num = int(input('Digite o número do aluno para ver as notas desse: '))

    if num == 99:
        print('Finalizando...\n')
        break
    #aceita apenas opções que são itens da lista
    #len()-1 porque o índice da lista começa em zero
    if num <= len(boletim)-1:
        print(f'\nNotas de {boletim[num][0]} são: {boletim[num][1]}')
