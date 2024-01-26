def main():
    col = int(input("Digite a quantidade de colunas:  "))
    lin = int(input("Digite a quantidade de linhas: "))

    i = 1
    while(i <= lin):
        j = 1 
        while(j < col):
            if(i == 1):#cima
                print("#", end ="")
            if(i == lin):#baixo
                print("#", end="")
            if(j == 1):#lado esquerdo
                print("#", end="")
            if(j == col - 1 and i > 1 and i < lin):
                print(" #", end="")
            if(i > 1 and i < lin and j > 1 and j < col - 1):
                print(" ", end="")
            j = j + 1
        i = i + 1
        print("")
main()
