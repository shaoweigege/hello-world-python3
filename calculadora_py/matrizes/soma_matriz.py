import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho

from matrizes.ordem_matriz import linha_coluna
from matrizes.construcao_matriz import construir_matriz
from matrizes.impressao_matriz import imprimir_matriz

from time import sleep


#efetuando a soma das matrizes
def efetuar_soma_matrizes (A, B):
    num_linhas = len(A)
    num_colunas = len(A[0]) #basta colocar o comprimento de uma das linhas de A
    soma = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor_soma = (A[i][j] + B[i][j])
            linha.append(valor_soma)
        soma.append(linha)
    return soma


#chamada principal da soma de matrizes
def somar_matrizes():
    ler_cabecalho('soma duas matrizes')
    #definindo a ordem das matrizes 
    print('Matriz A')
    Ai, Aj = linha_coluna()
    print()
    print('Matriz B')
    Bi, Bj = linha_coluna()
    print()
    #verificando se são de mesma ordem
    if Ai == Bi and Aj == Bj:
        #construindo as matrizes
        print('Construindo matriz A')
        A = construir_matriz(Ai, Aj)
        print('\nConstruindo matriz B')
        B = construir_matriz(Bi, Bj)
        print()
        #imprimindo as matrizes
        sleep(0.5)
        print('Matriz A:')
        imprimir_matriz(A, Ai, Aj)
        print()
        sleep(0.5)
        print('Matriz B:')
        imprimir_matriz(B, Bi, Bj)
        print()
        resultado = efetuar_soma_matrizes(A, B)
        #imprimindo a soma
        sleep(0.5)
        print('\nResultado da soma:')
        imprimir_matriz(resultado, Ai, Aj)
    else:
        print('Não é possível somar: As matrizes devem ser de mesma ordem.')
        sleep(0.5)
    print()
