import re

'''A funcao le os valores dos tracos linguisticos do modelo e devolve uma
assinatura a ser comparada com os textos fornecidos'''
def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = 4.51
    ttr = 0.693
    hlr = 0.55
    sal = 70.82
    sac = 1.82
    pal = 38.5

    return [wal, ttr, hlr, sal, sac, pal]

    '''A funcao le todos os textos a serem comparados e devolve uma lista 
        contendo cada texto como um elemento'''
def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)

    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
def separa_palavras(frase):
    return frase.split()

    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras
        que aparecem uma unica vez'''
def n_palavras_unicas(lista_palavras):
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

    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
def n_palavras_diferentes(lista_palavras):
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

    '''Essa funcao recebe duas assinaturas de texto e deve devolver 
        o grau de similaridade nas assinaturas.'''
def compara_assinatura(as_a, as_b):
    
    Sab = 0;
    i = 0
    while (i < 6):
        Sab = Sab + abs(as_a[i] + as_b[i]);
        i = i + 1;

    return (Sab / 6) 

def somaCaracter(totalCaracter):
    
    soma = 0
    for i in range(totalCaracter + 1):
        soma = soma + i

    return soma

    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
def calcula_assinatura(texto):
    
    listaSentencas = separa_sentencas(texto)
    listaFrases = []
    listaPalavras = []
    totalCaracter = 0
    totalCaracterFrases = 0

    for sentenca in listaSentencas:
        listaFrases.append(separa_frases(sentenca))

    for i in range(len(listaFrases)):
        listaPalavras.extend(separa_palavras(*listaFrases[i]))

    for palavra in listaPalavras:
        totalCaracter = totalCaracter + len(palavra)
    
    for frase in listaFrases:
        totalCaracterFrases = totalCaracterFrases + len(frase)

    wal = (totalCaracter / len(listaPalavras))
    ttr = (n_palavras_diferentes(listaPalavras) / totalCaracter)
    hlr = (n_palavras_unicas(listaPalavras) / totalCaracter)
    sal = (somaCaracter(totalCaracter) / len(listaSentencas))
    sac = (len(listaFrases) / len(listaSentencas))
    pal = (somaCaracter(totalCaracterFrases) / len(listaFrases))
    
    return [wal, ttr, hlr, sal, sac, pal]
    
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp 
        e deve devolver o numero (1 a n) do texto com maior probabilidade de 
        ter sido infectado por COH-PIAH.'''
def avalia_textos(textos, ass_cp):
    ''' Quanto menor o valor mais similar é. 
        Além disso estou usando a técnica de chutar para depois corrigir. 
    '''
    grau_de_similaridade = 200;
    indice = 0; ''' Indice com o maior grau de similaridade. '''
    i = 0;

    
    while (i < len(textos)):
        if (grau_de_similaridade < compara_assinatura(calcula_assinatura(textos[i]), ass_cp)):
            grau_de_similaridade = compara_assinatura(calcula_assinatura(textos[i]), ass_cp)
            indice = i;

        i = i + 1;

    return indice;


def main():

    as_Padrao = le_assinatura()
    textos = le_textos()
    
    print(avalia_textos(textos, as_Padrao))

main()
