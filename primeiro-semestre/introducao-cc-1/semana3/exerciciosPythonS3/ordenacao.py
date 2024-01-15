a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if a <= b:
    if b <= c: 
        print("crescente")
    else:
        print("não está em ordem crescente")
elif b <= c:
    if a < c:
        print("não está em ordem crescente")
    else:
        print("não está em ordem crescente")
else: 
    print("Não está em ordem crescente")
