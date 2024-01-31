def mostraInverso(lista):
    i = (len(lista) - 1)
    
    while (i >= 0):
        print(lista[i])
        i = i - 1

def main():
    lista = []
    indice = 0
    num = int(input("Digite um número: "))

    while (num != 0):
        lista.append(num)
        indice = indice + 1
        num = int(input("Digite um número: "))
    
    mostraInverso(lista)


main()
