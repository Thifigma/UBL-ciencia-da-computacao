n = int(input("Digite um valor: "))

if n % 2 == 0: 
    if n == 2: 
        print("primo")
    else:
        print("não primo")
elif n % n == 0 and n % 1 == 0:
    print("primo")
else:
    print("não primo")
