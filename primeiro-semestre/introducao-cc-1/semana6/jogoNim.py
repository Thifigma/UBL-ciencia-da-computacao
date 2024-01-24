#N peças (total de peças).
#Pode-se retirar 1 ou m peças. 
#Quem tirar a ultima possivel ganha o jogo.
#Quem retirar a ultima peça  ganha o jogo.

import random

def ehMultiplo(n, m):
    if(n % (m + 1) == 0):
        return True
    else:
        return False


def computador_escolhe_jogada(n, m):
    num = random.randint(1, m)
   
    while ((n - num) % (m + 1) != 0):
        num = random.randint(1, m)

    print("Computador retirou ", num, " peças!")    
    return num


def usuario_escolhe_jogada(n, m):
    num = int(input("Quantas peças quer retirar? "))
    
    while (num > m or num <= 0):
        num = int(input("Número invalido! Tente novamente: "))

    return num

def partida(n, m):
    
    if ehMultiplo(n, m):
        print("Você começa!")
        
        while (n > 0):
            n = n - usuario_escolhe_jogada(n, m)
            print("Sobrou", n, " peças!")
            if (n <= 0):
                print("Você venceu!!!")
                break

            n = n - computador_escolhe_jogada(n, m)
            print("Sobrou", n, " peças!")
            if (n <= 0):
                print("O computador venceu!!!")
                break

    else:
        print("Computador começa!")

        while (n > 0):
            n = n - computador_escolhe_jogada(n, m)
            print("Sobrou", n, " peças!")
            if (n <= 0):
                print("Fim de jogo! O computador venceu!!!")
                break

            n = n - usuario_escolhe_jogada(n, m)
            print("Sobrou", n, " peças!")
            if (n <= 0):
                print("Fim de jogo! Você venceu!!!")
                break

def main(): 
    
    print("Bem-vindo(a) ao jogo NIM! Escolha: ")

    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    escolha = int(input())
        
    if(escolha == 1):
        n = int(input("Quantas peças? "))
        m = int(input("Limite de pelas por rodada? "))
        partida(n, m)

    if(escolha  == 2):
        print(" Você escolheu campeonato! ")
        n = int(input("Quantas peças? "))
        m = int(input("Limite de pelas por rodada? "))
        rodada = 1
        while (rodada <= 3):
            print("**** Rodada ",rodada,"*****")
            partida(n, m)
            rodada = rodada + 1
    
main()
