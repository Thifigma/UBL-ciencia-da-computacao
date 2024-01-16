num = int(input("Digite um numero: "))
i = 0
anterior = 0
seq = False

while num != 0 and not seq:
    i = num % 10
    if i  == anterior:
        seq = True
    anterior = i
    num = num // 10

if seq:
    print("sim")
else: 
    print("não")
