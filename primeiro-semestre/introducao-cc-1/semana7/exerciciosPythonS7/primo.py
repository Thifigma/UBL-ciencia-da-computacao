import math

def ehPrimo(n):
    achou = True

    if (n % 2 == 0):
        if n == 2:
            return True
    else:
        i = 3
        while(i <= math.sqrt(n) and achou): #sqrt(n) diminui o custo do laço
            if(n % i == 0): #Procura por divisores. 
                achou = False  #Se encontrar um divisor não será primo. 
            i = i + 2

        return achou

def main():

    n = int(input("Digite um número: "))

    if ehPrimo(n):
        print("Eh primo! :)")
    else:
        print("Não eh primo! :(")

main()
