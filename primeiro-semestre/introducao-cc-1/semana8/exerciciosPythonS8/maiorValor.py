def maior_elemento(lista):
    
    maior = 0
    for valor in lista:
        if (valor > maior):
            maior = valor

    return maior

def main():
    lista = [1, 5, 7, 83, 3]
    print(maior_elemento(lista))

main()

