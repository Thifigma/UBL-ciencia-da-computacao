# Definição de matriz: matriz = [[], [], ... , []]
# Listas de Listas. 

import random

def cria_matriz_aleat(num_lin, num_col):
    ''' 
        Cria e retorna uma matriz com número de linhas e número de colunas
        definidas pelo usuário e de preenchimento "aleatório".
    '''
    matriz = [] #Inicialmente temos uma lista vazia.
    for i in range(num_lin):
        linha = [] # A cada laço se tem uma nova lista vazia.
        for j in range(num_col):
            linha.append(random.randint(1, 42))
        
        # Adiciona a nova linha à matriz.
        matriz.append(linha)

    return matriz

def cria_matriz(num_lin, num_col):
    ''' 
        Cria e retorna uma matriz com número de linhas e número de colunas
        definidas pelo usuário e solicita o preenchimento dos valores.
    '''
    matriz = [] #Inicialmente temos uma lista vazia.
    for i in range(num_lin):
        linha = [] # A cada laço se tem uma nova lista vazia.
        for j in range(num_col):
            linha.append(int(input()))
        
        # Adiciona a nova linha à matriz.
        matriz.append(linha)

    return matriz

def imprime_matriz(matriz):
    '''
        Imprime uma matriz formatada. 
    '''
    for row in matriz: # Metodo join concatena os elementos da linha.
        print(" ".join(f"{x}" for x in row)) 
        # f{n} transforma o número inteiro N em uma string

def le_matriz():
    '''
        Solicita as dimensões, realiza o preenchimeinto manual dos valores e 
        retorna a matriz.
    '''
    lin = int(input("Lin: "))
    col = int(input("Col: "))
    return cria_matriz(lin, col)

if __name__ == "__main__":
    imprime_matriz(le_matriz())
