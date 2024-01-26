def main():
    altura = int(input("Digite a altura: "))
    largura = int(input("Digite a largura: "))
    
    i = 0
    while(i < altura):
        j = 0
        while(j < largura):
            print("#", end = "")
            j = j + 1
        i = i + 1
        print("")
main()
