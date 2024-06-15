from matrizes import cria_matriz_aleat, imprime_matriz 

# Tupla é uma "lista" imutavel.

def dimensao(matriz):
    '''
        Retorna uma tupla com as dimensões da matriz.
    '''
    qt_c    = 0
    qt_l    = 0

    for lin in matriz:
        qt_l += 1
        qt_c = len(lin)

    return (qt_l, qt_c)

def eh_multiplicavel(matriz_1, matriz_2):
    '''
        Verifica se duas matrizes podem ser multiplicadas, 
        Retorna verdadeiro se for possivel e falso caso contrário
    '''
    
    d_matriz_1 = dimensao(matriz_1)
    d_matriz_2 = dimensao(matriz_2)

    if d_matriz_1[1] == d_matriz_2[0]:
       return True
    else:
        return False


if __name__ == "__main__":
    m1 = cria_matriz_aleat(5, 2)
    m2 = cria_matriz_aleat(3, 3)
    
    eh_multiplicavel(m1, m2):

