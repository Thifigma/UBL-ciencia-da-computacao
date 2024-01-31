def remove_repetidos(lista):
    novaLista = []

    for valor in lista:
        if valor not in novaLista:
            novaLista.append(valor)

    novaLista.sort()
    return novaLista

def main():
    lista = [2, 4, 2, 2, 3, 3, 1, 1, 1, 2, 3, 7, 8]
    print(remove_repetidos(lista))

main()
