from matrizes import cria_matriz_aleat, imprime_matriz 
from dimensoes_matriz import dimensao
import random

def soma_matrizes(m1, m2):
    '''
        Realiza a soma de duas matrizes se tiver a mesma dimensão, 
        e retorna seu valor. Caso o contrário retorna Falso e uma 
        mensagem de erro.
    '''
    d_m1 = dimensao(m1)
    d_m2 = dimensao(m2)

    somada = []

    # Compara as dimensões das matrizes.
    if d_m1 == d_m2:
        for i in range(len(m1)):
            linha = []

            # A cada linha da matriz percorrida é somado os valores
            for j in range(len(m1[i])):
                linha.append(m1[i][j] + m2[i][j])
            
            # Adiciona as somas dos valores na matriz somada.
            somada.append(linha)
    else:
        print("Erro: Matriz com dimensões diferentes!")
        return False

    print("Soma realizada com sucesso! ") 
    return somada

if __name__ == "__main__":
        #Cria duas matrizes com dimensões "aleatorias".
    m1 = cria_matriz_aleat(random.randint(1, 42), random.randint(1, 42))
    m2 = cria_matriz_aleat(random.randint(1, 42), random.randint(1, 42))
        
    soma_matrizes(m1, m2) 
