import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado: \n")

    wal = 4.51 
    ttr = 0.693
    hlr = 0.55
    sal = 70.82
    sac = 1.82
    pal = 38.5

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    pass

def constroi_frases(sentencas):
    ''' Essa funcao retorna uma lista de frases.'''
    
    lista_frases = []

    for sentenca in sentencas:
        frase = separa_frases(sentenca)
        lista_frases.extend(frase)

    return lista_frases

def constroi_palavras(frases):
    ''' Essa função retorna uma lista de palavras'''

    lista_palavras = []

    for frase in frases:
        palavra = separa_palavras(frase)
        lista_palavras.extend(palavra)

    return lista_palavras

def soma_palavras(palavras):
    ''' Essa função retorna a soma de todas as palavras'''
    soma = 0

    for palavra in palavras:
        soma += len(palavra)

    return soma

def soma_caracter(palavras):
    ''' Essa função retorna a soma de caracter '''
    soma = 0

    for palavra in palavras:
        for letra in palavra:
            soma += 1

    return soma

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    
    sentencas = separa_sentencas(texto)
    frases = constroi_frases(sentencas)
    palavras = constroi_palavras(frases)
    
    wal = soma_palavras(palavras) / len(palavras)                            
    ttr = n_palavras_diferentes(palavras) / len(palavras)
    hlr = n_palavras_unicas(palavras) / len(palavras)
    sal = soma_caracter(palavras) / len(sentencas)
    sac = len(frases) / len(sentencas)
    pal = soma_caracter(palavras) / len(frases)
                                       
    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass


def constroi_assinaturas(textos):
    ''' Essa função retorna a assinatura de todos os textos.'''
    
    assinaturas = []
    
    for texto in textos:
        assinaturas.append(calcula_assinatura(texto)) 

    return assinaturas

def main():
    
    le_assinatura()
    textos = le_textos()
    assinaturas = constroi_assinaturas(textos)


if __name__ == "__main__":
    main()
