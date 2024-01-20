import math

def ehPar(n):
    if(n % 2 == 0):
        return True
    else:
        return False

#Retorna se um numero é ou não primo. 
def ehPrimo(n):
    achou = True

    if ehPar(n):
        if n == 2:
            return True
    else:
        i = 3
        while(i <= math.sqrt(n) and achou): #sqrt(n) diminui o custo do laço
            if(n % i == 0): #Procura por divisores. 
                achou = False  #Se encontrar um divisor não será primo. 
            i = i + 2

        return achou
    
#Retorna o maior numero primo <= n
def maior_primo(n):
    while(n > 0):
        if(ehPrimo(n)):
            return n
        n = n - 1   

n = int(input("n: "))

print(maior_primo(n))
