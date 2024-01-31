def soma_elementos(lista):
    soma = 0
    for i in lista:
        soma = soma + i

    return soma


def main():
    lista = [5, 5, 5]
    print(soma_elementos(lista))

main()
